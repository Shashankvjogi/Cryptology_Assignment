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



