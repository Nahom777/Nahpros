import time
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("Welcome to Nahom's quiz!")
time.sleep(1)
print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
playing = input("Do you wanna play? ")
print("")
if playing.lower() != "yes":
    quit()

time.sleep(1)

print("Okay! Let's play ;)")
print("")
score = 0

time.sleep(1)

answer = input("1. When did the second world war happen? ")

if answer.lower() == "1945":
    time.sleep(2)
    print("Nice!")
    score += 1
else:
    print("Not quite!")

print("")

time.sleep(1)

answer = input("2. What is the capital City of Ethiopia? ")
time.sleep(2)
if answer.lower() == "addis ababa":
    time.sleep(1)
    print("You are correct!")
    score += 1
else:
    print("You are not correct!")  

print("")

time.sleep(1)

answer = input("3. What is the 1+1? ")
time.sleep(2)
if answer.lower() == "2":
    print("You are correct!")
    score += 1
else:
    print("You are not correct!") 
    time.sleep(1)

print("")
time.sleep(1)
print("You got" +" "+str(score)+" "+ "Questions correct!")