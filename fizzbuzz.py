#!bin/env python

# https://leetcode.com/problems/fizz-buzz/description/

def fizzbuzz(n):
    num_list = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            num_list.append('FizzBuzz')
        elif i % 3 == 0:
            num_list.append('Fizz')
        elif i % 5 == 0:
            num_list.append('Buzz')
        else:
            num_list.append(str(i))

    return num_list

print fizzbuzz(15)
