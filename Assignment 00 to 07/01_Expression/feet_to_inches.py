foot : int =12

def main():
    conversion: float = float(input("Enter the feet to convert it into inches: "))
    inches = conversion * foot
    
    if inches == 12:
        print(f"There are {inches} Inches in the {conversion} Foot")
        
    else :
        print(f"There are {inches} Inches in {conversion} Feet")
        


if __name__ == '__main__':
    main()
        