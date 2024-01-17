#!/usr/bin/env python
# coding: utf-8

# In[1]:


#NetTech Welcoming you
#Welcome user
def nettech():
    print("Welcome to NetTech")
    #ask user to its name
    user_name=input("Enter your name here: ")
    #greet user
    print("Hello",user_name)
    #ask user to its mobile number
    user_ph_no=input("Please Enter your phone number: ")
    #display users phone number
    print("user Phone number: ",user_ph_no)
    #Ask user to its email id
    user_email_id=input("Enter your email id here: ")
    #display users email id
    print("User email id: ",user_email_id)
    #ask user to its preferred course
    user_pref_course=("Enter your preferred course here :")
    #display users preferred course here
    print("Users preferred course :",user_pref_course)
    #ask user to its preferred location
    user_pref_loc=("Enter your preferred location: ")
    #display users preferred location
    print("User preferred location: ",user_pref_loc)
    nettech()
    

def amachi_mumbai():
    #Mumbai chai recommendation bot
    print("Welcome to city of garam garam chai | Amachi Mumbai")
    #ask user to its name
    user_name=input("Enter your name here :")
    #greet user
    print("Hello",user_name)
    #ask user to its budget
    user_budget=int(input("Enter your budget here:"))
    #<500 go to taj hotel
    if user_budget>500:
        print("Go to taj hotel")
    #100-500 go to udipi hotels
    elif user_budget>=100 and user_budget<=500:
        print("Go to udipi hotels")
    #20-50 go to prathamesh's cafe
    elif user_budget>=20 and user_budget<=50:
        print("Go to prathamesh's cafe")
    #5-20 go to tapari
    elif user_budget>=5 and user_budget<=20:
        print("Go to tapari | better than taj hotel")
    #5< go to simon
    else:
        print("Go to simon!")

def shopping_mall():
    #welcome user
    print('welcome to angel shop mall')
    #ask the user name
    user_name=input('please enter the your good name')
    #greet user
    print('hello',user_name.title())
    #ask the user its budget
    user_budget=int(input('please enter your budget here:'))
    if user_budget>=1000:
        print('buy the make-up kit')
    elif user_budget>=500:
        print('buy the electronic device with high quality')
    elif user_budget>=300:
        print('buy the jewellery with good quality')
    elif user_budget>=200:
        print("buy the toy's")
    else:
        print('sorry !no any option is available below this range')
    # ask to user any dout
    a1=input('have any query')
    if a1=='yes':
        print('go to our website')
    else:
        pass
    print('Thank you for visit our shop have good day')






def Quiz():
    #NetTech bot
    #Welcome user
    print("Welcome to India GK Quiz")
    user_q1=input("What is the national animal of india")


    if user_q1.lower()=="tiger":  #also here we are using upper() and capetalize()
        print("yes your answer is correct")

    else: 
        print("sorrry your answer is Incorrect")

def head_tail():
    #Heads and tails game
    #welcome to hedas and tails game
    print("Welcome to Heads & Tails game!")
    #check users choice heads or tails
    user_choice=input("Ente your choice here:")
    #display users choice
    print("you choose:",user_choice)
    #coin toss
    import random 
    if(random.choice("ht"))=='h':
        coin_toss="Heads"
    else:
        coin_toss="Tails"
    #display coin toss
    print("toss result:",coin_toss)
    #if user choice is equal to coin toss ---> you win
    if user_choice.lower()==coin_toss.lower():
        print("You win!")
    else:
        print("you lose!")
    #thank you messesge
    print("Thank you to play this game")

def Dice_game():
    #Dice Game
    #Welcome to dice game
    print("Welcome to dice game!")
    #user roll dice
    user_roll=int(input("Enter your dice numbere here:"))
    if user_roll>=1:
        print("You chose",user_roll)
    else:
        print("No number in dice")
    #user roll dic
    import random
    dice_res=int(random.choice("123456"))
    #display user result
    print("Display user result", dice_res)
    #if dice res and user roll is equal --> you win
    if user_roll==dice_res:
        print("you win")
    else:
        print("you lose!")
    print("thank you for playing dice game")

def multiplication():
    #Welcome to Multiplication table
    #WElcome user
    print("Welcome to Multplication Table of Mathematics!")
    #choose any number
    num=int(input("Enter your number here: "))
    #Display multiplication table
    for i in range(1,11):
        print(num,"x",i,"=",num*i)

