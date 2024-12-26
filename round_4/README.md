# Welcome to the CPD contest round 4

Stay tuned for more details and updates.


### 1. Showstpper 

The question 
```
You are given two arrays a1,a2,…,an
 and b1,b2,…,bn
.

In one operation, you can choose any integer i from 1 to n and swap the numbers ai and bi
.

Determine whether, after using any (possibly zero) number of operations, the following two conditions can be satisfied simultaneously:

an=max(a1,a2,…,an),
bn=max(b1,b2,…,bn)
.
Here max(c1,c2,…,ck)
 denotes the maximum number among c1,c2,…,ck
. For example, max(3,5,4)=5, max(1,7,7)=7, max(6,2)=6
```

In here what we do know is that the answer lies in the last number 

So we do the following 

bring every big number than the last element in b two the position in a

then do the same thing by swapping the last two elements.

![Showstopper](A_Showstopper.py)

### 2. Coder

To solve this problem we can think in zig zag
if we have 3 x 3 matrix we can place one 'C' at (0,0) and another 'C' at (1,1 )and another at (0,2) but that is not the problem it is how do we know how much c we placed we can either count when we are placing or count it mathimathically.

for mathimathically we can use 

```
number_of_c = (row // 2) * row  

number_of_c += (row + 1) // 2 if our n is odd

```

![Coders](B_Coder.py)