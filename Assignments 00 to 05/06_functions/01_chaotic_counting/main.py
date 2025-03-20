import random

# Probability that the function `done` returns True
DONE_LIKELIHOOD = 0.2


def chaotic_counting():
    for i in range(10):
        curr_num = i + 1
        if done():
            return # this ends the function execution, so we'll get back to the main() function!
        print(curr_num)

# There is no need to edit code beyond this point

def done():
    """ Returns True with a probability of DONE_LIKELIHOOD """
    if random.random() < DONE_LIKELIHOOD:
        return True
    return False

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done")

if __name__ == "__main__":
    main()