def average(a: float, b: float) -> float:
    """
    Returns the number which is halfway between a and b.
    """
    return (a + b) / 2  # Directly return the average

def main():
    avg_1 = average(0, 10)
    avg_2 = average(8, 10)
    
    final = average(avg_1, avg_2)
    print("avg_1:", avg_1)
    print("avg_2:", avg_2)
    print("final:", final)

if __name__ == '__main__':
    main()
