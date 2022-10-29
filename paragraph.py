print("hello,welcome to our game.")
name = input("hello man what is your name?:")
print(f"hello {name}")
how = input("how are you?:")
print(f"some too.")
day = input("how is your day going?:")
print(f"ok.so,Let's play a game.")
interest = input("do you have any interest?yes/no:")
if interest == "yes":
    print("ok.so,I will ask you questions and you will answer.")
else:
    print("ok.so good by & take care.")
bir = input("what is your birthday? ")

fn = input("well,what is father's name? ")
mn = input("well what is your mother's name? ")
hsb = input("do you have any sister/brother? ")
if hsb == "sister":
    print("what is her  name? ")
    sn = input("answer:")
elif hsb == "brother":
    print("what is his name")
    bn = input("answer")
elif hsb == ("no"):
    print("ok.")
else:
     print("wrong answer.")

hn = input("what is your hobby? ")

print("ok.so,Your reply time is up.Now is our time.")
print("We are written a paragraph about your self from your giving answer.")
ws = input("do you want to see it?yes/no:")
if ws == "yes":
    print(f"hello {name}.your birthday on {bir}.your hobby is {hn}.n/ your father's name is {fn} & your mother name is {mn}n/ you have a {hsb}")
    # if hsb == "brother":
    #     print(f"His name is {bn}")
    # else:
    #     print(f"Her name is {sn}")
    
    print(f'His name is {bn} ') if hsb=='brother' else print(f"Her name is {sn}")
    print("that is all,thanks & good by")
else:
     print("ok.so,good by take care")
     