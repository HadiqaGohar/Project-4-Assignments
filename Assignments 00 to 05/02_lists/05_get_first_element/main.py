def get_first_element(lst):

    print(lst[0]) 

def get_lst():
  
    lst = []
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":  # Keep adding elements until the user presses Enter
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop: ")
    return lst

def main():
    lst = get_lst()  # Get user-inputted list
    get_first_element(lst)  # Print first element

if __name__ == '__main__':
    main()
