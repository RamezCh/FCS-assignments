def sumDigitsRecursively(num):
  # O(log base 10 of num)
  # O(log10(num)) because we dividing by 10 each time
    if num < 1:
        return 0
    # We had this in class but not recursively I think or was it recursively as well?
    return (num % 10) + sumDigitsRecursively(num // 10)

def removeDuplicatesRecursively(string):
  #O(n) because it goes through string once
  #Only 1 character, do nothing bro
    if len(string) < 2:
      return string
    # Is first character = 2nd? Yes -> Skip
    if string[0] == string[1]:
      return removeDuplicatesRecursively(string[1:])
    # No - > Keep 1st char, and use function with its next char and repeat
    return string[0] + removeDuplicatesRecursively(string[1:])

def invertKeyValueDictionary(dictionary):
  # O(n) because it goes through it once
  newDict = {}
  for key, value in dictionary.items():
    if value in newDict.keys():
      prev_value = newDict[value]
      new_value = [prev_value, key]
      newDict[value] = new_value
    else:
      newDict[value] = key
  return newDict

def convertMatrixToDictionary(matrix):
  # O(n * m) because it is a matrix, main list and inside of it lists, so time of big list * inside lists its like a nested loop to say
  newDict = {}
  for list_index in matrix:
    key = list_index.pop(2)
    newDict[key] = list_index
  return newDict

def countHTMLTagsRecursively(html, tag):
  #O(n) just one big string
  opening_tag = "<" + tag + ">"
  closing_tag = "</" + tag + ">"
  start_index = html.find(opening_tag)
  # Nothing Found
  if start_index == -1:
    return 0
  # Closing tag after finding opening
  end_index = html.find(closing_tag, start_index)
  # Opening found -> +1 and look for others after tag is closed
  return 1 + countHTMLTagsRecursively(html[end_index + len(closing_tag):], tag)
  
def countNormalizedColumnsRecursively(matrix, column_index = 0):
  # O(n * m) because it is a matrix
  if column_index >= len(matrix[0]):
    return 0 # O(1)

  column = [row[column_index] for row in matrix]
  mean = sum(column)  / len(column) # O(n)
  squared_diff = [(x - mean) ** 2 for x in column]
  mean_squared_diff = sum(squared_diff) / len(column)
  standard_deviation = mean_squared_diff ** 0.5 # O(1)

  if mean < 1 and (standard_deviation > 0.5 and standard_deviation < 2):
      return 1 + countNormalizedColumnsRecursively(matrix, column_index + 1)

  return countNormalizedColumnsRecursively(matrix, column_index + 1)
    
def menu_of_choices():
  print("Choose one of the following: \n1.Sum of digits recursively \n2.Remove duplicates recursively \n3.Invert dictionary \n4.Convert matrix to dictionary \n5.Count HTML tags recursively \n6.Count normalized columns \n7.Exit") # O(1)
  
  user_choice = int(input("Enter your choice's number: ")) # O(1)
  
  if user_choice == 1:
    i = int(input("Enter a number: ")) # O(1)
    print(sumDigitsRecursively(i)) # O(log10(num))
    
  if user_choice == 2:
    s = input("Enter a string: ") # O(1)
    print(removeDuplicatesRecursively(s)) # O(n)
    
  if user_choice == 3:
    dict = {} # O(1)
    size_dict = input("Enter size of dict: ") # O(1)
    for i in range(int(size_dict)): # O(n)
      key = input("Enter unique key: ") # O(1)
      value = input("Enter value: ") # O(1)
      dict[key] = value # O(1)
    
    print(invertKeyValueDictionary(dict)) # O(n)
    
  if user_choice == 4:
    row_count = int(input("Enter the number of rows:")) # O(1)
    matrix = [] # O(1)
    for i in range(row_count):          # O(i)
      row_content = input("Enter row content: ")
      row_list = row_content.strip('[]').split(', ') # O (n + m)  n is the length of the string, m is the number of elements in the resulting list
      matrix.append(row_list)
    print(convertMatrixToDictionary(matrix))
    
  if user_choice == 5:
    html = "<html><head><title>My Website</title></head><body><h1>Welcome to my website!</h1><p>Here you'll find information about me and my hobbies.</p><h2>Hobbies</h2><ul><li>Playing guitar</li><li>Reading books</li><li>Traveling</li><li>Writing cool h1 tags</li></ul></body></html>"  # O(1)
    tag = input("Enter a tag: ")  # O(1)
    print(countHTMLTagsRecursively(html, tag))
    
  if user_choice == 6:
    Matrix = [[-1.2649110640673518, 5.123451, 43],[-0.6324555320336759, 5.13123123, 4334],[0.0, 6.1543453, 125879],[0.6324555320336759, 0.1231235709, 123544],[1.2649110640673518, 9.1543524234, 55676]]  # O(1)
    print(countNormalizedColumnsRecursively(Matrix))
    
  if user_choice == 7:
    print("Exiting...") # O(1)
    return -1 # O(1)
  if user_choice > 7 or user_choice < 1:
    print("Invalid choice") # O(1)
  menu_of_choices() # Time complexity depends on the choice of the user

def main():
    user_name = input("What is your name? ") # O(1)
    print("Welcome",user_name) # O(1)
    menu_of_choices() # Time complexity depends on the choice of the user
    print("Code terminated. Goodbye!") # O(1)
  
main()