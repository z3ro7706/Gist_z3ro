#include <iostream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

class TrafficLightSystem {
private:
    static const int NUM_INTERSECTIONS = 4;
    static const int NUM_LIGHTS = 8;
    static const int LIGHT_STATES = 3; // 빨강(0), 노랑(1), 초록(2)
    
    // 신호등 상태를 문자열로 변환
    string stateToString(int state) {
        switch(state) {
            case 0: return "빨강";
            case 1: return "노랑";
            case 2: return "초록";
            default: return "오류";
        }
    }
    
    // 교차로별 신호등 배치 (각 교차로마다 2개씩)
    void printIntersectionLayout(const vector<int>& combination) {
        cout << "\n=== 교차로 신호등 상태 ===" << endl;
        for(int i = 0; i < NUM_INTERSECTIONS; i++) {
            cout << "교차로 " << (i+1) << ": ";
            cout << "신호등A(" << stateToString(combination[i*2]) << ") ";
            cout << "신호등B(" << stateToString(combination[i*2+1]) << ")" << endl;
        }
        cout << "------------------------" << endl;
    }

public:
    // 모든 가능한 조합의 수 계산
    long long calculateTotalCombinations() {
        return pow(LIGHT_STATES, NUM_LIGHTS);
    }
    
    // 특정 조합을 10진수에서 3진수로 변환하여 표시
    vector<int> getCombination(long long index) {
        vector<int> combination(NUM_LIGHTS);
        long long temp = index;
        
        for(int i = 0; i < NUM_LIGHTS; i++) {
            combination[i] = temp % LIGHT_STATES;
            temp /= LIGHT_STATES;
        }
        
        return combination;
    }
    
    // 실제 교통 규칙을 고려한 유효한 조합 계산
    bool isValidTrafficState(const vector<int>& combination) {
        // 각 교차로에서 양방향 신호가 동시에 초록불이면 안됨 (충돌 방지)
        for(int i = 0; i < NUM_INTERSECTIONS; i++) {
            int lightA = combination[i*2];     // 교차로 i의 첫 번째 신호등
            int lightB = combination[i*2+1];   // 교차로 i의 두 번째 신호등
            
            // 둘 다 초록불이면 유효하지 않음 (교통사고 위험)
            if(lightA == 2 && lightB == 2) {
                return false;
            }
        }
        return true;
    }
    
    // 모든 조합 분석
    void analyzeAllCombinations() {
        long long totalCombinations = calculateTotalCombinations();
        long long validCombinations = 0;
        
        cout << "=== 교차로 신호등 시스템 분석 ===" << endl;
        cout << "교차로 수: " << NUM_INTERSECTIONS << "개" << endl;
        cout << "신호등 수: " << NUM_LIGHTS << "개" << endl;
        cout << "신호 상태: " << LIGHT_STATES << "가지 (빨강, 노랑, 초록)" << endl;
        cout << "총 가능한 조합: " << totalCombinations << "가지" << endl << endl;
        
        // 처음 몇 개 조합 예시 출력
        cout << "=== 처음 5개 조합 예시 ===" << endl;
        for(int i = 0; i < 5 && i < totalCombinations; i++) {
            vector<int> combination = getCombination(i);
            cout << "조합 " << (i+1) << ":";
            for(int j = 0; j < NUM_LIGHTS; j++) {
                cout << " " << stateToString(combination[j]);
            }
            cout << " -> " << (isValidTrafficState(combination) ? "유효" : "무효") << endl;
        }
        
        // 유효한 조합 개수 계산
        cout << "\n=== 교통 규칙 적용 분석 ===" << endl;
        cout << "분석 중..." << endl;
        
        for(long long i = 0; i < totalCombinations; i++) {
            vector<int> combination = getCombination(i);
            if(isValidTrafficState(combination)) {
                validCombinations++;
            }
        }
        
        cout << "교통 규칙을 고려한 유효한 조합: " << validCombinations << "가지" << endl;
        cout << "무효한 조합: " << (totalCombinations - validCombinations) << "가지" << endl;
        cout << "유효한 조합 비율: " << (double)validCombinations/totalCombinations*100 << "%" << endl;
    }
    
    // 특정 조합 상세 표시
    void showDetailedCombination(long long index) {
        if(index >= calculateTotalCombinations()) {
            cout << "잘못된 인덱스입니다!" << endl;
            return;
        }
        
        vector<int> combination = getCombination(index);
        cout << "\n=== 조합 " << (index+1) << " 상세 정보 ===" << endl;
        printIntersectionLayout(combination);
        cout << "교통 규칙 준수: " << (isValidTrafficState(combination) ? "예" : "아니오") << endl;
    }
};

int main() {
    TrafficLightSystem system;
    
    // 기본 분석 실행
    system.analyzeAllCombinations();
    
    // 사용자 입력으로 특정 조합 확인
    char choice;
    cout << "\n특정 조합을 자세히 보시겠습니까? (y/n): ";
    cin >> choice;
    
    if(choice == 'y' || choice == 'Y') {
        long long index;
        cout << "조합 번호를 입력하세요 (1-" << system.calculateTotalCombinations() << "): ";
        cin >> index;
        system.showDetailedCombination(index - 1);
    }
    
    cout << "\n프로그램을 종료합니다." << endl;
    return 0;
}