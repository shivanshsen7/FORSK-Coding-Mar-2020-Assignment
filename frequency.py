# Day 5
"""
Name: 
    Character Frequency       
Filename:
    frequency.py 
Problem Statement:
    This program accepts a string from User and counts the number of characters 
    (character frequency) in the input string. 

Sample Input:
    www.google.com
Sample Output:
    {'c': 1, 'e': 1, 'g': 2, 'm': 1, 'l': 1, 'o': 3, '.': 2, 'w': 3}
""" 
#remove Cooment in-case need custom input
#str_in = input('Please enter a String to evaluate: ')

str_in = r'www.google.com'
#converting string to sorted list and making a set 
str_list = list(str_in)
str_list.sort()
str_set = set(str_list)
#list-compehension to get count of each character from set & zipping it in 
#Dictionary
str_dict=dict(zip(str_set,tuple(map(lambda x : str_list.count(x),str_set))))
#Sorting Dictionary based on Key
for key in sorted(str_dict.keys()):
    print('\'',key,'\'',"is repeated overs",str_dict[key],"times in string.")
