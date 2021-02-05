#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random as r
import math as m

def generate_plank(user):
    
    #Take the details of the users current planking ability
    plank_mins = user["current_plank"]["mins"]
    plank_secs = user["current_plank"]["secs"]
    
    #Convert that into just minutes (demimal)
    base_time = plank_mins + plank_secs/60
    
    #add up to 30 seconds to the plank
    added_secs = r.randint(0, 30)/60
    target_plank_mins = base_time + added_secs
    
    #convert back into mins and secs
    target_plank_mins_secs = m.modf(target_plank_mins)
    target_plank_time = (int(target_plank_mins_secs[1]), round(target_plank_mins_secs[0]*60))
    
    #return an instruction to be printed to the user
    plank_time = f"Plank for {target_plank_time[0]} minute(s) and {target_plank_time[1]} seconds"
    return plank_time

def bodyweight(user):
    
    print("Your bodyweight workout is as follows:")
    
    exercises = ["plank", "press up"]
    workout = []
    
    #Chose what workouts to do, in what order
    for i in range(7):
        workout.append(r.choice(exercises))
    
    #Generate a unique instruction for each exercise in this workout
    for exercise in workout:
        if exercise == "plank":
            print(generate_plank(user))
            
#This would be replaced with the data for the logged in user
user = {"current_plank":{"mins":2, "secs":40}}

bodyweight(user)

