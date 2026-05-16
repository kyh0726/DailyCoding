#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <map>

using namespace std;

struct Node {
    int genre_total_plays;
    int total_plays;
    int index;
};

struct Compare {
bool operator()(Node a, Node b) {

    if (a.genre_total_plays < b.genre_total_plays) {
        return true;
    }
    if (a.genre_total_plays > b.genre_total_plays) {
        return false;
    }
    
    
    if (a.total_plays < b.total_plays) {
        return true;
    }
    if (a.total_plays > b.total_plays) {
        return false;
    }
    
    if (a.index > b.index) {
        return true;
    }
    return false;
}
};  


vector<int> solution(vector<string> genres, vector<int> plays) {

    map<string, int> genre_play_counter;
    map<string, int> genre_max_counter;
    vector<int> answer;
    
    priority_queue<Node, vector<Node>, Compare> q;
    
    
    
    for (int i = 0; i < genres.size(); i++) {
        string cur_genre = genres[i];
        int cur_plays = plays[i];
        
        genre_play_counter[cur_genre] += cur_plays;
    }
    
    for (int i = 0; i < genres.size(); i++) {
        string cur_genre = genres[i];
        int cur_plays = plays[i];
        int genre_total_plays = genre_play_counter[cur_genre];
        q.push({genre_total_plays, cur_plays, i});
    }
    

    
    while (!q.empty()) {
        Node cur_song = q.top();
        q.pop();

        int cur_idx = cur_song.index;
        string cur_genre = genres[cur_idx];
        
        if (genre_max_counter[cur_genre] == 2) {
            continue;
        } else {
            genre_max_counter[cur_genre] += 1;
            answer.push_back(cur_idx);
        }
    }
    
    return answer;
}