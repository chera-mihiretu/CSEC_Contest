# Welcome to the CPD contest round 4

Stay tuned for more details and updates.

### 1. Showstopper

The question:
```
You are given two arrays a1, a2, ..., an and b1, b2, ..., bn.

In one operation, you can choose any integer i from 1 to n and swap the numbers ai and bi.

Determine whether, after using any (possibly zero) number of operations, the following two conditions can be satisfied simultaneously:

an = max(a1, a2, ..., an),
bn = max(b1, b2, ..., bn).
Here max(c1, c2, ..., ck) denotes the maximum number among c1, c2, ..., ck. For example, max(3, 5, 4) = 5, max(1, 7, 7) = 7, max(6, 2) = 6.
```

The answer lies in the last number. So we do the following:

1. Bring every number greater than the last element in b to the position in a.
2. Then do the same thing by swapping the last two elements.

![Showstopper](A_Showstopper.py)

### 2. [Coder](https://codeforces.com/problemset/problem/384/A)

To solve this problem, we can think in a zigzag pattern. If we have a 3x3 matrix, we can place one 'C' at (0,0), another 'C' at (1,1), and another at (0,2). The problem is how to know how many 'C's we placed. We can either count while placing them or count mathematically.

Mathematically, we can use:
```
number_of_c = (row // 2) * row  
number_of_c += (row + 1) // 2 if our n is odd
```

![Coders](B_Coder.py)

### 3. Bow Wow and The Timetable

In this problem, we know that if people arrive at 1000, they will miss trains from 1, 100. We only count the number of multiples of 4 we can find in the range of their arrival. This means we move two steps from the back to the front every time, and if we are still in the range, we know that these people missed the train at this specific position.

Another case is if they arrive at 10000, they will miss trains from 1, 100,. We know that the time of arrival must be strictly greater than the train's take-off time. For that, we will check the existence of one before the last 1, which is at position 0.

![Solution](C_1_BowWow_and_the_Timetable.py)
