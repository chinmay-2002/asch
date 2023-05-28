name=input("please enter your name=")
print("Hello!",name," my name is chitti(the chatbot) please choose below option to interact with me")

def chatBot():
    print("1.do you want to chat?")
    print("2.do you want to play 'guess age' game?")
    print("3.do you want to exit")
    ch=int(input("enter your choice="))
    takeInput(ch)

def takeInput(ch):
    if ch==1:
        interact()
    elif ch==2:
        game()
    elif ch==3:
        print("good bye..")
        exit(0)

def interact():
    print("Chitti: Hello!",name,"you can interact with me by typing following words")
    print("1.hi\n2.how are you?\n3.what's your name?\n4.bye")
    prompts = {
        "hi": "Hello!",
        "how are you?": "I'm doing well, thank you!",
        "what's your name?": "My name is chitti.",
        "bye": "Goodbye! Take care."
    }
    while True:
        print(name,end=":")
        user_input = input()
        user_input = user_input.lower()
        if (user_input == 'bye'):
            print("chitti: Good bye! take care.\n")
            chatBot()
        elif user_input in prompts:
            print("chitti:", prompts[user_input])
        else:
            print("I'm sorry, I don't understand. Can you please rephrase?")

def game():
    print('hello',name,"welcome to 'guess age' game..")
    print("let me guess your age by asking few questions..")
    rem3 = int(input("Q1.what's your remainder for age after dividing by 3 ?="))
    rem5 = int(input("Q2.what's your remainder for age after dividing by 5?="))
    rem7 = int(input("Q3.what's your remainder for age after dividing by 7?="))
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
    print("Your age is",age)
    print(name,end=" ")
    ip=input("is this correct?(yes/no)=")
    if ip=='yes':
        print("thank you..\n")
        chatBot()
    else:
        print('something went wrong please enter proper remainders')
        game()

#calling chatBot() method
chatBot()