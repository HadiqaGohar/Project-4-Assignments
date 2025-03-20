INCHES_IN_FOOT = 12  

def main():
   
    feet = float(input("Enter number of feet: "))

    # Convert feet to inches
    inches = feet * INCHES_IN_FOOT

  
    print(f"{feet} feet is equal to {inches} inches.")


if __name__ == '__main__':
    main()
