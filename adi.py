from multiprocessing.connection import answer_challenge


name = input("name?:")
birth = input("birth day?:")
time = input("time?:")
print(f"hello {name}")
print(f"your birth day is {birth}")
print(f"your birth time is {time}")
know = input("do you know about your birthday?")
if answer_challenge =="i don't know":
    print("do yu want to see it")
else:
    ("so,good by & take care")



