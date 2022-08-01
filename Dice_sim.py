import random
x="y"
while x=="y":
    num=random.randint(1,6)
    if num==1:
        print("|---------|")
        print("|         |")
        print("|    0    |")
        print("|         |")
        print("|---------|")
    if num==2:
        print("|---------|")
        print("| 0       |")
        print("|         |")
        print("|       0 |")
        print("|---------|")
    if num==3:
        print("|---------|")
        print("|         |")
        print("|  0 0 0  |")
        print("|         |")
        print("|---------|")
    if num==4:
        print("|---------|")
        print("|0       0|")
        print("|         |")
        print("|0       0|")
        print("|---------|")
    if num==5:
        print("|---------|")
        print("|0       0|")
        print("[    0    |")
        print("[0       0|")
        print("|---------|")
    if num==6:
        print("|---------|")
        print("|0   0   0|")
        print("|         |")
        print("|0   0   0|")
        print("|---------|")
    x=input("press y to roll again or n to exit :")
    print("\n")
    if x=="n":
        print("Thank you for playing!!!")

echo "# 00sujay" >> README.md
git init
git add A
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/00sujay/00sujay.git
git push -u origin main
