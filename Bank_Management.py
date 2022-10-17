NameOfClients = ['Person_1', 'Person_2', 'Person_3', 'Person_4', 'Person_5', 'Person_6', 'Person_7']
ClientBalances = [10000, 20000, 30000, 40000, 50000, 60000, 70000]
ClientPins = ['0001', '0002', '0003', '0004', '0005', '0006', '0007']
ClientDeposition = 0
ClientWithdrawal = 0
ClientBalance = 0
disk1 = 1
disk2 = 7
u = 0
while True:
    print("***********WELCOME************")
    print("======= (a.) Open new account ======")
    print("======= (b.)  Withdraw amount =======")
    print("======= (c.)  Deposit amount =======")
    print("======= (d.) View balance of clients =========")
    print("======= (e.) Quit =========")
    print("***************************************")
    Enteroption=input("Select an option :")
    if Enteroption=="a":
        print("You have selected option a ")
        ClientID=eval(input("Enter client ID "))
        u=u+ClientID
        
        if u>7:
            print("\n")
            print("Client registration limit reached or Client registration limit too low ")
            u=u-ClientID
        else:
            while disk1<=u:
                name=input("Enter FullName :")
                NameOfClients.append(name)
                pin=str(input("Enter the Pin "))
                ClientPins.append(pin)
                ClientBlanace=0
                ClientDeposition=eval(input("Please add money to deposit to start an account "))
                ClientBalance=ClientBalance+ClientDeposition
                ClientBalances.append(ClientBalance)
                print("\nName=",end=" ")
                print(NameOfClients[disk2])
                print("Pin=",end=" ")
                print(ClientPins[disk2])
                print("Balance=","Rs",end=" ")
                print(ClientBalances[disk2],end=" ")
                disk1=disk1+1
                disk2=disk2+1
                print("\n Your account has been created successfully")
                print("Note: Please remember the Name and Pin")
        mainMenu=input("Press Enter to go back to the main menu to conduct another transaction or quit")
    elif Enteroption=="b":
        v=0
        print("You have selected option b")
        while v<1:
            w=-1
            name=input("Please enter a name ")
            pin=input("Please enter the pin ")
            while w<len(NameOfClients)-1:
                w=w+1
                if name==NameOfClients[w]:
                    if pin==ClientPins[w]:
                        v=v+1
                        ClientBalance=(ClientBalances[w])
                        print("Your current balance ","Rs",ClientBalance,end=" ")
                        ClientWithdrawal=eval(input("Enter the amount you wish to withdraw : "))
                        if ClientWithdrawal>ClientBalance:
                            deposition=eval(input("Insufficient balance! deposit a higher value than your current balance to withdraw"))
                            print("Your current balance","Rs",end=" ")
                            print(ClientBalance,end=" ")
                            ClientBalance=ClientBalance-ClientWithdrawal
                            print("\n")
                            print("Transaction successful")
                            ClientBalances[w]=ClientBalance
                            print("Your new Balance","Rs",ClientBalance,end=" ")
                            print("\n\n")
                        else:
                            ClientBalance=ClientBalance-ClientWithdrawal
                            print("\n")
                            print("Transaction successful")
                            print("Your new Balance","Rs",ClientBalance,end=" ")
                            print("\n")
            if v<1:
                print("Your name and pin does not match \n")
                break
        mainMenu=input("Press Enter to go back to the main menu to conduct another transaction or quit")
    elif Enteroption=="c":
        print("You have selected option c")
        x=0
        while x<1:
            w=-1
            name=input("Please enter a name")
            pin=input("Please enter the pin")
            while w<len(NameOfClients)-1:
                w=w+1
                if name==NameOfClients[w]:
                    if pin==ClientPins[w]:
                        x=x+1
                        print("Your current balance","Rs",end=" ")
                        print(ClientBalances[w],end=" ")
                        ClientBalance=ClientBalances[w]
                        print("\n")
                        ClientDeposition=eval(input("Enter the amount you wish to deposit : "))
                        CleintBalance=ClientBalance+ClientDeposition
                        ClientBalances[w]=ClientBalance
                        print("\n")
                        print("Amount has beed deposited successfully!")
                        print("Your new balance","Rs",end=" ")
            if x<1:
                print("Your name and pin does not match \n")
                break
        mainMenu=input("Press Enter to go back to the main menu to conduct another transaction or quit")
    elif Enteroption=="d":
        print("You have selected option d")
        w=0
        print("Client name list and balances are mentioned below")
        print("\n")
        while w<=len(NameOfClients)-1:
            print("->Customer=",NameOfClients[w])
            print("->Balance=","Rs",ClientBalances[w],end=" ")
            print("\n")
            w=w+1
        mainMenu=input("Press Enter to go back to the main menu to conduct another transaction or quit")
    elif Enteroption=="e":
        print("You have selected option e ")
        print("Thank you for banking with us :) ")
        print("\n")
        print("Have a nice day !!")
    else:
        print("Invalid option :( ")
        print("Please try again!")
        mainMenu = input("Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
    
            
        
  
        
                    
                        
                        
        
                            
                            
    
    