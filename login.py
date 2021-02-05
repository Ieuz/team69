#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def read_profile(name):
    return True

def login():
    cont = True
    print("Welcome to the fitness tracker 3000!")
    
    while cont:
        print("Would to log in or sign up?")
        login_bool = input(">>>")
        
        if login_bool.lower() == "sign up":
            create_profile()
            cont = False
            
        elif login_bool.lower() == "log in":
            logging_in = True
            while logging_in:
                try: 
                    print("What is your profile name?")
                    profile_name = input(">>>")
                    read_profile(profile_name)
                    logging_in = False
                    cont = False
                except:
                    print("This profile name does not exist. Please try again.")
        else:
            print("This is not a valid input. Please type 'log in' or 'sign up'.")

