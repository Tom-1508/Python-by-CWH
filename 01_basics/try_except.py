try:
    a = int(input("Enter the number: "))
    print(a+3)
except Exception as e:
    print("Some error occured",e)