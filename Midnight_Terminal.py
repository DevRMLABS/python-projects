print("One windy summers night in a bright metropolis city in your room a mysterious laptop appears it could hold the answers will you solve it?")
choice = input("Will you power the laptop on or keep it off?")

if choice == "turn on":
    print("The laptop displays a power on symbol(POWER ON....)")
elif choice == "turn off":
    print("Nothing happens and you continue off on your LoFi night")
    exit()
print("The computer seems as if it has a conciousness, it asks for your name")
name = input("Enter your name")
print("The computer eagerly welcomes you, " , name)

print("This laptop explains it has been passed from user to user since the beginning of time, it has but 3 files each with ungodly power.")
print("Pick your poison")

print("you have three files to pick from, each one is color coded.")

choice = input("Will you continue using the computer?").lower()
if choice == "Yes":
    
    print("You the files tab visibly displaying three of the files previously mentioned, Green, Red, or Black.")
elif choice == "No":
    
    print("You decide not to test your luck, closing the computer and proceeding with a swift escape into the darkness")
    exit()
choice = input(" Will you open the Red, Green, or Black one first?")
if choice == "Yes":
    print("The three files appear")
    
elif choice == "No":
    print("you close the computer")
    exit()
    
choice = input("Red, Green, or Black?").lower()

if choice == "Red":
    print("The file begins to open...")
    
elif choice == "Green":
    print("The file begins to open...")
    
elif choice == "Black":
    print("The file begins to open...")



