#include <bits/stdc++.h> 
using namespace std;


#define ll long long
#define pb push_back
#define all(v) v.begin(), v.end()
#define rall(v) v.rbegin(), v.rend()
#define F first
#define S second
#define endl '\n'

const ll MOD = 1e9 + 7;
const ll INF = 1e18;


void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
}


bool checkKal(vector<int>&arr, int jump){
    int start = 0;
    int end = arr.size() - 1;

    while (start < end) {
        if (arr[start] == arr[end]) {
            start ++;
            end --;
        } else {
            if (arr[start] == jump) {
                start ++;
            } else if (arr[end] == jump) {
                end --;
            }else{
                return false;
            }
        }
    }
    return true;
}


int main() {
    fastIO();

    int t = 1; 
    cin >> t; 
    while (t--) {
        
        int n;
        cin >> n; 

        int start = 0;
        int end = n - 1;

        vector<int> arr(n, 0);

        for (int i = 0; i < n; i++) {
            cin >> arr[i];
        }
        

        bool changed = false;
        int left = -1;
        int right = -1;

        while (start < end) {
            if (arr[start] == arr[end]) {
                start++;
                end--;
            }else {
                left = arr[start];
                right = arr[end];
                break;
            }
        }

        
        if (left == -1 && right == -1) {
            cout << "YES" << endl;
            continue;
        }

        if (checkKal(arr, left) || checkKal(arr, right)) {
            cout << "YES" << endl;
        }else {
            cout << "NO" << endl;
        }


        
    }

    return 0;
}
