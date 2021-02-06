import random


def generate_onearmbcurl(user,diff):
    onearmcurl_reps=user["max_onearmcurls"]
    new_reps=onearmcurl_reps+diff*2
    print(f"Do {new_reps} one arm bicep curls")

def generate_flye(user,diff):
    flye_reps=user["max_flyes"]
    new_reps=flye_reps+diff*2
    print(f"Do {new_reps} Flyes")

def generate_frsquats(user,diff):
    frsquat_reps=user["max_frsquats"]
    new_reps=frsquat_reps+diff*2
    print(f"Do {new_reps} front squats")

def generate_splitter(user,diff):
    splitter_reps=user["max_splitters"]
    new_reps=splitter_reps+diff*2
    print(f"Do {new_reps} splitters")

def generate_latwalks(user,diff):
    latwalk_reps=user["max_latwalks"]
    new_reps=latwalk_reps+diff*2
    print(f"Do {new_reps} lateral walk reps")

def Rband(user,diff):
    print("Your workout with the resistance band is as follows:")

    exercises=["one-arm bicep curl","flye","front squat","splitter","lateral walk"]
    workout=[]

    exercise_counts=[5,7,10,12]
    for i in range(exercise_counts[diff]):
        workout.append(random.choice(exercises))

    for exercise in workout:
        if exercise=="one-arm bicep curl":
            generate_onearmbcurl(user,diff)
        elif exercise=="flye":
            generate_flye(user,diff)
        elif exercise=="front squat":
            generate_frsquats(user,diff)
        elif exercise=="splitter":
            generate_splitter(user,diff)
        elif exercise=="lateral walk":
            generate_latwalks(user,diff)

user={"max_onearmcurls":2,"max_flyes":4,"max_frsquats":6,"max_splitters":8,"max_latwalks":10}
diff=2
Rband(user,diff)