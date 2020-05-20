def ask_user():
    msg = ""
    while True:
        msg = input("How do you do?")
        if msg.lower() == "good":
            print("That is great!")
            break
        else:
            print("Interesting...")

ask_user()
