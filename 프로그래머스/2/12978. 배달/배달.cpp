#include <iostream>
#include <vector>
using namespace std;

int solution(int N, vector<vector<int> > road, int K) {
    int answer = 1;
    int INF = 100000000;
    vector<vector<int>> map = vector<vector<int>>(N+1, vector<int>(N+1, INF));
    
    for (vector<int> r: road) {
        int x = r[0];
        int y = r[1];
        int cost = r[2];
        
        map[x][y] = std::min(map[x][y], cost);
        map[y][x] = std::min(map[y][x], cost);
    }
    
    for (int i = 1; i < N + 1; i++) {
        for (int j = 1; j < N + 1; j++){
            for (int k = 1; k < N + 1; k++) {
                map[j][k] = std::min(map[j][k], map[j][i] + map[i][k]);
            }   
        }
    }
    
    for (int i = 2; i < N+1; i++) {
        if (map[1][i] <= K) {
            answer += 1;
        }
    }
    

    return answer;
}