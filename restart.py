
# Day 1
"""
Code Challenge
  Name:
    Replacing of Characters
  Filename:
    restart.py
  Problem Statement:
    In a hardcoded string RESTART, replace all the R with $
    except the first occurrence and print it.
  Input:
    RESTART
  Output:
    RESTA$T


"""

str1 = "RESTART"  #Hardcoding str1

#    Below to find index no. of first 'R' and 
#    then replacing all further 'R' with '$'
#    finally concatanating both string before first 'R' and
#    after first 'R'(replaced with '$') and assigning it into 'str2'

str2 = str1[:str1.find("R")+1] + str1[str1.find("R")+1:].replace("R","$")

#   printing Final result
print(str2)
