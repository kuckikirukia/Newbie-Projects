#  // Password Generator //

import random
import string

generator = input('Do you want to create a password? Enter: Yes or No ')
num = int(input('What length do you want the password? '))
diff = int(input('What difficulty do you want the password? \n[1] Easy\n[2] Moderate\n[3] Strong\n'))

password = ''

if diff == 1:
    for char in range(1, num+1):
        password += random.choice(string.ascii_lowercase)

elif diff == 2:
    for char in range(1, num + 1):
        password += random.choice(string.ascii_letters)

elif diff == 3:
    for char in range(1, num+1):
        password += random.choice(string.printable)

print('Your new password is ' + "' " + str(password) + " '")

