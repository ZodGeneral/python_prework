# Question 1
# Write a function to print "hello_USERNAME!" 
# USERNAME is the input of the function. 

def hello_name():
    #prints uppercase version of user input

    user_name = input()
    print(f"hello_{user_name.upper()}!")
    return

hello_name()

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    #prints all odd numbers between 1 and 100

    n = 1
    while n <= 100:
        if n % 2 == 1:
            print(n, end=' ')
        n += 1

first_odds()

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below.

def max_num_in_list():

    #User input for size of list and then elements of list
    #Prints maximum number from list as output

    a_list = []
    n = int(input('\nSize of list: '))
    for i in range(0, n):
        element = int(input())
        a_list.append(element)
    
    ordered_list = sorted(a_list)
    print('Max number in list is: ',ordered_list[-1])


max_num_in_list()

# Question 4
# Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).

def is_leap_year(a_year):

    #The year has to be divisible by 4 evenly and not divisible by 100 unless divisible by 400
    
    return a_year % 4 == 0 and (a_year % 100 != 0 or a_year % 400 == 0)

a_year = int(input('Pick a year to discover if it is a leap year: '))
print(is_leap_year(a_year))

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.

def is_consecutive(b_list):

    #Compares the list sorted from least to greatest to a range of the list
    #These will only be equal if they are consecutive numbers in the list

    return sorted(b_list) == list(range(min(b_list), max(b_list)+1))

# input for a list
b_list = []
n = int(input("Enter list size: "))
for i in range(0, n):
    x = int(input())
    b_list.append(x)

print(is_consecutive(b_list))