responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("What do you want to do now? ")
    responses[name] = response
    print("Cool!")
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        print("\n----Poll Results----")
        for name, response in responses.items():
            print(f"{name} is really wants to {response}.")
        polling_active = False
        break
    elif repeat == 'yes':
        continue
    elif repeat != 'yes' or repeat != 'no':
        print(f"Don't understand '{repeat}', try again.")