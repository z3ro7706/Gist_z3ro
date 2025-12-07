import discord
from discord.ext import commands, tasks
from datetime import datetime, timedelta
import asyncio

# =========================
# 설정 부분
# =========================
TOKEN = "YOUR_BOT_TOKEN_HERE"  # 👉 여기에 실제 봇 토큰 넣기

# 채널 이름 (실제 디스코드 서버 채널 이름과 동일하게!)
CREATE_CHANNEL_NAME = "내전생성방"   # 명령어 입력 채널
ANNOUNCE_CHANNEL_NAME = "내전안내"   # 안내가 올라갈 채널  (띄어쓰기 없음!)

# 사용할 이모지
CHECK_EMOJI = "✅"  # 참가
LIST_EMOJI = "📋"   # 참가자 리스트 출력

# 인텐트 설정
intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# 내전 정보를 저장할 딕셔너리
# key: 안내 메세지 ID, value: dict(...)
raids = {}

# 고유 코드 -> 메시지 ID 매핑
raid_code_map = {}

# 고유 코드 생성용 카운터
raid_counter = 1


# =========================
# 유틸 함수들
# =========================
def parse_game_datetime(date_str, time_str):
    """
    유저가 입력한 날짜/시간 문자열을 datetime 객체로 변환.
    지원 예시:
      날짜 : "2025-12-25", "12-25", "2025.12.25", "12/25"
      시간 : "21:00", "21:00:00"
    """
    now = datetime.now()

    # 날짜 파싱 시도
    date_formats = ["%Y-%m-%d", "%m-%d", "%Y.%m.%d", "%m/%d"]
    game_date = None

    for fmt in date_formats:
        try:
            tmp = datetime.strptime(date_str, fmt)
            # 연도가 없는 형식인 경우(예: %m-%d, %m/%d)는 올해로 간주
            if "%Y" not in fmt:
                tmp = tmp.replace(year=now.year)
            game_date = tmp
            break
        except ValueError:
            continue

    if game_date is None:
        return None  # 파싱 실패

    # 시간 파싱 시도
    if time_str:
        time_formats = ["%H:%M", "%H:%M:%S"]
        for tfmt in time_formats:
            try:
                t = datetime.strptime(time_str, tfmt).time()
                game_date = game_date.replace(
                    hour=t.hour, minute=t.minute, second=t.second
                )
                break
            except ValueError:
                continue
        # 시간 형식이 안 맞으면 그냥 00:00 기준으로 둔다.

    return game_date


def generate_raid_code():
    """R0001, R0002 처럼 고유 코드 생성"""
    global raid_counter
    code = f"R{raid_counter:04d}"
    raid_counter += 1
    return code


async def delete_after(message: discord.Message, delay: int):
    """delay초 후에 해당 메시지를 삭제"""
    await asyncio.sleep(delay)
    try:
        await message.delete()
    except discord.HTTPException:
        # 삭제 실패해도 봇이 죽지 않도록 그냥 무시
        pass


# =========================
# 봇 준비 완료
# =========================
@bot.event
async def on_ready():
    print(f"✅ 로그인 완료: {bot.user} (id: {bot.user.id})")

    # 백그라운드 정리 작업 시작
    if not cleanup_old_raids.is_running():
        cleanup_old_raids.start()
        print("🧹 cleanup_old_raids 루프 시작")


# =========================
# 메시지 감지
# =========================
@bot.event
async def on_message(message: discord.Message):
    # 다른 봇이 보낸 메시지는 무시
    if message.author.bot:
        return

    # 지정한 채널에서만 내전 관련 명령 처리
    if message.channel.name == CREATE_CHANNEL_NAME:
        content = message.content.strip()

        if content.startswith("./내전생성"):
            await handle_create_raid_command(message)
        elif content.startswith("./내전취소"):
            await handle_cancel_raid_command(message)
        elif content.startswith("./내전수정"):
            await handle_edit_raid_command(message)

    # commands 확장 기능도 같이 동작하게
    await bot.process_commands(message)


