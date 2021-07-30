yourage=int(input("Enter your year of  date of birth in which you have born:\n"))
isyear=False
isage=False

if len (str(yourage))==4:
    isyear=True

else:
    isage=True

if yourage<1900 and isyear:
     print("you are one oldest person of all time ")
     exit()

if yourage>2021:
    print("you are not born at now ")
    exit()

if isage:
    isyear=2000-isyear
print(f"you will be 100 years old at : {yourage + 100}")

interestedage=int(input("Enter the interested age in which your age is in \n"))
print(f"YOu will be {interestedage-yourage} years old in {interestedage}")


