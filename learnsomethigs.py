print("quit  - want to quit")
print("start - car will start")
print("stop  - car will stop")

what_want = input("what are you want?: ")
if what_want == "quit":
    print("Thanks")

elif what_want == "start":
    print("car is started")

elif what_want == "stop":
    print("car is stoped")

else:
    print(" 'OUT OF RANGE' Please try again.Thanks. ")