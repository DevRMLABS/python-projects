# A curious adventurer enters a dragon's cave in search of fortune. What awaits them?
def introduce_player():
    print("you are a young adventurer searching for fortune beyond your wildest dreams")
    print("Young and naive you enter a cave unaware a dragon calls it home what befalls of you!")
    
    introduce_player()
    
choice = input("Do you risk your life entering the cave further or be rational and leave?").lower()
if choice == "enter_cave":
        print("you sigh and walk further into the cave system")
elif choice == "leave_cave":
        print("you leave, asking your self if it was truly worth it to risk everything!")
else:
    print("this is not a valid choice")    
print("/nYou enter the cave and discover two paths. 1 is left, 2 is right.")
if choice == "left_pathway":
  print("1. Left pathway")
  print("2. Right pathway")
next_choice = input("Which path will you take?").lower()
if next_choice == "left" or next_choice == "1":
    print("you walk into the left pathway. You enter a dusty common area, discovering relic equipment from the fallen empire in a chest!")
elif next_choice == "right_pathway" or next_choice == "2":
    print("You walk into the right pathway. Walking into the throne room. There sit's the bones of the former king Kefrey The Great, you take his dragon bone greatsword")
    