def cube():
    #Welcome to cube dictonary
    #WElcome user
    print("Welcome to cube world!")
    #ask user to choose any number as a input
    num=int(input("Enter your number here: "))
    #diplsay cube of the number
    for i in range(1,num+1):
        print("cube of",i,"=",i**3)

def factorial():
    #Factorial
    #Welcome user
    print("Welcome to the world of factorial!")
    #aks user to take 1 numnber as a input
    num=int(input("Enter your number here: "))
    factorial=1
    #display the factorial of the number

    if i in range(1,num+1):
        factorial=factorial*i
    print("the factorial of the",i,factorial)

def fibonacci():
    #Fibonacci series
    #WElcome user
    print("WElcome to the wor0.0.0.0.0.0.0.ld of fibonacci series!")
    #ask user to take 1 number as input
    num=int(input("Please Enter your number here: "))
    n1=0
    n2=1
    #display the fibonacci series
    for i in range(1,10):
        n3=n1+n2
        n1=n2
        n2=n3
        print("The fibonacii series of the numbers",i,"=",n3)


def pass_generate():
    #Password generator by using string library
    #welcome user
    print("Welcome to the world of password generator")
    #ask user to length of the password
    len=int(input("Plese Enter the length of the password :"))
    if len>=8 and len<100:
        print("It is valid")
        #user random adn string library
        import random
        import string
        char=string.ascii_letters+string.digits+string.punctuation
        password=""
        #use for loop
        for i in range(len):
            password=password+(random.choice(char))
        print(password)

    elif len>=100:
        print("Plese Enter the less characters")
    else:
        print("Please Enter the more characters")

def count_time():
    from countdown import countdown

    # Create a countdown of 1 minute and 10 seconds
    countdown(mins=1, secs=10)

    # Create a countdown of 1 minute
    countdown(1)

    #Create a countdown of 10 seconds
    countdown(mins=0, secs=10)

def mind():
    import time
    #welcome user
    print('welcome to the mind game')
    time.sleep(3)
    #Ask user to guess a number
    print('guess a number from 1-5000')
    time.sleep(3)
    #display 
    print('okay now divide the number by 2 ')
    time.sleep(3)
    print('finally minus the number which is guess')
    time.sleep(3)
    print('yes! found it')
    print('the answer is 25')


# In[3]:


import tkinter as tk

# creating a main window
window=tk.Tk()


# change title 
window.title('roshani')
# size
window.geometry('700x700')

#lable
tk.Label(window,text='made by : Roshani patil',bg='black',fg='red',font=('Helvetica',21,'bold')).place(x=200,y=20)



# button
tk.Button(window,text='factorial table',command=factorial,bg='white',fg='red').place(x=50,y=100,width=200,height=25)
tk.Button(window,text='fibonacci table',command=fibonacci,bg='white',fg='red').place(x=270,y=100,width=200,height=25)
tk.Button(window,text='pass_generate table',command=pass_generate,bg='white',fg='red').place(x=490,y=100,width=200,height=25)
tk.Button(window,text='count time table',command=count_time,bg='white',fg='red').place(x=50,y=150,width=200,height=25)
tk.Button(window,text='welcome bot',command=nettech,bg='white',fg='red').place(x=270,y=150,width=200,height=25)
tk.Button(window,text='recommandation_bot',command=amachi_mumbai,bg='white',fg='red').place(x=490,y=150,width=200,height=25)
tk.Button(window,text='shopping bot',command=shopping_mall,bg='white',fg='red').place(x=50,y=200,width=200,height=25)
tk.Button(window,text='quiz game',command=Quiz,bg='white',fg='red').place(x=270,y=200,width=200,height=25)
tk.Button(window,text='head and tail ',command=head_tail,bg='white',fg='red').place(x=490,y=200,width=200,height=25)
tk.Button(window,text='Dice_game ',command=Dice_game,bg='white',fg='red').place(x=50,y=250,width=200,height=25)
tk.Button(window,text=' multiplication table ',command=multiplication,bg='white',fg='red').place(x=270,y=250,width=200,height=25)







window.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:





# In[2]:





# In[ ]:



         


# In[ ]:



    
    


# In[ ]:





# In[ ]:




