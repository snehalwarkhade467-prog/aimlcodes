print("================================")
print(" Welcome to Recommendation Assistant")
print("================================")

print("1. Movies")
print("2. Books")
print("3. Music")

choice = input("Enter your choice (1/2/3): ")

if choice == "1":
    print("\nChoose Movie Genre:")
    print("a. Action")
    print("b. Comedy")
    print("c. Drama")

    genre = input("Enter genre (a/b/c): ")

    if genre == "a":
        print("Recommended Movie: RRR")
    elif genre == "b":
        print("Recommended Movie: Hera Pheri")
    elif genre == "c":
        print("Recommended Movie: Taare Zameen Par")
    else:
        print("Invalid Genre!")

elif choice == "2":
    print("\nChoose Book Category:")
    print("a. Mythology")
    print("b. Fiction")
    print("c. Motivation")

    category = input("Enter category (a/b/c): ")

    if category == "a":
        print("Recommended Book: The Palace of Illusions")
    elif category == "b":
        print("Recommended Book: The Guide")
    elif category == "c":
        print("Recommended Book: Wings of Fire")
    else:
        print("Invalid Category!")

elif choice == "3":
    print("\nChoose Music Type:")
    print("a. Romantic")
    print("b. Devotional")
    print("c. Party")

    music = input("Enter type (a/b/c): ")

    if music == "a":
        print("Recommended Song: Kesariya")
    elif music == "b":
        print("Recommended Song: Achyutam Keshavam")
    elif music == "c":
        print("Recommended Song: Kala Chashma")
    else:
        print("Invalid Music Type!")

else:
    print("Invalid Choice!")