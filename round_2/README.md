# Contest Solution and Approaches

## Contest Round 2
## Puzzle Peices 
- [Problem](https://codeforces.com/problemset/problem/1345/A)

Approach 
In this problem The Pieces can placed perfectely only when we have single column or row.

But in addition to that we can place pieces if they have two rows and two columns.

![Solution](round_2/A_Puzzle_Pieces.py)

## Not Dividing
- [Problem](https://codeforces.com/problemset/problem/1794/B)

In this problem the required is only that a[i + 1] should not be divided by a[i] for all 0 <= i < n

We know that this means it is considering the previous number only. 

for this reason, here is what we are going to do. We start from i = 1 (0-index) and we will check if the current is divisible by previous number, if true we will increament the current number only by one. but there is one edge case if our a[0] == 1

eg: a = [1, 2, 3]

we know that 2 % 1 == 0, then we increament 2 by one 
then a = [1, 3, 3] -> but notice 3 is still divisible by 1

to avoid this case we starting making the first element different from 1.
![Solution](round_2/B_Not_Dividing.py)

## Settlement Of Guinea Pigs
[Problem](https://codeforces.com/problemset/problem/1802/B)
In this problem we know that if the dector helped us to indetify the genders we can put males into male avaries but until we know which guinea pigs we can not put any of them together because we are not sure. 

So until we know the genders we would need the numbers of guinea pigs avaries. 

but once we know the which guinea pigs is male or female, i.e the doctor helped us, at that moment we can have two cases 

let say n = number of the guinea pigs after the doctor identified the gender of the guinea pigs

1. if n is even 
2. if n odd

####  In the second case we use simple calculation. 

```python 
avaries = (n + 1) // 2
```

because we know the guinea pig will fall into one with the same gender or new one.

#### For the first case

lets take n = 4

then if the gender of the Guinea Pigs is 
m m m f

Then we can place them in these manner  [m,m], [m], [f] and this is the best we can do. 

So whenever n is even we will have 

```python 
avaries = ((n + 1) + 1) // 2
```

But we also need keep in mind that we have the guinea pigs that are bought after the doctor identified the existing guinea pigs in that case we will have an additional box
```python 
avaries += k # number of guinea pigs bought after the doctor identified the guinea pigs
```

Then we need to keep track of the maximum avaries on the way.

![Solution](round_2/C_Settlement_of_Guinea_Pigs.py)



## Begginer's Zelda
[Problem](https://codeforces.com/problemset/problem/1905/B)

In this problem We have a greedy solution.

so if have n numbers of the leaves our solution will be 
```python 
solution = (n + 1) // 2

```
This happens because of this 
if we started at specific leave we can make all the nodes on the path from u current leave to v the other because incase of tree there is always path from leave to another leave.

![Solution](round_2/D_Begginer_s_Zelda.py)

