import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""

What did you see on line 1?
10
What was the smallest number you could have seen, what was the largest?
5,19

What did you see on line 2?
9
What was the smallest number you could have seen, what was the largest?
3,5,7,9
Could line 2 have produced a 4?
no

What did you see on line 3?
4.554299581540739
What was the smallest number you could have seen, what was the largest?
2.5, 4.5

"""

print(random.randint(1, 101))
