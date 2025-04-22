def signUp():
    print("----Sign Up for Elementa----")
    while True:
        userName = input("Please create a user name: ").strip().lower()

        if len(userName) <= 3 or " " in userName:
            print("User name must be larger than 3 characters and contain no spaces")
            continue
        

        print("Hello " + userName)

        break

    
signUp()