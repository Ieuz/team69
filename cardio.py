import random as r
import math as m
    
def running_on_the_spot(user,diff):
    
    #Take the details of the users curent running ability
    running_time = user["max_running_time"]
    
    #add up to a 15% increase in running time (dependent upon difficulty)
    increase = diff*0.05 + 1
    new_time = int(running_time * increase)
    
    #Return the instruction to be printed to the user
    print(f"Do {new_time} minutes of running on the spot.")
    return new_time

def squats(user, diff):
    
    #Take the details of the users current squats ability
    max_squats = user["max_squats"]
    
    #add up to a 15% increase in number of reps (dependent upon difficulty)
    increase = diff*0.05 + 1
    new_reps = int(max_squats * increase)
    
    #Return the instruction to be printed to the user
    print(f"Do {new_reps} squats.")
    return new_reps

def high_knees(user,diff):
    #Take the details of the users current high knees max time
    max_time = user["max_high_knees"]
    
    #add up to a 15% increase in number of time (dependent upon difficulty)
    increase = diff*0.05 + 1
    new_time = int(max_time * increase)
    
    #Return the instruction to be printed to the user
    print(f"Do {new_time} minutes of high knees.")
    return new_time

def burpees(user,diff):
    #Take the details of the users current max burpees
    max_burpee = user["max_burpees"]
    
    #add up to a 15% increase in number of reps (dependent upon difficulty)
    increase = diff*0.05 + 1
    new_burpee = int(max_burpee * increase)
    
    #Return the instruction to be printed to the user
    print(f"Do {new_burpee} burpees.")
    return new_burpee
 
def skaters(user,diff):
    #Take the details of the users current skaters max time
    max_time = user["max_skaters"]
    
    #add up to a 15% increase in time (dependent upon difficulty)
    increase = diff*0.05 + 1
    new_time = int(max_time * increase)
    
    #Return the instruction to be printed to the user
    print(f"Do {new_time} minutes of skaters.")
    return new_time

def mountain_climbers(user,diff):
    #Take the details of the users current mountain climbers max time
    max_time = user["max_mountain_climbers"]
    
    #add up to a 15% increase in time (dependent upon difficulty)
    increase = diff*0.05 + 1
    new_time = int(max_time * increase)
    
    #Return the instruction to be printed to the user
    print(f"Do {new_time} minutes of mountain climbers.")
    return new_time

def up_down_plank(user,diff):
    #Take the details of the users current up down plank max time
    max_time = user["max_up_down_plank"]
    
    #add up to a 15% increase in time (dependent upon difficulty)
    increase = diff*0.05 + 1
    new_time = int(max_time * increase)
    
    #Return the instruction to be printed to the user
    print(f"Do {new_time} minutes of up down planks.")
    return new_time

def plank(user,diff):
    #Take the details of the users current max plank time
    max_time = user["max_plank"]
    
    #add up to a 15% increase in time (dependent upon difficulty)
    increase = diff*0.05 + 1
    new_time = int(max_time * increase)
    
    #Return the instruction to be printed to the user
    print(f"Do {new_time} minutes of the plank.")
    return new_time

def side_plank(user,diff):
    #Take the details of the users current max side plank time
    max_time = user["max_side_plank"]
    
    #add up to a 15% increase in time (dependent upon difficulty)
    increase = diff*0.05 + 1
    new_time = int(max_time * increase)
    
    #Return the instruction to be printed to the user
    print(f"Do {new_time} minutes of side planks.")
    return new_time

def star_jumps(user,diff):
    #Take the details of the users current max star jumps
    max_star_jumps = user["max_star_jumps"]
    
    #add up to a 15% increase in number of reps (dependent upon difficulty)
    increase = diff*0.05 + 1
    new_star_jumps = int(max_star_jumps * increase)
    
    #Return the instruction to be printed to the user
    print(f"Do {new_star_jump} star jumps.")
    return new_star_jumps

def tuck_jumps(user,diff):
    #Take the details of the users current max tuck jumps
    max_tuck_jumps = user["max_tuck_jumps"]
    
    #add up to a 15% increase in number of reps (dependent upon difficulty)
    increase = diff*0.05 + 1
    new_tuck_jumps = int(max_tuck_jumps * increase)
    
    #Return the instruction to be printed to the user
    print(f"Do {new_tuck_jumps} tuck jumps.")
    return new_tuck_jumps
    
def cardio_workout(user, diff):
    
    print("Your cardio workout is as follows:")
    
    exercises = ["running on the spot","squats","high knees","burpees","skaters","mountain climbers","up down planks","plank","side planks","star jumps","tuck jumps"]
    workout = []
    
    #Chose what workouts to do, in what order
    exercise_counts = [7, 10, 12, 15]
    for i in range(exercise_counts[diff]):
        workout.append(r.choice(excersises))
    
    #Generate a unique instruction for each exercise in this workout
    for exercise in workout:
        if exercise == "running on the spot":
            running_on_the_spot(user,diff)
        elif exercise == "squats":
            squats(user,diff)
        elif exercise == "high knees":
            high_knees(user,diff)
        elif exercise == "burpees":
            burpees(user,diff)
        elif exercise == "skaters":
            skaters(user,diff)
        elif exercise == "mountain climbers":
            mountain_climbers(user,diff)
        elif exercise == "up down planks":
            up_down_planks(user,diff)
        elif exercise == "plank":
            planks(user,diff)
        elif exercise == "side planks":
            side_planks(user,diff)
        elif exercise == "star jumps":
            star_jumps(user,diff)
        else:
            tuck_jumps(user,diff)
            
            
#This would be replaced with the data for the logged in user
user = {"current_plank":{"mins":2, "secs":40}, "max_pressups":30, "max_squats":15, "max_situps":30}
difficulty = 3

cardio_workout(user, difficulty)
