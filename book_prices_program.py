def get_book_price():
    price_input = float(input("Enter a book price: $"))
    return price_input


def calculate_avg_price(prices_list):
    total_books = len(prices_list)
    sum_of_book_prices = sum(prices_list)
    avg_book_price = float("{:.2f}".format(sum_of_book_prices / total_books))
    return avg_book_price


list_with_book_prices = []
while True:
    book_price = get_book_price()
    if book_price > 0:
        list_with_book_prices.append(book_price)
    else:
        books_number = len(list_with_book_prices)
        avg_price = calculate_avg_price(list_with_book_prices)
        print(f"Book count is: {books_number}\n"
              f"The average book price is: ${avg_price}")
        break


modified_book_prices = []
while True:
    book_price = get_book_price()
    if book_price > 0:
        if book_price > avg_price:
            print(f"${book_price} is above the avg price")
            modified_book_prices.append("Above Price")
        elif book_price < avg_price:
            print(f"${book_price} is below the avg price")
            modified_book_prices.append("Below Price")
        elif book_price == avg_price:
            print(f"${book_price} is equal to the avg price")
            modified_book_prices.append("Equal Price")
    else:
        print(modified_book_prices)
        break

