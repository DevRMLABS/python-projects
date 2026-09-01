# This program asks for, Age, push ups, sit ups, run, and timed ruck distance.
print("Hi what is your name?")
your_name = input(">")
print("Hi, " + your_name)
print("The length of your name is:")
print(len(your_name))
print("if you could guess what is the max amount of push-ups you can do without warming up?")
push_ups = int(input("How many reps can you do without warming up?"))
print("if you could guess how many sit ups do you think you can do in a minute?")
sit_ups = int(input("How many reps can you do in a minute?"))
print("If you can guess your improved 2 mile run time what would it be?")
run_time = float(input(" how fast would you say your improved 2 mile time is?"))
print("finally, what is your 4 mile ruck time?")
ruck_time = float(input("how fast can you complete a 4 mile timed ruck?"))
run_pace = run_time  / 2
ruck_pace = ruck_time / 4
print(run_pace)
print(ruck_pace)
