import string
import random

password = []

for i in range(12):

    random_char = random.choice(string.ascii_letters)
    password.append(random_char)

print("Generated password: "+ "".join(password))