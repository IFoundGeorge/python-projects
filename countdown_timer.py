import time
import os

num = input("Enter a number: ")

for i in range(int(num), 0, -1):
    os.system('cls')
    print(i)
    time.sleep(1)
    
print("Time's up!")