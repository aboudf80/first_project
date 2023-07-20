import requests


def convert_currency(amount, from_currency, to_currency):
    # API endpoint to get the latest exchange rates
    endpoint = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"

    try:
        # Make a GET request to the API endpoint
        response = requests.get(endpoint)

        # Parse the response as JSON
        data = response.json()

        # Extract the exchange rate for the target currency
        target_rate = data["rates"][to_currency]

        # Convert the amount to the target currency
        converted_amount = amount * target_rate

        return converted_amount

    except requests.exceptions.RequestException as e:
        # Handle any errors that occur during the request
        print("An error occurred:", str(e))
        return None

print("Welcome to currency converter")
# Currency conversion options
print("1. USD to ILS")
print("2. ILS to USD")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    from_currency = "USD"
    to_currency = "ILS"
elif choice == 2:
    from_currency = "ILS"
    to_currency = "USD"
else:
    print("Invalid choice!")
    choice = int(input("Enter your choice (1 or 2): "))

amount = float(input(f"Enter the amount in {from_currency}: "))

converted_amount = convert_currency(amount, from_currency, to_currency)

if converted_amount is not None:
    print(f"{amount} {from_currency} is equivalent to {converted_amount} {to_currency}.")
    print("do you want to start over?")
    print("1. Yes")
    print("2. No")




    choice2 = int(input("Enter your choice (1 or 2): "))
    if choice2 == 1:
        print("1. USD to ILS")
        print("2. ILS to USD")
        choice = int(input("Enter your choice (1 or 2): "))
        if choice == 1:
                  from_currency = "USD"
                  to_currency = "ILS"
        elif choice == 2:
                from_currency = "ILS"
                to_currency = "USD"
        else:
                print("Invalid choice!")
                choice = int(input("Enter your choice (1 or 2): "))

        amount = float(input(f"Enter the amount in {from_currency}: "))

        converted_amount = convert_currency(amount, from_currency, to_currency)

        if converted_amount is not None:
            print(f"{amount} {from_currency} is equivalent to {converted_amount} {to_currency}.")

    else:
         exit()

