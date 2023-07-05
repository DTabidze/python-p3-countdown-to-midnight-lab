# your code goes here!
import time

def countdown_with_sleep(n):
    while n > 0:
        print(f'{n} SECOND(S)!')
        time.sleep(1)
        n -= 1
    print("HAPPY NEW YEAR!")

def countdown(num):
    while num > 0:
        print(f'{num} SECOND(S)!')
        num -= 1
        time.sleep(1)
    print("HAPPY NEW YEAR!")
countdown(10)
