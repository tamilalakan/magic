# Stage_one
def first_stage(cards):
  First_stage,First_stage1 = [],[]
  time.sleep(4)
  print()
  for i in range(len(cards)):
    if i%2 != 0:
      print(cards[i])
      First_stage.append(cards[i])
    else:
      First_stage1.append(cards[i])
  time.sleep(2)
  print("\nIf your card is present here...Just tell 'yes' or 'no'\n")
  First_card = input()

  if First_card == "yes" or First_card == "y":
    First_ = First_stage + First_stage1
  else:
    First_ = First_stage1 + First_stage
  return second_stage(First_)

# Stage_Two

def second_stage(First_):
  Second_stage,Second_stage1 = [],[]
  print()
  for i in range(len(First_)):
    if i%2 != 0:
      print(First_[i])
      Second_stage.append(First_[i])
    else:
      Second_stage1.append(First_[i])
  time.sleep(2)
  print("\nIf your card is present here...Just tell me 'yes' or 'no'\n")
  Second_card = input()

  if Second_card == "yes" or Second_card == "y":
    Second = Second_stage1 + Second_stage
  else:
    Second = Second_stage + Second_stage1
  return third_stage(Second)

# Stage_Three
def third_stage(Second):
  Third_stage,Third_stage1 = [],[]
  print()
  for i in range(len(Second)):
    if i%2 != 0:
      print(Second[i])
      Third_stage.append(Second[i])
    else:
      Third_stage1.append(Second[i])
  time.sleep(2)
  print("\nIf your card is present here...Just tell me 'yes' or 'no'\n")
  Third_card = input()

  if Third_card == "yes" or Third_card == "y":
    Third = Third_stage + Third_stage1
  else:
    Third = Third_stage1 + Third_stage

  return final(Third)

# Stage_Final
def final(Third):
  # print name
  print()
  time.sleep(3)
  name_of_card = Third[1]
  if name_of_card[0] == "K":
    print("Your Face_card Name:",end=' ')
    time.sleep(4)
    print('King\n')
  else:
    print("Your Face_card Name:",end=' ')
    time.sleep(4)
    print('Queen\n')
  time.sleep(3)
  # print color
  color = Third[4]
  if color[0] == "S" or color[0] == "C":
    print("Your Face_card color:",end=" ")
    time.sleep(4)
    print("Black\n")
  else:
    print("Your Face_card color:",end=' ') 
    time.sleep(4)
    print("Red\n")
  time.sleep(3)
  # print symbol
  symbol = Third[6]
  if symbol[0] == "S":
    print("Your Face_card Symbol:",end=" ")
    time.sleep(4) 
    print("Spade\n")
  elif symbol[0] == "C":
    print("Your Face_card Symbol:",end=" ")
    time.sleep(4)
    print("Club\n")
  elif symbol[0] == "H":
    print("Your Face_card Symbol:",end=" ")
    time.sleep(4)
    print("Heart\n")
  elif symbol[0] == "D":
    print("Your Face_card Symbol:",end=" ")
    time.sleep(4) 
    print("Diamond\n")
  # print card
  time.sleep(4)
  print("And Finally your Face_card is:",end=" ")
  time.sleep(4)
  print(Third[2])
  return 


def main():
  cards = ["King  - Club","King  - Heart","King  - Spade","King  - Diamond","Queen - Club","Queen - Heart","Queen - Spade","Queen - Diamond"]
  print("Welcome to my magic program\n")
  time.sleep(4)
  print("Can you please tell me your name..\n")
  time.sleep(2)
  user_name = input()
  print("\nHello "+user_name+"... its a Sweet and taste name \n")
  time.sleep(4)
  print("Now we start the magic.\n")
  time.sleep(3)
  print("From this think any one card\n")
  time.sleep(2)
  print("King - Heart  \t Queen - Heart \nKing - Diamond \t Queen - Diamond  \nKing - Spade  \t Queen - Spade  \nKing - Club  \t Queen - Club\n")

  time.sleep(8)
  print("If you choose a card....just press enter")
  n = input()
  if n == "":
    return first_stage(cards)


import time
main()
