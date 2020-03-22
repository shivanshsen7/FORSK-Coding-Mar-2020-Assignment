"""
# Shopping List App 
    We are going to make a "Shopping List" app. 
    Run the script to start using it.
    Put new things into the list one at a time
    Enter the word DONE - in all CAPS - to QUIT the program
    And once i quit, I want the app to show me everything thats on my list.

Hint 1
    Step 1: Make a list to hold onto our items.
    Step 2: Print out instructions on how to use the app

    Step 3: Ask for new items
    Step 4: Add new items to our list
    Step 5: Be able to quit the app with DONE

    Step 6: print out the list
"""
global pp
pp=0
print('Welcome to "Shopping List"')

"""
CMDs:
Start by typing names you want to add to your list
to terminate app at any point type   DONE
to view current items in list type   $v
to start append new items in list type   $a
to terminate app without viewing final list type   $exit
to remove a item from list type   $rmv,<index no.>
"""
doc='''
The Script Comprises of 2 modes
Editor mode('>>>') & CMD mode('<<<')

editor mode type infinitely
cmd mod perform oprations
to switch in b/w modes type '$$'
commands in CMD mode:
    view
    del
    count
    doc
'''

print('{:<40s}{:<20s}'.format('Start by typing names you want to add to your list\n\n',' '))
keylogger = list()

def f1(x):
    if x =='$$':
        return False
    if x =='DONE':
        return False
    else:
        return True


def shop_ls():
    global shop_list
    shop_list = list(filter(f1,keylogger))
    pass

def show():
    shop_ls()
    print('{:^60s}{:<20s}'.format('\n--------------Shopping List--------------',' '))
    for x,y in enumerate(shop_list):
        print(x,y)
    else:
        None

def edit():
    e_in = input('>>>')
    keylogger.append(e_in)
    if keylogger[-1] =="$$":
        return cmd()
    elif keylogger[-1] =="DONE":
        show()
        return None
    else:
        return edit()

def cmd():
    show()
    c_in = input('<<<')
    if c_in == '$$':
        return edit()
    elif c_in == 'view':
        return cmd()
    elif c_in == 'del':
        at_del = int(input('<<< delete at :'))
        del keylogger[at_del]
        return cmd()
    elif c_in == 'count':
        print('\nThe no. of elements in Shopping List is {}'.format(len(shop_list)))
    elif c_in == 'doc':
        print(doc)
    elif c_in == "DONE":
        import sys
        sys.exit()
    else:
        print('Please enter a Valid command')

edit()
while(keylogger[-1]=='$$'):
    cmd()
