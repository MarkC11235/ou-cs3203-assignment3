# list = [1,2,3,4,5]

def sumList(list):
    sum = 0
    for i in list:
        sum += i
    return sum

def multiplyList(list):
    product = 1
    for i in list:
        product *= i
    return product

def reverseList(list):
    return list[::-1]

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