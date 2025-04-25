def is_leap(year) -> bool:
    leap = False
    # Remove the input from inside the function since year is already a parameter
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    return leap

# Add main block to test the function
if __name__ == "__main__":
    year = int(input("Enter a year: "))
    result = is_leap(year)
    if result:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")