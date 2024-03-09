# Question 1
def printMountainPattern(peak):
  for i in range(peak):
    print("*"*i)
  for i in range(peak, -1, -1):
    print("*"*i)

range_max = int(input("Enter the maximum range: "))
printMountainPattern(range_max)

# Question 2
def findEvenNumbersFromXtoY(x, y):
  even_numbers = []
  for i in range(x, y+1):
    if i % 2 == 0:
      even_numbers.append(i)
  print("The even numbers between", x, "and", y, "are", even_numbers)

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
while(y<x):
  print("The second number should be greater than the first number")
  y = int(input("Enter the second number: "))
findEvenNumbersFromXtoY(x, y)

# Question 3
def reverseString(s):
  reversed_word = ""
  for i in s:
    reversed_word = i + reversed_word
  return reversed_word
word = input("Enter a word: ")
print("Input: \""+word+"\" Output: \""+reverseString(word)+"\"")

# Question 4
def returnEvenList(list):
  even_list = []
  for i in list:
    if i % 2 == 0:
      even_list.append(i)
  return even_list
list = []
user_input = input("Enter a number to the list, press X when done: ")
while user_input.upper() != "X":
  try:
    list.append(int(user_input))
  except ValueError:
    print("Invalid input, X or integer please.")
  user_input = input("Enter a number to the list, press X when done: ")

print("Input:", list, "Output:", returnEvenList(list))

# Question 5
def isValidIPv4Address(s):
  octets = s.split(".")
  if len(octets) != 4:
    return False
  for octet in octets:
    if not octet.isdigit():
      return False
    if int(octet) < 0 or int(octet) > 255:
      return False
    for index in range(len(octet)):
      if octet[index] == "0" and index != (len(octet)-1):
        return False
  return True
  
ip_address = input("Enter an IPv4 address: ")
if isValidIPv4Address(ip_address):
  print(ip_address, "is a valid IPv4 address")
else:
  print(ip_address, "is a invalid IPv4 address")