# =========================
# ./내전생성 처리
# =========================
async def handle_create_raid_command(message: discord.Message):
    # "./내전생성 " 뒤의 내용만 떼기
    parts = message.content.split(maxsplit=1)
    if len(parts) < 2:
        await message.channel.send("형식: `./내전생성 종류/날짜/시간/필요인원`")
        return

    args = parts[1].strip()  # "롤/2025-12-25/21:00/10" 등
    tokens = [t.strip() for t in args.split("/")]

    if len(tokens) != 4:
        await message.channel.send(
            "형식: `./내전생성 종류/날짜/시간/필요인원` 으로 입력해줘!"
        )
        return

    game_type, date_str, time_str, need_str = tokens

    # 필요 인원 숫자 체크
    try:
        need_count = int(need_str)
    except ValueError:
        await message.channel.send("`필요인원`은 숫자로 적어줘! (예: 5, 10)")
        return

    # 안내 채널 찾기
    announce_channel = discord.utils.get(
        message.guild.text_channels,
        name=ANNOUNCE_CHANNEL_NAME
    )

    if announce_channel is None:
        await message.channel.send(
            f"`{ANNOUNCE_CHANNEL_NAME}` 채널을 찾을 수 없어요. "
            f"채널 이름을 실제 서버 이름에 맞게 코드에서 바꿔줘야 해요."
        )
        return

    # 고유 코드 생성
    raid_code = generate_raid_code()

    # 생성자 닉네임
    creator_name = message.author.display_name

    # 안내 메시지 내용
    content = (
        "[내전안내]\n"
        f"고유코드 : {raid_code}\n"
        f"게임종류 : {game_type}\n"
        f"날짜 : {date_str}\n"
        f"시간 : {time_str}\n"
        f"필요인원 : {need_count}\n"
        f"생성자 : {creator_name}"
    )

    # 안내 채널에 메시지 보내기
    info_message = await announce_channel.send(content)

    # 참가 / 리스트 이모지 달기
    await info_message.add_reaction(CHECK_EMOJI)
    await info_message.add_reaction(LIST_EMOJI)

    # 이 메시지에 대한 내전 정보 저장
    raids[info_message.id] = {
        "code": raid_code,
        "game_type": game_type,
        "date": date_str,
        "time": time_str,
        "need": need_count,
        "members": [],         # user_id 리스트 (참가 순서대로)
        "channel_id": info_message.channel.id,
        "creator_id": message.author.id,
        "creator_name": creator_name,
    }

    raid_code_map[raid_code] = info_message.id

    # 생성되었다고 생성방에도 안내
    await message.channel.send(f"내전이 생성되었어! 고유코드: `{raid_code}`")


# =========================
# ./내전취소 [고유코드]
# =========================
async def handle_cancel_raid_command(message: discord.Message):
    parts = message.content.split(maxsplit=1)
    if len(parts) < 2:
        await message.channel.send("형식: `./내전취소 고유코드`")
        return

    raid_code = parts[1].strip()

    if raid_code not in raid_code_map:
        await message.channel.send("해당 고유코드의 내전을 찾을 수 없어요.")
        return

    msg_id = raid_code_map[raid_code]
    raid = raids.get(msg_id)
    if raid is None:
        await message.channel.send("이미 삭제되었거나 존재하지 않는 내전이에요.")
        return

    # 안내 채널 가져오기
    announce_channel = discord.utils.get(
        message.guild.text_channels,
        name=ANNOUNCE_CHANNEL_NAME
    )

    if announce_channel is None:
        await message.channel.send(
            f"`{ANNOUNCE_CHANNEL_NAME}` 채널을 찾을 수 없어요."
        )
        return

    # 원래 안내 메시지 삭제 시도
    try:
        msg = await announce_channel.fetch_message(msg_id)
        await msg.delete()
    except discord.NotFound:
        pass

    # ✅ 참가자들에게 DM 발송
    guild = message.guild
    if guild is not None:
        dm_text = (
            "[내전 취소 안내]\n"
            f"고유코드 : {raid_code}\n"
            f"게임종류 : {raid['game_type']}\n"
            f"날짜 : {raid['date']}\n"
            f"시간 : {raid['time']}\n"
            f"필요인원 : {raid['need']}\n"
            "참가 중이던 내전이 취소되었습니다."
        )
        for user_id in raid["members"]:
            member = guild.get_member(user_id)
            if member is None:
                continue
            try:
                await member.send(dm_text)
            except discord.Forbidden:
                # DM 막아놓은 사람 등
                pass
            except discord.HTTPException:
                pass

    # 취소 안내 메시지 (내전안내 채널에 공지)
    cancel_text = (
        "[내전취소 안내]\n"
        f"고유코드 : {raid_code}\n"
        f"게임종류 : {raid['game_type']}\n"
        f"날짜 : {raid['date']}\n"
        f"시간 : {raid['time']}\n"
        f"필요인원 : {raid['need']}\n"
        f"생성자 : {raid['creator_name']}\n"
        f"해당 내전이 취소되었습니다."
    )
    await announce_channel.send(cancel_text)

    # dict에서 제거 (마지막에)
    raids.pop(msg_id, None)
    raid_code_map.pop(raid_code, None)

    # 명령 내린 사람에게도 피드백
    await message.channel.send(f"고유코드 `{raid_code}` 내전이 취소되었어요.")


