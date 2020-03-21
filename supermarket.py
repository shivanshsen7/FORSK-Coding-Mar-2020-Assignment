# Day 6
"""
Name: 
    Supermarket      
Filename:
    supermarket.py 
Problem Statement:
    You are the manager of a supermarket. 
    You have a list of items together with their prices that consumers bought on a particular day. 
    Your task is to print each item_name and net_price in order of its first occurrence. 
    Take Input from User 
Data:
    Not required
Extension:
    Not Available   
Hint: 
    item_name = Name of the item. 
    net_price = Quantity of the item sold multiplied by the price of each item.
    try to use new class for dictionary : OrderedDict 
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    
    
    BANANA FRIES 12
    POTATO CHIPS 30
    APPLE JUICE 10
    CANDY 5
    APPLE JUICE 10
    CANDY 5
    CANDY 5
    CANDY 5
    POTATO CHIPS 30

Sample Output:
    BANANA FRIES 12
    POTATO CHIPS 60
    APPLE JUICE 20
    CANDY 20
"""
#Asking for User to provide Input & 
#at the of every line price of item must be present

print('OrderedDict is not necessary as in from py3.7 it is included in dict()')
print('Read-more at:\n')
print(r'http://www.blog.pythonlibrary.org/2018/02/27/python-3-7-dictionaries-now-ordered/')
#line 47 to 50 only work if copy-paste in an IDE
#if using cmd-line or to type line by-line go line 54 to 59 by selecting & pressing CTRL + 1
sip = input('Enter a List with price after space after item name:')
#splitting multi-line input to list
sip_raw_ls = sip.split('\n')

# =============================================================================
# sip_raw_ls = list()
# while True:
#     a = input()
#     if a =='':
#         break
#     sip_raw_ls.append(a)

#if using cmd-line or to type line by-line go line 54 to 59 by selecting & pressing CTRL + 1
# =============================================================================


#splitting every element of list ,i.e., evreyline based on space.
for x in range(len(sip_raw_ls)):
    sip_raw_ls[x] = sip_raw_ls[x].split()


#The List to contain Standarized input
sip_std=list()
#every element of list contains two parts, one with item name(_Before last Space_)
#other one with price of item(_The price is still depticted as String not integer_)
for y in sip_raw_ls:
    sip_std.append([y[:-1],y[-1]])

#lists below contain only item_name & item_price_per_unit respectively
item_sip = list()
item_cores_price = list()

for y in range(len(sip_std)):
    #converting list to string for item_names with space contained within
    sip_std[y][0] = " ".join(sip_std[y][0])
    #appending item_name & thier price in diff. list respectively
    item_sip.append(sip_std[y][0])
    item_cores_price.append(sip_std[y][1])
    
#----- Input -----
print('-'*5,'Input','-'*5)
for x in range(len(item_sip)):
    #showing input in more formatted way & 
    #showing list to start from 0(Just to show, not true), better view for non-CS person
    print(x+1,'-->',item_sip[x],":",item_cores_price[x])
#creating a dictionary to set item as key & its unit price as value
item_set = dict(zip(item_sip,item_cores_price))
#uncomment the below to see Dictionary
#print(item_set)

#output as in dictionary, with
#item_name as Key &
#total price of product(unit_price * no. of sales)  as Value
item_set_output=dict()
#printing the Output as Desired in Sample Output
print()
#----- Output -----
print('-'*5,'Output','-'*5)
for x,y in item_set.items():
    #print(x,'$',y)
    print(x,int(y)*(item_sip.count(x)))
    item_set_output[x]=int(y)*(item_sip.count(x))

