try:
    i = int(input("Enter a number:"))
    c = 1/1
except Exception as e:
    print(e)
else:
    print("these is the exception with else and We are Succesful ion it")
    exit()

finally:
    print("we are dont ")  # print the erorr that you had on your application


print("thanks for using the shareits")
