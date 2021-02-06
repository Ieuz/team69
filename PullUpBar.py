import random


def generate_pullup(user,diff):
    pullup_reps=user["max_pullups"]
    new_reps=pullup_reps+diff*2
    print(f"Do {new_reps} pull-ups")

def generate_chinup(user,diff):
    chinup_reps=user["max_chinups"]
    new_reps=chinup_reps+diff*2
    print(f"Do {new_reps} chin-ups")

def generate_muscleup(user,diff):
    muscleup_reps=user["max_muscleups"]
    new_reps=muscleup_reps+diff*2
    print(f"Do {new_reps} muscle-ups")

def generate_kneestoelbows(user,diff):
    kte_reps=user["max_ktes"]
    new_reps=kte_reps+diff*2
    print(f"Do {new_reps} knees to elbows reps")

def generate_hangingkneeraise(user,diff):
    hkr_reps=user["max_hkrs"]
    new_reps=hkr_reps+diff*2
    print(f"Do {new_reps} hanging knee raises")

def PullUpBar(user,diff):
    print("Your workout with the pull up bar is as follows:")

    exercises=["pull up","chin up","muscle up","knees to elbows","hanging knee raise"]
    workout=[]

    exercise_counts=[2,4,6,7]
    for i in range(exercise_counts[diff]):
        workout.append(random.choice(exercises))

    for exercise in workout:
        if exercise=="pull up":
            generate_pullup(user,diff)
        elif exercise=="chin up":
            generate_chinup(user,diff)
        elif exercise=="muscle up":
            generate_muscleup(user,diff)
        elif exercise=="knees to elbows":
            generate_kneestoelbows(user,diff)
        elif exercise=="hanging knee raise":
            generate_hangingkneeraise(user,diff)

user={"max_pullups":2,"max_chinups":4,"max_muscleups":6,"max_ktes":8,"max_hkrs":10}
diff=1
PullUpBar(user,diff)