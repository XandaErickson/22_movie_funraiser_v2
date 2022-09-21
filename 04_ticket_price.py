def not_blank(question, error):
    valid = False

    while not valid:
        response = input(question)

        while response != "":
            return response
        else:
            print(error)


def int_checker(question):
    error = "Please enter a whole number between 12 and 130."
    valid = False
    while not valid:
        try:
            response = int(input(question))
            if response <= 0:
                print(error)
            else:
                return response
        except ValueError:
            print(error)


name = ""
tickets = 0
max_tickets = 5
ticket_sale = 0
ticket_price = 0
profit_made = 0
profit = 0
while name != "xxx" and tickets < max_tickets:
    if tickets < max_tickets - 1:
        print("There are {} tickets remaining.".format(max_tickets - tickets))

    else:
        print("There is one ticket left.")

    name = not_blank("Name:", "This cannot be blank, please enter your name.")
    if name == "xxx":
        break

    age = int_checker("Age:  ")
    if age < 12:
        print("You are too young to see this movie.")
        continue
    elif age > 130:
        print("There must be a mistake.")
        continue
    if age < 16:
        ticket_price = 7.5
    elif age < 65:
        ticket_price = 10.5
    else:
        ticket_price = 6.5

    tickets += 1
    ticket_sale += ticket_price
    print("Your ticket price is ${:.2f}".format(ticket_price))
    profit_made = ticket_price - 5

    ticket_price = 0
print("You have made ${:.2f}".format(profit))
