#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
class SegmentTree {
public:

    SegmentTree(int k, string str) : k(k), str(vector<char>(str.begin(), str.end())) {
        int size = 4 * pow(2, k);
        tree.resize(size, 0);
        build(0, 0, pow(2, k) - 1);
    }
    void display() {
        for (int i = 0; i < tree.size(); ++i) {
            cout << tree[i] << " ";
        }
        cout << endl;
    }
    void change(int index, char command) {
        str.at(index) = command;
        vector<int> path;
        while (index > 0) {
            path.push_back(index);
            index = (index - 1) / 2;
        }
        path.push_back(0);
        query(0, path.size() - 1, path);
    }

    int getRootValue() {
        return tree[0];
    }

private:
    int k;
    vector<char> str;
    vector<int> tree;

    void build(ll node, int string_left, int string_right) {
        if (string_left == string_right) {
            tree[node] = 1;
            return;
        }
        int string_mid = string_left + (string_right - string_left) / 2;
        auto [left_child, right_child] = getChild(node);
        build(left_child, string_left, string_mid);
        build(right_child, string_mid + 1, string_right);
        setValue(node);
    }

    pair<int, int> getChild(ll node) {
        ll left = 2 * node + 1;
        ll right = 2 * node + 2;
        return pair<ll, ll>{left, right};
    }

    void query(ll node, int index, vector<int> &path) {
        if (index == 0) {
            setValue(node);
            return;
        }
        auto [left_child, right_child] = getChild(node);
        if (path[index - 1] == left_child) {
            query(left_child, index - 1, path);
        } else {
            query(right_child, index - 1, path);
        }
        setValue(node);
    }

    void setValue(ll node) {
        auto [left, right] = getChild(node);
        if (str[node] == '1') {
            tree[node] = tree[left];
        } else if (str[node] == '0') {
            tree[node] = tree[right];
        } else {
            tree[node] = tree[left] + tree[right];
        }
    }
};

void mainFunction() {
    int k;
    cin >> k;
    string str;
    cin >> str;
    reverse(str.begin(), str.end());
    int q;
    cin >> q;
    vector<pair<int, char>> queries(q);
    for (int i = 0; i < q; ++i) {
        cin >> queries[i].first >> queries[i].second;
    }
    
    SegmentTree segmentTree(k, str);
    
    int length = pow(2, k);
    vector<int> answer;

    for (auto &[x, command] : queries) {
        segmentTree.change(length - x - 1, command);
        answer.push_back(segmentTree.getRootValue());
        // segmentTree.display();
    }
    for (int ans : answer) {
        cout << ans << endl;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    mainFunction();

    return 0;
}



