# function goes here

def not_blank(question: object, error: object) -> object:
    valid = False

    while not valid:
        response = input(question)

        while response != "":
            return response
        else:
            print(error)


tickets = 5

# Main Routine
while tickets != 0:
    print("There are {} tickets remaining.".format(tickets))
    name: object = not_blank("What is your name?: ", "This cannot be blank, please enter your name.")
    tickets -= 1
    if name == "xxx":
        tickets = 0
    if tickets == 0 and name != "xxx":
        print("You have bought all of the remaining tickets.")
