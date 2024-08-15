#Find the length of the string 

str = "shashank"
print(len(str))

#Slice the string as per your choice 

print(str[0:5])

#Concatenate two strings

str_join = "Jogi"
print(str+ " " +str_join)

#Convert in to lower case in to uppercase character 
str_upper = str.upper()
print(str.upper())

#Convert upper case into lower case characters
print(str.lower())

#convert the character into Unicode ( Ascii values)
ch = 'c'
print(ord(ch))

#convert Unicode into character 

print(chr(99))

# Check whether the given "substring" exists in the string

substr ="anka"

if substr in str:
    print("Yes! it is present in the string")
else:
    print("No! it is not present")

# Replace the character 'k' with 'h'

print(str.replace('s','n'))

# Pad the string with "x" at the end

print(str.ljust(9, 'x'))

#Remove leading and trailing whitespace or specified characters from the string

text = "   I am cyber security student   "
trimmed_text = text.strip()
print(trimmed_text) 

#split the given string in to group of five characters 

string = "manipalInstituteofTechnology"
n = 5
out = [(string[i:i+n]) for i in range(0, len(string), n)]
print(out)

# count total number of words 

countWords = len("I am cyber security student")
print("count of words :",countWords)

#Find the frequency of each characters in the string 

string = "I am cyber security student"
res = {i: string.count(i) for i in set(string)}

print(res)

#STDIN and File operators 
# get the file name from the user 
# check the file exist or not 

import os

file_name = input("Please enter the file name: ")

if os.path.isfile(file_name):
    print(f"The file '{file_name}' exists.")
else:
    print(f"The file '{file_name}' does not exist.")


#Looping and File handling 
#read the contents from the file 
#reverse the contents from the file 
#Write into the file 


try:
    file_name = input("Enter the file name to read from: ")
    with open(file_name, 'r') as file:
        contents = file.read()
        print("Original contents of the file:")
        print(contents)
except FileNotFoundError:
    print(f"The file '{file_name}' does not exist.")
    exit()


reversed_contents = contents[::-1]


with open(file_name, 'w') as file:
    file.write(reversed_contents)
     

print(f"Reversed contents have been written back to '{file_name}'.")


#Math operations 

#Perform modular arithmetic operation 

a = 10
b = 5
m = 2
result_add = (a + b) % m
print(f"({a} + {b}) % {m} = {result_add}")


#Find the prime numbers 
#check the given number is prime or not 
    	

num = 29
flag = False

if num == 0 or num == 1:
    print(num, "is not a prime number")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break

    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")    	
        
        
#print the prime numbers with the given range 
        
def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def print_primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes


start = 10
end = 50
primes_in_range = print_primes_in_range(start, end)
print(f"Prime numbers between {start} and {end}: {primes_in_range}")

    	
#Check the given two numbers are co prime or not 

def __gcd(a, b): 
	# Everything divides 0 
	if (a == 0 or b == 0): return 0
	
	# base case 
	if (a == b): return a 
	
	# a is greater 
	if (a > b): 
		return __gcd(a - b, b) 
			
	return __gcd(a, b - a) 
def coprime(a, b): 
	if ( __gcd(a, b) == 1): 
		print("Co-Prime") 
	else: 
		print("Not Co-Prime")	 

a = 5; b = 6
coprime(a, b) 

a = 8; b = 16
coprime(a, b) 



#find the factors for the given number ( can use python library)

def find_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

number = 28
factors = find_factors(number)
print(f"Factors of {number}: {factors}")


#Generate 10 random numbers 
 
import random


random_numbers = [random.randint(1, 100) for _ in range(10)]

print("10 random numbers:", random_numbers)
 
 


