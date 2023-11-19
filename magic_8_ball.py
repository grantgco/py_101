# November 19, 2023

import random
import sys

name = ""
question = ""
answer = ""

random_number = random.randint(1,9)

#print(random_number)

if question == "": # Error to exit the script if the world is going to explode because there is no question being asked.
  print("OMG.  The fabric of the world is in jepoardy.  There is no question!")
  sys.exit()

# Otherwise, continue...

if random_number == 1:
  answer ="Yes - definitely"
elif random_number == 2:
  answer ="It is decidely so"
elif random_number == 3:
  answer ="Without a doubt"
elif random_number == 4:
  answer ="Reply hazy, try again"
elif random_number == 5:
  answer ="Ask again later"
elif random_number == 6:
  answer ="Better not tell you now"
elif random_number == 7:
  answer ="My sources say no"
elif random_number == 8:
  answer ="Outlook not so good"
elif random_number == 9:
  answer ="Very doubtful"
else:
  answer = "Error"

if name == "": # Prints if there is no name
  print("Question: " + question)
else:
  print(name + " asks: " + question)

print("Magic 8-Ball's Answer: " + answer)
