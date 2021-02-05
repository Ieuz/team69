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
    print(f"Plank for {target_plank_time[0]} minute(s) and {target_plank_time[1]} seconds")
    return target_plank_time


def generate_pressup(user, diff):
    
    #Take the details of the users current press up ability
    pressup_reps = user["max_pressups"]
    
    #add up to a 15% increase in number of reps (dependent upon difficulty)
    increase = diff*0.05 + 1
    new_reps = int(pressup_reps * increase)
    
    #decide upon variation
    variations = ["standard", "diamond", "wide hands"]
    variation = r.choice(variations)
    
    #Return the instruction to be printed to the user
    print(f"Do {new_reps} {variation} press ups.")
    return new_reps

def generate_squat(user, diff):
    
    #Take the details of the users current press up ability
    max_squats = user["max_squats"]
    
    #add up to a 15% increase in number of reps (dependent upon difficulty)
    increase = diff*0.05 + 1
    new_reps = int(max_squats * increase)
    
    #Return the instruction to be printed to the user
    print(f"Do {new_reps} squats.")
    return new_reps

def generate_situp(user, diff):
    
    #Take the details of the users current press up ability
    situp_reps = user["max_situps"]
    
    #add up to a 15% increase in number of reps (dependent upon difficulty)
    increase = diff*0.05 + 1
    new_reps = int(situp_reps * increase)
    
    #decide upon variation
    variations = ["sit ups", "crunches"]
    variation = r.choice(variations)
    
    #Return the instruction to be printed to the user
    print(f"Do {new_reps} {variation}.")
    return new_reps

def bodyweight(user, diff):
    
    print("Your bodyweight workout is as follows:")
    
    exercises = ["plank", "press up", "squat", "sit up"]
    workout = []
    
    #Chose what workouts to do, in what order
    exercise_counts = [7, 10, 12, 15]
    for i in range(exercise_counts[diff]):
        workout.append(r.choice(exercises))
    
    #Generate a unique instruction for each exercise in this workout
    for exercise in workout:
        if exercise == "plank":
            generate_plank(user)
        elif exercise == "press up":
            generate_pressup(user, diff)
        elif exercise == "squat":
            generate_squat(user, diff)
        else:
            generate_situp(user, diff)
            
#This would be replaced with the data for the logged in user
user = {"current_plank":{"mins":2, "secs":40}, "max_pressups":30, "max_squats":15, "max_situps":30}
difficulty = 3

bodyweight(user, difficulty)
