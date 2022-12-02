import time
from GameData14 import data
import os
import random

logo = """             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""


# shuffle the info in database
random.shuffle(data)

# function to compare the instagram followers of two people
def compare(a,b):
    if a['follower_count'] > b['follower_count']:
        return 'A'
    elif a['follower_count'] < b['follower_count'] :
        return 'B'
    else:
        return 'A' or 'B'

def print_stats(acct):
    return f"{acct['name']}, {acct['description']}, from {acct['country']}"


# initialize player's score
score = 0
print(logo)
# game loop
while True:
    # iterate over the list, when final element reached, shuffle list and start over.
    # this could be done with two random numbers picked from the list, but this is the method I picked.
    for i in range(len(data)-1):
        if i == len(data)-1:
            i = 0
            random.shuffle(data)

        print(f"Compare A: {print_stats(data[i])}")
        time.sleep(0.2)
        print(vs)
        time.sleep(0.2)
        print(f"Against B: {print_stats(data[i+1])}")

 # Check:       print(compare(data[i], data[i+1]))

        # make sure user enters either A or B
        while True:
            uzer = input("Who do you think has more Instagram followers? Type A or B: ")
            if uzer == 'A' or uzer == 'B':
                break

        # compare user's answer to real answer
        check = compare(data[i], data[i+1])

        # if user's wrong, exit and print their score
        if uzer != check:
            break
        else:
            score += 1
            os.system('clear')
            print("Yess!!! Your score now is: ",score)

    break       # exit while loops and therefore exit game

# print results
print(f"You lost!!! {data[i]['name']} has {data[i]['follower_count']},\
      {data[i+1]['name']} has {data[i+1]['follower_count']}. Your score is {score}.")


