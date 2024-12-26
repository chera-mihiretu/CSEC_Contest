#include <bits/stdc++.h>

using namespace std;


int spread(vector<vector<int>>& graph, vector<int>& allAnswer, vector<int>& child_count, int node, int parent){
    int children = 1;
    allAnswer.push_back(node);
    for (auto child : graph[node]){
        if (child != parent){
            children += spread(graph, allAnswer, child_count, child, node);
        }
    }
    child_count[node] = children;
    return children;
}




int main (){
    int n, q; 
    cin >> n >> q;
    vector<int> allAnswer;
    vector<vector<int>> graph(n, vector<int>());
    vector<int> child_count(n, 0);
    vector<int> answer(q, -1);
    for (int i = 0; i < n - 1; ++i){
        int child;
        cin >> child;
        graph[child - 1].push_back(i + 1);
        graph[i + 1].push_back(child - 1);
    }

    for (vector<int> &v : graph){
        sort(v.begin(), v.end());
    }

    spread(graph, allAnswer, child_count, 0, -1);
    unordered_map<int, int> map;
    for (int i = 0; i < allAnswer.size(); i ++){
        map[allAnswer[i]] = i;
    }
    
    for (int i = 0; i < q; i ++ ){
        int u, k;
        cin >> u >> k;
        u --;
        k --;
        int start_index = map[u];
        // cout << k;
        int end_k = start_index + k;
        // cout << "start_index: " << start_index << " end_k: " << end_k << endl;
        if (k < child_count[u]){
            answer[i] = allAnswer[end_k] + 1;
        } 
        cout << answer[i] << endl;
    }


    




}