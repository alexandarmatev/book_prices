# Importing the logo for the program
from logo import logo

# Printing the logo for the program
print(logo)


# Function for getting of the book price
def get_book_price():
    price_input = float(input("Enter a book price: $"))
    return price_input


# Function for calculating the avg book price
def calculate_avg_price(prices_list):
    total_books = len(prices_list)
    sum_of_book_prices = sum(prices_list)
    avg_book_price = float("{:.2f}".format(sum_of_book_prices / total_books))
    return avg_book_price


# Empty list for storing of the book prices
list_with_book_prices = []
# While loop until the input of the user is either 0 or less
while True:
    # Catching a ZeroDivisionError error if the user's initial input is 0
    try:
        # Getting the book price by using the get book price function
        book_price = get_book_price()
        if book_price > 0:
            # Appending the user input into the list with book prices
            list_with_book_prices.append(book_price)
        elif book_price < 0:
            print("You've entered invalid amount. Try again.")
        else:
            # Getting the books number by using len function
            books_number = len(list_with_book_prices)
            # Storing the output of the avg price function into variable
            avg_price = calculate_avg_price(list_with_book_prices)
            # Printing the book count and the avg book price
            print(f"Book count is: {books_number}\n"
                  f"The average book price is: ${avg_price}")
            # Breaking of the while loop
            break
    except ZeroDivisionError:
        print("You've entered invalid amount. Try again.")

# Creating an empty dictionary which will map the book prices
mapped_book_prices = {}
# While loop until the input of the user is either 0 or less
while True:
    # Getting the book price by using the get book price function
    book_price = get_book_price()
    if book_price > 0:
        # Printing the appropriate message if the price is above the avg
        if book_price > avg_price:
            print(f"${book_price} is above the avg price")
            mapped_book_prices[book_price] = "above price"
        # Printing the appropriate message if the price is below the avg
        elif book_price < avg_price:
            print(f"${book_price} is below the avg price")
            mapped_book_prices[book_price] = "below price"
        # Printing the appropriate message if the price is equal to the avg
        elif book_price == avg_price:
            print(f"${book_price} is equal to the avg price")
            mapped_book_prices[book_price] = "equal price"
    elif book_price < 0:
        print("You've entered invalid amount. Try again.")
    else:
        # If the list is empty
        if not mapped_book_prices:
            print("There are no prices to show. Try with entering a book price.")
        # Finally, printing the dictionary with the appended values
        else:
            print(f"The final dictionary with the prices is: {mapped_book_prices}")
            # Breaking of the while loop
            break

