def incriment(num):
    try:
        return int(num)+1
    except:
        raise ValueError("These is value Error")


a = incriment("2324d")
print(a)
