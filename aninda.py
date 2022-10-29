print("welcome to my computer quiz!")

playing = input("do you want to play? ")

if playing != "yes":
    quit()

print("okay! let's play :)")
score = 0

answer = input("what does cpu stand for? ")
if answer == "central processing unit":
    print("correcy")
    score += 1
else:
    print("incorrect")

answer = input("whice software would be good for coding? ")
if answer == "python":
    print("correcy")
    score += 1
else:
    print("incorrect")

answer = input("Who are you? ")
if answer == "man":
    print("correcy")
    score += 1
else:
    print("incorrect")

print("you got " + str(score) + " questions correct")
print("you got " + str((score / 4) * 100) + "%.")

