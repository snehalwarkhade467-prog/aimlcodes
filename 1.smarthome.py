print("================================")
print(" Smart Home Automation System")
print("================================")

while True:
    print("\n1. Light Control")
    print("2. Fan Control")
    print("3. Door Security")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        light = input("Is the light ON? (yes/no): ").lower()

        if light == "yes":
            print("Light is ON.")
        else:
            print("Light is OFF.")

    elif choice == "2":
        fan = input("Is the fan ON? (yes/no): ").lower()

        if fan == "yes":
            print("Fan is ON.")
        else:
            print("Fan is OFF.")

    elif choice == "3":
        door = input("Is the door open? (yes/no): ").lower()

        if door == "yes":
            print("Door is open.")
            print("Security Alarm ON.")
        else:
            print("Door is closed.")
            print("Security Alarm OFF.")

    elif choice == "4":
        print("Exiting Smart Home Controller...")
        break

    else:
        print("Invalid choice! Try again.")