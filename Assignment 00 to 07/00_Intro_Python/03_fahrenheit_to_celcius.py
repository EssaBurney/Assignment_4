def main():
    
    fehrenheit = float(input("\033[1mEnter the temperature in fehrenheit to convert it to celsius: \033[0m"))
    
    celsius = (fehrenheit - 32) / 1.8
    print(f"temperature :{fehrenheit} F = {celsius}C")
    
if __name__ == "__main__":
    main()