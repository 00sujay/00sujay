def inchtocms(inch):
    print(f"The equivalent for {inch}in is ",inch*2.54,"cms")
def miletokm(miles):
    print(f"The equivalent for {miles}miles is ",miles*1.60935,"km")
def fahtocel(fah):
    print(f"The equivalent for {fahr}°F is ",((fahr-32)*5)/9,"°C")
def mphtokph(mph):
    print(f"The equivalent for {mph}mph is ",mph*1.609344,"kph")
def kgstolbs(kgs):
    print(f"The equivalent for {kgs}kg is ",kgs*2.2046226218,"lbs")
def sqfttoacres(sqft):
    print(f"The equivalent of {sqft}sqft is ",sqft*0.0000229568,"acres")
while True:
    print("***********UNIT CONVERTER************")
    print("======= (a.) Inches to Centimeters ======")
    print("======= (b.) Miles to Kilometers =======")
    print("======= (c.) Fahrenheit to Celsius =======")
    print("======= (d.) Mph to Kph =========")
    print("======= (e.) Kilograms to Pounds =========")
    print("======= (f.) Square feet to acres =========")
    print("======= (q.) Exit =========")
    print("***************************************")
    user_input=input("Select an option ")
    if user_input=="a":
        inch=float(input("Enter in inches :"))
        inchtocms(inch)
        main=input("Press enter to use another conversion or quit")
    if user_input=="b":
        miles=float(input("Enter in miles :"))
        miletokm(miles)
        main=input("Press enter to use another conversion or quit")
    if user_input=="c":
        fahr=float(input("Enter in Fahrenheit :"))
        fahtocel(fahr)
        main=input("Press enter to use another conversion or quit")
    if user_input=="d":
        mph=float(input("Enter in miles per hour :"))
        mphtokph(mph)
        main=input("Press enter to use another conversion or quit")
    if user_input=="e":
        kgs=float(input("Enter in kilograms :"))
        kgstolbs(kgs)
        main=input("Press enter to use another conversion or quit")
    if user_input=="f":
        sqft=float(input("Enter in square feet :"))
        sqfttoacres(sqft)
        main=input("Press enter to use another conversion or quit")
    if user_input=="q":
        break