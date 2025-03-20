MAX_LENGTH = 3 

def shorten(lst):
   
    while len(lst) > MAX_LENGTH:  
        last_elem = lst.pop()  # Remove the last element
        print(last_elem)  # Print the removed element

def get_lst():

    lst = []
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop: ")
    return lst

def main():
    lst = get_lst()  # Get the list from the user
    shorten(lst)  # Call shorten function to modify the list

if __name__ == '__main__':
    main()
