def main():
    pro1()
    pro2()
    pro3()
    pro4()
    pro5()
# Problem 1:
# Create a function with the variable below. After you create the variable do the instructions below that.
# arrayForProblem2 = ["Kenn", "Kevin", "Erin", "Meka"]
# a) Print the 3rd element of the numberList.
# b) Print the size of the array
# c) Delete the second element.
# d) Print the 3rd element.
def pro1():
    def ghost():
        arrayFor = ["Kenn", "Kevin", "Erin", "Meka"]
        print(arrayFor[2])
        print(len(arrayFor))
        arrayFor.pop(1)
        print(arrayFor[2])
    ghost()

# Problem 2:
# We will keep having this problem until EVERYONE gets it right without help
# Create a function that has a loop that quits with ‘q’. If the user doesn't enter 'q', ask them to input another string.
def pro2():
    user=""
    while user !="q":
        user = input("Enter somthing\n")

def pro3():
    def collect():
        name = ["Jonathan","Michael", "William","Robert"]
        nnames= ["John", "Mike", "Bill", "Rob"]
        f = range (0,4)
        for x in f:
            print(f"{name[x]}/{nnames[x]}")
        print(nnames[2])
    collect()
# Problem 4:
# Create an array of 5 numbers. Using a loop, print the elements in the array reverse order. Do not use a function
def pro4():
    array = [1,2,3,4,5]
    f = range(int(len(array))-1,-1,-1)
    for x in f:
        print(array[x])

# Problem 5:
# Create a function that will have a hard coded array then ask the user for a number. Use the userInput to state how many numbers in an array are higher, lower, or equal to it.
def pro5():
    def fin():
        high = 0
        low = 0
        equal = 0
        user = int(input("Enter a number\n"))
        array = [12,3256,13,42321,32,235,346,43,421,4,543,32,13,5,45,6,5415,6,86543,214,5,576867,5,15,7,8807765]
        for x in array:
            if user < x:
                high += 1
            elif user > x:
                low += 1
            elif user == x:
                equal += 1
        print(f"{high} numbers are higher than {user}")
        print(f"{low} numbers are lower than {user}")
        print(f"{equal} numbers are equal to {user}")
    fin()


main()