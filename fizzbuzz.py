# Day 2

"""
Code Challenge
  Name:
    Fizz Buzz
  Filename:
    fizzbuzz.py
  Problem Statement:
    Write a Python program which iterates the integers from 1 to 50(included).
    For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
    For numbers which are multiples of both three and five print "FizzBuzz".
    User Input not required
  Output:
    1
    2
    Fizz
    4
    Buzz
"""
ip = range(1,51)#assigning all natural numbers upto 50 into a range
for integer in ip:#iterating for range, ip
    if (integer%3 == 0) and (integer%5 == 0):#condition for multiple for both 3 & 5
        print('FizzBuzz')
    elif (integer%3 == 0):#condition for multiple for 3
        print('Fizz')
    elif (integer%5 == 0):#condition for multiple for 5
        print('Buzz')
    else:#condition for multiple for all other integer
        print(integer)
