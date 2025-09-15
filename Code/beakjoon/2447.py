def make_star(n:int):
    if(len(n)==1):
        return "*"

    star_unit=make_star(n//3)
    star_res=star_unit+[[" "]*(n//3)]*n//3+star_unit

    return star_res


while(True):  #값을 파일로 input해서 받아내는 법
    try:
        n=int(input())
        print(make_star(n))
    except:
        break