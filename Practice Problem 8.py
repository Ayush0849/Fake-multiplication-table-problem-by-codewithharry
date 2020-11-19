import random


def istrue(num, tablelis):
    new_list = []
    for i in range(1, 11):
        new_list.append(num*i)
    if new_list == tablelis:
        print("The results are completely right")
    else:
        print("Be Alert! results are wrong")
    inpu = input(
        "Do you want to check Rohan's list with my list\nEnter \"y\" for yes\nEnter \"n\" for no: ")
    if inpu == "y":
        print(new_list)
        print("(:=======================Thanks for using this program!=============================:)")
    elif inpu == "n":
        print("(:=======================Thanks for using this program!=============================:)")
        quit()
    else:
        print("Input invalid")


def rohandasfraud(number):
    tablelis = []
    for i in range(1, 11):
        tablelis.append(number*i)
    # here we are using random to choose a indexing value
    table = random.randint(7, 8)
    # here we will use random to choose the value to be enter between the list
    tablelis[table] = random.randint(30, 35)
    print(tablelis)
    # print(tablelis)
    inputt = input(
        "Do you want to check wheather this list is right?\nEnter \"y\" for yes\nEnter \"n\" for no: ")
    if inputt == "y":
        istrue(inpu, tablelis)
    elif inputt == "n":
        print("(:=======================Thanks for using this program!=============================:)")
        exit()
    else:
        print("Input invalid!")


if __name__ == "__main__":
    try:
        print("<----------------------------------Welcome to my program--------------------------------->")
        inpu = int(input("Enter the number to know the table\n--> "))
        rohandasfraud(inpu)
    except Exception as e:
        print("Please enter a valid input! -_- ")
