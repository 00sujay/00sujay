score=0
score=int(score)
name=input("Hey! Who's there?")
name=name.title()
print(f"Welcome to the quiz {name}")
print("Let's Begin :)")
print("What does CPU stand for? ")
ans1="central processing unit"
resp=input("Answer :").lower()
if resp!=ans1:
    print("Incorrect")
else:
    print(f"Good job {resp} is the right answer")
    score=score+1
print("What does GPU stand for? ")
ans2="graphics processing unit"
resp=input("Answer: ").lower()
if resp!=ans2:
    print("Incorrect")
else:
    print(f"{resp} is the correct answer")
    score=score+1
print("What does RAM stand for? ")
ans3="random access memory"
resp=input("Answer: ").lower()
if resp!=ans3:
    print("incorrect")
else:
    print("Hurray!!keep going")
    score=score+1
print("What does PSU stand for? ")
ans4="power supply unit"
resp=input("Answer :").lower()
if resp!=ans4:
    print("Incorrect")
else:
    print(f"{resp} is the right answer")
    score=score+1
print("What does ROM stand for? ")
ans5="read only memory"
resp=input("ANswer: ").lower()
if resp!=ans5:
    print("Incorrect")
else:
    print(f"{resp} is the right answer")
    score=score+1
print("Your total score is "+str(score))
print(f"Thanks for playing {name}....Bubye!!")
