# Importing the logo for the program
from logo import logo


# Printing the logo of the program
print(logo)


# Function for getting of the book price
def get_book_price():
    price_input = float(input("Enter a book price: $"))
    return price_input


# Function for calculating the avg book price and total books count
def calculate_avg_price(prices_list):
    total_books = len(prices_list)
    sum_of_book_prices = sum(prices_list)
    avg_book_price = float("{:.2f}".format(sum_of_book_prices / total_books))
    return avg_book_price, total_books


# Empty list for storing of the book prices
list_with_book_prices = []
# While loop until the input of the user is either 0 or less
while True:
    try:
        # Getting the book price by using the get book price function
        book_price = get_book_price()
        if book_price > 0:
            # Appending the user input into the list with book prices
            list_with_book_prices.append(book_price)
            print(f"${book_price} was added to the list.")
        elif book_price <= 0 and not list_with_book_prices:
            print("There is no valid initial price provided. Try with entering a valid book price.")
        elif book_price <= 0 and list_with_book_prices:
            # Storing the outputs of the avg price function into variable
            avg_price, books_number = calculate_avg_price(list_with_book_prices)
            # Printing the book count and the avg book price
            print(f"Book count is: {books_number}\n"
                  f"The average book price is: ${avg_price}")
            # Breaking of the while loop
            break
    # Catching a ValueError error if the user's initial input is different from integer
    except ValueError:
        print("You've entered invalid amount. Try again.")

# Creating an empty dictionary which will map the book prices
mapped_book_prices = {}
# While loop until the input of the user is either 0 or less
while True:
    try:
        # Getting the book price by using the get book price function
        print("Let's continue with comparing of the book prices.")
        book_price = get_book_price()
        if book_price > 0:
            # Printing the appropriate message if the price is above the avg
            if book_price > avg_price:
                print(f"${book_price} is above the avg price")
                mapped_book_prices[f"${book_price}"] = "above avg price"
            # Printing the appropriate message if the price is below the avg
            elif book_price < avg_price:
                print(f"${book_price} is below the avg price")
                mapped_book_prices[f"${book_price}"] = "below avg price"
            # Printing the appropriate message if the price is equal to the avg
            elif book_price == avg_price:
                print(f"${book_price} is equal to the avg price")
                mapped_book_prices[f"${book_price}"] = "equal to avg price"
        # Checking for a valid user input and for not empty dictionary
        elif book_price <= 0 and not mapped_book_prices:
            print("There are no prices to compare. Try with entering a valid book price.")
        # Breaking the while loop if the dictionary is not empty and the user has entered 0 or less
        elif book_price <= 0 and mapped_book_prices:
            print(f"The final dictionary with the prices is: {mapped_book_prices}")
            break
    # Catching a ValueError error if the user's initial input is different from integer
    except ValueError:
        print("You've entered invalid amount. Try again.")
