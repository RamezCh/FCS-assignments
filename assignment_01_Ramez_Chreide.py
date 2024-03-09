"""Question 1"""
contain_dot_after_at =  False
contain_character_between_dot_at = True
start_end_dot = False
start_end_at = False
is_single_at = True
is_valid_email = False
error_count = 1
input = "Fred@SE.com"
email = input.strip().lower()
index_at = 0
print("The email is",email)

"""
invalid email formats:

"example.test.com" (missing "@")
"@example.com" (starts with "@")
"example@test@com" (multiple "@")
"example@.com" (dot directly after "@")
"example@test.com." (ends with ".")
".example@test.com" (starts with ".")

Note: No loops
"""

""" The email should not start or end with "@" or ".". """
if email[0] == "." or email[-1] == ".":
  start_end_dot = True
  error_count += 1
  
if email[0] == "@" or email[-1] == "@":
  start_end_at = True
  error_count += 1

""" It contains one "@" symbol. """
if email.count("@") > 1 or email.count("@") == 0:
  is_single_at = False
  error_count += 1
else: 
  index_at = email.index("@")

""" Check for Dot and it's conditions """
if email.count(".") > 0:
  
  if email[index_at + 1] == "." or email[index_at - 1] == ".":
    contain_character_between_dot_at = False
    error_count += 1

  if email.index(".", index_at):
    contain_dot_after_at = True
    error_count -= 1

""" Check if we passed all tests or not """
if error_count == 0:
  is_valid_email = True

if is_valid_email:
  print("The email is valid")
else:
  print("The email is invalid")

"""Question 2"""

""" Time before 6 PM """
is_day_time = True
""" Older than 18 """
is_adult = True
has_vip_pass = True
has_ticket = True

if is_day_time and has_ticket:
  print("Welcome to the event. You may enter.")

if is_day_time and (has_ticket or has_vip_pass):
  print("Welcome to the event. You may enter.")

if not is_day_time and is_adult and has_vip_pass:
  print("Sorry bro, code is denying you your rights to enter.")

if is_adult and (has_ticket or has_vip_pass) and not is_day_time:
  print("You may not enter this village.")

if (is_day_time and has_ticket) or (not is_day_time and is_adult and
has_vip_pass):
  print("Welcome to the event. You may enter by the power of OR.")

if (not is_day_time and has_vip_pass) or (is_day_time and not has_ticket):
  print("Stop right there, you can't enter.")

if (is_adult and not is_day_time) and (has_vip_pass or not has_ticket):
  print("You may not enter.")

if not (is_adult and has_ticket) and (is_day_time or has_vip_pass):
  print("You may not enter.")

if (is_day_time and has_ticket) or (not is_day_time and (is_adult or
has_vip_pass)):
  print("Welcome to the event. You may enter by the power of OR.")

if ((not is_adult or not has_ticket) and is_day_time) or (is_adult and not
is_day_time and not has_vip_pass):
  print("You are out.")

if is_adult and ((is_day_time and not has_vip_pass) or (not is_day_time and
has_vip_pass)):
  print("You may not enter.")

if (is_adult or has_ticket) and not (is_day_time and not has_vip_pass):
  print("Come everyday")

if not (is_adult and (has_vip_pass or is_day_time)) or (has_ticket and not
is_day_time):
  print("Oh no! You can't enter :(")

if (has_ticket or has_vip_pass) and not (is_adult and is_day_time):
  print("Pew pew pew, stay out!")

if not ((not is_adult and has_ticket) or (is_day_time and not has_vip_pass)):
  print("Come in bro, don't feel shy")