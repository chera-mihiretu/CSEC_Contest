// lucky me 
#include <bits/stdc++.h>
#define all(arr) arr.begin(), arr.end()
#define Arr(T) vector<T> 
#define Pair(T) pair<int,int>
#define f first
#define s second
using namespace std;    

int main () {

    int n, m;
    cin >> n >> m;

    Arr(Pair(int)) left(n);
    Arr(Pair(int)) right(n);

    for (int i = 0; i < n; i ++) {
        left[i].f = (i * 2) + 1;
        left[i].s = ((n + i) * 2) + 1 ;
        right[i].f = ((n + i) * 2 + 2);
        right[i].s = ((i + 1) * 2) ;
    }


    int turn = 0;
    int temp = n * 4;
    int index = 0;
    while (temp--) {
        if (turn == 0) {
            if (left[index].s <= m) {
                cout << left[index].s << ' ';
            }
        }else if (turn == 1) {
            if (left[index].f <= m) {
                cout << left[index].f << ' ';
            }
        }else if (turn == 2) {
            if (right[index].f <= m) {
                cout << right[index].f << ' ';
            }
        } else {
            if (right[index].s <= m) {
                cout << right[index].s << ' ';
            }
        }
        turn ++;
        index += turn / 4;
        turn = turn % 4;
       
    }
    cout << endl;
    

    

}