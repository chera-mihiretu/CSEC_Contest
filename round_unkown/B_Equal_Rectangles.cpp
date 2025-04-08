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


int main() {
    fastIO();

    int t; 
    scanf("%d", &t);
    while (t--) {
        int n;
        scanf("%d", &n);
        vector<int> a(n);
        for (int i = 0; i < n * 4; ++ i) {
            scanf("%d ", &a[i]);
        }

        unordered_set<int> nums;

        for (int i = 0; i < nums.size(); i ++ ){
            printf("akjdfhlaj\n");
             
            nums.insert(a[i]);
            
            
        }

        vector<int> unique;
        
        for (auto a : nums) {
            printf("%s ", "hellow");
            unique.push_back(a);
        }

        sort(unique.begin(), unique.end());

        for (auto c : unique) {
            printf("%d ", c);
        }
        printf("\n");

        int start = 0;
        int end = unique.size() - 1;
        int prev = -1;
        while (start < end) {
            if (prev == -1) {
                prev = unique[start] * unique[end];
            }else {
                if (prev != unique[start] * unique[end]) {
                    printf("NO\n");
                    break;
                }
            }
        }

        printf("YES\n");




        
    }

    return 0;
}
