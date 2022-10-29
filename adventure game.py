name = input("type your name: ")
print("welcome", name, "to this adventure")
score = 0

print("you have same adventure in this game")

adventure1 = input("if you are near a river.now you have to cross the river then how can you cross the river at swim or build a raft? ")

if adventure1 == "swim":
    print("you can not do it.becouse the river is very deep")
    score -= 1

elif adventure1 =="build a raft":
    print("correct")
    score += 1

adventure2 = input("if you do not have any water.but you have a river so,what do you need to do?drink a river water/nothing: ")
if adventure2 == "nothing":
    print("your dead is coming soon")
    score -= 1

elif adventure2 == "drink a river water":
    print("so,your dead is coming soon.becouse, it is very danger for you")
    score -= 1

adventure3 = input("now,what do you need to do?die/stay: ")
if adventure3 =="stay":
    print("it is not possible.becouse,your dead is coming soon. ")
    score -= 1

elif adventure3 =="die":
    print("so,congratulations for your happy death day.")
    score -= 1

print("you got " + str(score) + " questions correct")
print("you got " + str((score / 4) * 100) + "%.")