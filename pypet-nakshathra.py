# Nakshathra First Python Project
import random
import time

name = "The Queen Python"
photo ="*"
age = 5
weight = 5.5
hungryness = 10
sleepiness = 10
mood = True
status="alive"
terminate =True
phrases=["iam your besti", "keep it up", "do you like pop corn?"]


def startup_pypet():
    print("welcome to py pet!")
    print("Hello, its " + name)

def pypet_status():
    print(name + "  is  " + status)

def pypet_stats():
    print(name + " weight is " + str(weight) + " pounds ")

def pypet_feed():
    global hungryness
    hungryness -=6
    print("hungryness: " + str(hungryness))
    if hungryness < 5 :
        print("Your pet is hungry!")
        print("""
        Choose the food you like to feed?
        1. Milk
        2. French Fries
        3. Chocolate
        """)
        food_name = input('<<<')
        print("Serving: " + food_name)
    else:
        print("Your pypet *BURPS* loudly")

def pypet_mood():
    if mood:
        print("happy-blue color")
    elif not mood:
        print("angry-red color")
    else:
        print("normal-yellow colour")


def pypet_chat():
        print("What's your name??")
        user_name = input('<')
        print("Hello " + user_name)
        print(random.choice(phrases))


def pypet_play():
        print("It's play time")
        print("what game should we play")
        print("""
        1=rock,paper,scissor 
        2=painting with paws 
        3=find the letter 
        4=word search 
        5=hangman 
        6=word chain 
        7=two truths and one lie 
        8=trivia""")

        game_name = input('<<<')
        print("Playing: " + game_name)


def pypet_sleep():
        global sleepiness
        sleepiness -= 3
        time.sleep(5)
        print("Go to bed")
        print("Zzz... I'm feeling rested now.")
        print("sleepiness: " + str(sleepiness))

def simulate():
    while not terminate:
        print("#################")
        time.sleep(1)
        print("sleepiness: " + str(sleepiness))

print("""
Welcome to Nakshathra's PyPet care and play area
Choose one of the following
1=welcome
2=play
3=stats 
4=status 
5=feed 
6=mood 
7=chat
8=sleep
9=quit""")

user_input = input('>')

if user_input == "1":
    startup_pypet()
elif user_input == "2":
    pypet_play()
elif user_input == "3":
    pypet_stats()
elif user_input == "4":
    pypet_status()
elif user_input == "5":
    pypet_feed()
elif user_input == "6":
    pypet_mood()
elif user_input == "7":
    pypet_chat()
elif user_input == "8":
    pypet_sleep()
elif user_input == "9":
    terminate = True
else:
    startup_pypet()
    pypet_stats()
    pypet_status()
    pypet_feed()
    pypet_mood()
    pypet_play()
    pypet_sleep()
    print("Goodbye!")


#Call Simulate Pet
simulate()

