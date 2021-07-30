import time
while (True):
    print("Press q to quit")
    a = input("Enter the number:")
    if a == 'q':
        break
    try:
        print("Trying...")
        time.sleep(2)
        a = int(a)
        if a > 6:
            print("You have Entered grater than 6 ")
        else:
            print("You have Entered less than 6")
    except Exception as e:
        # e menas the error is intered
        print(F"Your intput is resulted in error.{e}")


print("Thanks for usering me")
# non stop running programm
