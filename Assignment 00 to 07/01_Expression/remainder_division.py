def main():
    dividend :int = int(input("Enter the Dividend: "))
    divisor :int = int(input("Enter the divisor: "))
    
    if divisor == 0:
        print("division by zero(0) is not possible")
        return
    
    quotient = dividend // divisor
    remainder = dividend % divisor
    
    print(f"The qoutient of this divison is {quotient} with a remainder of {remainder}")
    
if __name__ == '__main__':
    main()