def main():
    side_1 = float(input("\033[1mEnter the length of side 1: \033[0m"))
    side_2 = float(input("\033[1mEnter the length of side 2: \033[0m"))
    side_3 = float(input("\033[1mEnter the length of side 3: \033[0m"))
    
    perimeter = side_1 + side_2 + side_3
    
    print(f"The perimeter of the triangle is: {perimeter}")
    
    
if __name__ == "__main__":
    main()
    