DAYS_IN_YEAR = 365
HOURS_IN_DAYS = 24
MINUTES_IN_HOURS = 60
SECONDS_IN_MINUTES = 60


def main():
    year :int = int (input("enter the years you want to know how many seconds are there in it. "))
    year = year * DAYS_IN_YEAR * HOURS_IN_DAYS * MINUTES_IN_HOURS * SECONDS_IN_MINUTES
    print(f"There are {year} seconds in year")
    
if __name__ == '__main__':
    main()