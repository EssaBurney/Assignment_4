import random

NUM_SIDES :int = 6

def main():
    die1 :int = random.randint(1,NUM_SIDES)
    die2 :int = random.randint(2,NUM_SIDES)
    
    total :int = die1 + die2
    
    print(f"First Die:  {die1}")
    print(f"second Die: {die2}")
    print(f"The total of Die 1 and Die 2 is : {total}")
    
if __name__ == '__main__':
    main()