class chatbook:
    def __init__(self):
        self.__name = "Default user"
        self.username = ''
        self.password = ''
        self.loggedin = False
        #self.menu()
    def menu(self):
        user_input = input("""Welcome to chatbook, How would you like to proceed
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit                                       
                           """)
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.sendmsg()
        else:
            exit()

    def signup(self):
        email = input("Enter you email here->  ")
        pwd = input("Setup your password here->  ")
        self.username = email
        self.password = pwd
        print("You have signup successfully")
        print("\n")
        self.menu()

    def signin(self):
        if(self.username == '' and self.password == ''):
            print("Please signup first by pressing 1 in the main menu")
        else:
            uname = input("Enter you email/username here ->")
            pwd = input("Enter your password")
            if self.username == uname and self.password == pwd:
                print("You have signed in successfully !!")
                self.loggedin = True
            else:
                print("Please write the correct credentials")
        self.menu()

    def my_post(self):
        if(self.loggedin == True):
            txt = input("Enter you message here")
            print(f"Following content has been posed {txt}")
        else:
            print("You need to sign in first of post.")
        print("\n")
        self.menu()
    def sendmsg(self):
        if(self.loggedin==True):
            txt = input("Enter you message here -- ")
            frnd = input("Whom to send the message? -> ")
            print(f"Your mesage has been sent to {frnd}---{txt}")

        else:
            print("You need to signin first for message")
        print("\n")
        self.menu()
            
        













#user1 = chatbook()