// lucky me 
#include <bits/stdc++.h>
#define all(arr) arr.begin(), arr.end()
#define Arr(T) vector<T> 
#define Pair(T) pair<int,int>
#define f first
#define s second

using namespace std;    
typedef long long ll;

bool good(vector<int> nums, int k) {
    sort(all(nums));
    for (int i = 1; i <= k; i++) {
        int target = k - i + 1;
        int index = upper_bound(all(nums), target) - nums.begin() - 1;

        if (index < 0) return false;
        nums.erase(nums.begin() + index);
        if (nums.empty()) return true;
        nums[0] += target;
        sort(all(nums));
        
    }
    return true;
}

int solve() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];

    int left = 1, right = n, ans = 0;
    while (left <= right) {
        int mid = (left + right) / 2;
        if (good(nums, mid)) {
            ans = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    cout << ans << endl;
    return ans;
}

int main() {

    int t;
    cin >> t;
    while (t--) solve();            
}
