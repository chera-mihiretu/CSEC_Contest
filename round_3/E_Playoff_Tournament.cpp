#include <bits/stdc++.h>

using namespace std;
class SegmentTree{
    public:
    vector<int> tree;
    vector<char> s;
        SegmentTree(int k, string s){
            this->s.assign(s.begin(), s.end());
            tree.assign(4*k, 0);
            build(0, 0, k-1);
        }
   
        
        void build(int node, int left, int right){
            if (left == right){
                this->tree[left] = 1;
                return;
            }

            int mid = left + (right - left) / 2;
            pair<int, int> children = getChild(node);

            build(children.first, left, mid);
            build(children.second, mid+1, right);

            setTheValues(s[node], children);

        }

        pair<int, int> getChild(int node){
            return make_pair(2*node, 2*node+1);
        }

        void changeIt(vector<int> path, int index, int node){
            pair<int, int> children = getChild(node);
            if (index == 0){
                setTheValues(s[node], children);
                return;
            }

            if (children.first == path[index - 1]){
                changeIt(path, index-1, children.first);
            }else if (children.second == path[index - 1]){
                changeIt(path, index-1, children.second);
            }

            setTheValues(s[node], children);
        }
        void changePos(int index, char value){
            s[index] = value;
            vector<int> path;
            while (index) {
                path.push_back(index);
                index = (index - 1) / 2;
            }
            path.push_back(0);
            changeIt(path, path.size() - 1, 0);
            
        }


        void setTheValues(char node, pair<int, int> children){
            if (node == '0'){
                this->tree[node] = this->tree[children.first];
            }else if (node == '1'){
                this->tree[node] = this->tree[children.second];
            }else{
                this->tree[node] = this->tree[children.first] + this->tree[children.second];
            }
        }
        int getAnswer(){
           
            return this->tree[0];
        }   
};

int main(){
    int k, q, n;
    string values;
    cin >> k;
    cin >> values;
    cin >> q;
    n = values.size();
    SegmentTree* seg = new SegmentTree(k, values);
    vector<int> answer;
    while (q){
        int position;
        char value;
        for (auto i : seg->tree){
            cout << i << " ";
        }
        cin >> position >> value;
        seg->changePos(n - position, value);
        answer.push_back(seg->getAnswer());
        
        q--;
    }

    for (auto i : answer){
        cout << i << endl;
    }

}