# =========================
# ./내전수정 [코드]/[종류]/[날짜]/[시간]/[필요인원]
# =========================
async def handle_edit_raid_command(message: discord.Message):
    parts = message.content.split(maxsplit=1)
    if len(parts) < 2:
        await message.channel.send(
            "형식: `./내전수정 고유코드/종류/날짜/시간/필요인원`"
        )
        return

    args = parts[1].strip()
    tokens = [t.strip() for t in args.split("/")]

    if len(tokens) != 5:
        await message.channel.send(
            "형식: `./내전수정 고유코드/종류/날짜/시간/필요인원` 으로 입력해줘!"
        )
        return

    raid_code, game_type, date_str, time_str, need_str = tokens

    if raid_code not in raid_code_map:
        await message.channel.send("해당 고유코드의 내전을 찾을 수 없어요.")
        return

    # 필요 인원 숫자 체크
    try:
        need_count = int(need_str)
    except ValueError:
        await message.channel.send("`필요인원`은 숫자로 적어줘! (예: 5, 10)")
        return

    msg_id = raid_code_map[raid_code]
    raid = raids.get(msg_id)

    if raid is None:
        await message.channel.send("이미 삭제되었거나 존재하지 않는 내전이에요.")
        return

    # 안내 채널 가져오기
    announce_channel = discord.utils.get(
        message.guild.text_channels,
        name=ANNOUNCE_CHANNEL_NAME
    )

    if announce_channel is None:
        await message.channel.send(
            f"`{ANNOUNCE_CHANNEL_NAME}` 채널을 찾을 수 없어요."
        )
        return

    # 원래 메시지 가져오기
    try:
        msg = await announce_channel.fetch_message(msg_id)
    except discord.NotFound:
        await message.channel.send("원래 안내 메시지를 찾을 수 없어요.")
        return

    # raid 정보 업데이트 (참가자는 그대로 유지)
    raid["game_type"] = game_type
    raid["date"] = date_str
    raid["time"] = time_str
    raid["need"] = need_count

    # 수정된 안내 메시지 내용 (고유코드, 생성자, 참가자는 그대로)
    new_content = (
        "[내전안내 - 수정됨]\n"
        f"고유코드 : {raid['code']}\n"
        f"게임종류 : {raid['game_type']}\n"
        f"날짜 : {raid['date']}\n"
        f"시간 : {raid['time']}\n"
        f"필요인원 : {raid['need']}\n"
        f"생성자 : {raid['creator_name']}"
    )

    # 기존 안내 메시지 내용 수정
    await msg.edit(content=new_content)

    # 원문 내전 안내에 "답장" 형태로 수정 안내
    notify_text = (
        f"[내전 수정 안내]\n"
        f"고유코드 {raid['code']} 내전이 수정되었습니다."
    )
    await msg.reply(notify_text, mention_author=False)

    # 참가자들에게 DM 발송
    guild = message.guild
    if guild is not None:
        dm_text = (
            "[내전 수정 안내]\n"
            f"고유코드 : {raid['code']}\n"
            f"게임종류 : {raid['game_type']}\n"
            f"날짜 : {raid['date']}\n"
            f"시간 : {raid['time']}\n"
            f"필요인원 : {raid['need']}\n"
            "참가 중인 내전의 정보가 수정되었습니다."
        )

        for user_id in raid["members"]:
            member = guild.get_member(user_id)
            if member is None:
                continue
            try:
                await member.send(dm_text)
            except discord.Forbidden:
                # DM을 차단했거나 받을 수 없는 경우
                pass
            except discord.HTTPException:
                # 기타 전송 오류
                pass

    # 수정 명령을 사용한 사람에게도 피드백
    await message.channel.send(f"고유코드 `{raid_code}` 내전 정보를 수정했어요.")


