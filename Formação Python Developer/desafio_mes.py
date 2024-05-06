def get_month_name(number):
    months = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    }

    if number in months:
        return months[number]
    else:
        return 'Invalid month number'

# Get user input and convert to integer
month_number = int(input("Enter a number from 1 to 12: "))

# Get and print the corresponding month name
month_name = get_month_name(month_number)
print(f"The month corresponding to the number {month_number} is {month_name}.")