# list = [1,2,3,4,5]

# this takes a list and returns the sum of all the elements in the list
def sumList(list):
    sum = 0
    for i in list:
        sum += i
    return sum

# this takes a list and returns the product of all the elements in the list
def multiplyList(list):
    product = 1
    for i in list:
        product *= i
    return product

def reverseList(list):
    return list[::-1]

# this is the main function that takes user input and calls the other functions
def main():
    list = []
    num_elements = input("Enter number of elements in list: ")
    for i in range(0, int(num_elements)):
        element = input("Enter element: ")
        list.append(int(element))
    
    print("Sum of list: ", sumList(list))
    print("Product of list: ", multiplyList(list))
    print("Reversed list: ", reverseList(list))

main()