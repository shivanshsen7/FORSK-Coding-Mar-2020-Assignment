# Day 4
"""
Name: 
    Vowels Finder
Filename: 
    vowels.py
Problem Statement:
    Remove all the vowels from the list of state
Hint: 
    Use nested for loops and while
Sample Input:
    state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
Sample Output:
    ['lbm', 'clfrn', 'klhm', 'flrd'] 
"""
#SAMPLE INPUT
state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']


#VOWELS : 'a','e','i','o','u' 
#or : 'A','E','I','O','U' 

#OUTPUT LIST DECLARATION
output=[]
#FUNCTION TO FILTER VOWELS IN STRING
def f1(x):
    y=''
    if not x in 'aeiouAEIOU':
        return True
    else:
        return False

#ITERATING FUNCTION THROUGHOUT INPUT LIST
for i in state_name:
    p = list(filter(f1,i))
    #CONVERTING LIST INTO STRING
    p_str = "".join(p)
    #APPENDING STRING INTO 'output' LIST
    output.append(p_str)
#PRINTING LIST
print(output)