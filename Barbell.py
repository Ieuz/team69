import random


def generate_barbcurl(user,diff):
    barbcurl_reps=user["max_barbcurls"]
    new_reps=barbcurl_reps+diff*2
    print(f"Do {new_reps} barbell bicep curls")

def generate_barbsquat(user,diff):
    barbsquat_reps=user["max_barbsquats"]
    new_reps=barbsquat_reps+diff*2
    print(f"Do {new_reps} barbell squats")

def generate_benchpress(user,diff):
    benchpress_reps=user["max_benchpressreps"]
    new_reps=benchpress_reps+diff*2
    print(f"Do {new_reps} bench press reps")

def generate_deadlift(user,diff):
    deadlift_reps=user["max_deadlifts"]
    new_reps=deadlift_reps+diff*2
    print(f"Do {new_reps} deadlifts")

def generate_barbspress(user,diff):
    barbspress_reps=user["max_barbspresses"]
    new_reps=barbspress_reps+diff*2
    print(f"Do {new_reps} barbell shoulder presses")

def barbell(user,diff):
    print("Your workout with a barbell and a bench is as follows:")

    exercises=["barbell bicep curl","barbell squat","bench press","deadlift","barbell shoulder press"]
    workout=[]

    exercise_counts=[5,7,10,12]
    for i in range(exercise_counts[diff]):
        workout.append(random.choice(exercises))

    for exercise in workout:
        if exercise=="barbell bicep curl":
            generate_barbcurl(user,diff)
        elif exercise=="barbell squat":
            generate_barbsquat(user,diff)
        elif exercise=="bench press":
            generate_benchpress(user,diff)
        elif exercise=="deadlift":
            generate_deadlift(user,diff)
        elif exercise=="barbell shoulder press":
            generate_barbspress(user,diff)

user={"max_barbcurls":2,"max_barbsquats":4,"max_benchpressreps":6,"max_deadlifts":8,"max_barbspresses":10}
diff=3
barbell(user,diff)