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

# Creating an empty list which will store the modified book prices
modified_book_prices = []
# While loop until the input of the user is either 0 or less
while True:
    # Getting the book price by using the get book price function
    book_price = get_book_price()
    if book_price > 0:
        # Printing the appropriate message if the price is above the avg
        if book_price > avg_price:
            print(f"${book_price} is above the avg price")
            modified_book_prices.append("Above Price")
        # Printing the appropriate message if the price is below the avg
        elif book_price < avg_price:
            print(f"${book_price} is below the avg price")
            modified_book_prices.append("Below Price")
        # Printing the appropriate message if the price is equal to the avg
        elif book_price == avg_price:
            print(f"${book_price} is equal to the avg price")
            modified_book_prices.append("Equal Price")
    else:
        # Finally, printing the list with the appended values
        print(f"The final list with modified prices is: {modified_book_prices}")
        # Breaking of the while loop
        break