# =========================
# 리액션 추가 이벤트
# =========================
@bot.event
async def on_raw_reaction_add(payload: discord.RawReactionActionEvent):
    # 봇이 단 리액션은 무시
    if payload.user_id == bot.user.id:
        return

    message_id = payload.message_id

    # 이 메시지가 우리가 관리하는 내전 메시지인가?
    if message_id not in raids:
        return

    emoji = str(payload.emoji)
    raid = raids[message_id]

    # ✅ 참가 토글 (추가만 여기서, 제거는 on_raw_reaction_remove에서)
    if emoji == CHECK_EMOJI:
        if payload.user_id not in raid["members"]:
            raid["members"].append(payload.user_id)

    # 📋 참가자 리스트 출력 (답장 + 2분 뒤 자동 삭제)
    elif emoji == LIST_EMOJI:
        guild = bot.get_guild(payload.guild_id)
        if guild is None:
            return

        channel = bot.get_channel(payload.channel_id)
        if channel is None:
            return

        # 원본 내전 안내 메시지 가져오기 (답장 달기 위해)
        try:
            original_msg = await channel.fetch_message(message_id)
        except discord.NotFound:
            return

        # 참가자 문자열 만들기
        if not raid["members"]:
            text = (
                f"고유코드 : {raid['code']}\n"
                "참가 인원 : 아직 아무도 없습니다."
            )
        else:
            lines = []
            for idx, user_id in enumerate(raid["members"], start=1):
                member = guild.get_member(user_id)
                if member is not None:
                    name = member.display_name
                else:
                    name = f"Unknown({user_id})"
                lines.append(f"{idx}. {name}")

            text = (
                f"고유코드 : {raid['code']}\n"
                "참가 인원 :\n" + "\n".join(lines)
            )

        # 원문 내전 안내에 "답장" 형태로 참가 리스트 보내기
        reply_msg = await original_msg.reply(text, mention_author=False)

        # 2분(120초) 뒤에 자동 삭제
        asyncio.create_task(delete_after(reply_msg, 120))


# =========================
# 리액션 제거 시 (참가 취소)
# =========================
@bot.event
async def on_raw_reaction_remove(payload: discord.RawReactionActionEvent):
    message_id = payload.message_id

    if message_id not in raids:
        return

    emoji = str(payload.emoji)
    if emoji != CHECK_EMOJI:
        return

    raid = raids[message_id]

    # 참가자가 ✅를 뗐으면 리스트에서 제거 (참가 취소)
    if payload.user_id in raid["members"]:
        raid["members"].remove(payload.user_id)


# =========================
# 오래된 내전 안내 자동 삭제
# =========================
@tasks.loop(minutes=30)  # 30분마다 한 번씩 체크
async def cleanup_old_raids():
    if not raids:
        return

    now = datetime.now()
    to_delete = []

    for msg_id, data in list(raids.items()):
        game_dt = parse_game_datetime(data["date"], data["time"])
        if game_dt is None:
            # 날짜 파싱 실패하면 그냥 건너뜀
            continue

        # 게임 날짜·시간 + 2일이 지났는지 체크
        if now >= game_dt + timedelta(days=2):
            channel = bot.get_channel(data["channel_id"])
            if channel is not None:
                try:
                    msg = await channel.fetch_message(msg_id)
                    await msg.delete()
                    print(f"🗑️ {msg_id} 내전 안내 메시지 삭제 완료")
                except discord.NotFound:
                    # 이미 수동으로 삭제된 경우
                    pass
                except discord.Forbidden:
                    print("❗ 메시지 삭제 권한이 없습니다.")
                except discord.HTTPException as e:
                    print(f"❗ 메시지 삭제 중 오류 발생: {e}")

            to_delete.append(msg_id)

    # 딕셔너리에서도 제거
    for mid in to_delete:
        raid = raids.pop(mid, None)
        if raid:
            code = raid.get("code")
            if code and code in raid_code_map:
                raid_code_map.pop(code, None)


# =========================
# 실행
# =========================
if __name__ == "__main__":
    bot.run("")
