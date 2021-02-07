import random as r
import math as m

def generate_jog(user):
    
    #Take the details of the users jogging disance and pace
    jog_dist = user["running"]["jog"]["distance"]
    pace = user["running"]["jog"]["pace"]

    #calculate pace for jog (in meters per second)
    jog_time = jog_dist/pace 
    
    #return an instruction to be printed to the user
    print(f"Go for a {jog_dist}m jog and try to finish it in {jog_time} seconds.")
    return jog_dist, jog_time

def generate_distance(user):

    #Take the distance the user would consider to be average in kilometers
    target = user["running"]["distance"]["targ_dist"]
    maximum_dist = user["running"]["distance"]["max_dist"]
    pace_average_min = user["running"]["avg_pace"]["mins"]
    pace_average_sec = user["running"]["avg_pace"]["secs"]

    #convert pace into minutes (decimal)
    pace = pace_average_min + (pace_average_sec/60)

    #calculate pace for target distance and max distance (in KM per min)
    target_time = target*pace
    max_time = maximum_dist*pace

    #convert pace back into mis and secs for target and max
    target_time_mins_secs = m.modf(target_time)
    #print(target_time_mins_secs)
    target_pace_time = (int(target_time_mins_secs[1]), round(target_time_mins_secs[0]*60))
    #print(target_pace_time)
    max_time_mins_secs = m.modf(max_time)
    max_pace_time = (int(max_time_mins_secs[1]), round(max_time_mins_secs[0]*60))

    #return the paces and distances calculated to the user
    print(f"Try and finish your target distance ({target}KM) in {target_pace_time[0]} minute(s) and {target_pace_time[1]} second(s).")
    print(f"Try and finish your maximum distance ({maximum_dist}KM) in {max_pace_time[0]} minute(s) and {max_pace_time[1]} second(s).")
    return target_pace_time, max_pace_time

def generate_interval(user):

    #Take the distance of the sprint in meters
    distance = user["running"]["sprint"]["distance"]

    #calculate how many times it would take the user to complete 1000m from the distance
    total_runs = 1000//distance

    if difficulty == 0:
        rest = 60
    elif difficulty == 1:
        rest = 30
    elif difficulty == 2:
        rest = 10
    elif difficulty == 3:
        rest = 5

    #return workout
    print(f"Sprint {total_runs} {distance} meter runs with {rest} second(s) rest inbetween.")
    return distance, rest

def generate_sprint(user):

    #Take the distance of the sprint in meters and the usres personal best time for the sprint
    distance = user["running"]["sprint"]["distance"]
    pb = user["running"]["sprint"]["personal_best"]

    #return sprint with personal best
     print(f"Your personal best time for a {distance}m sprint is {pb} seconds. Try and beat it today.")
    return distance, pb
