def start():
    print("Welcome to Madhura's Chatbot")
    print("I will help you, ask me questions")
    print("1: Tell me about Hotel")
    print("2: Tell me Hotel Owner name")
    print("3: Contact")
    print("4: End chat")
    print("5: Tell my age ")

def guess_age(rem3, rem5, rem7):
    print('\nLet me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is {0}; that's a good time to start programming!".format(age))



    
def answer(opt):
    if opt==1:
        print("Hotel is Beautiful")
    elif opt==2:
        print("Chinmay Pimpalgaonkar")
    elif opt==3:
        print("Contact 100")
    elif opt==4:
        print("Chat ended")
    elif opt==5:
        guess_age(0,1,0)
    else:
        print("Enter valid option")



# start()

while True:
    start()
    a = int(input("Enter Choice"))
    answer(a)
    if a==4:
        break
        
print("Thank you don't come again")