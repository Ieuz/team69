import random


def generate_bcurl(user,diff):
    bcurl_reps=user["max_bcurls"]
    new_reps=bcurl_reps+diff*2
    print(f"Do {new_reps} bicep curls")


def generate_tcurl(user,diff):
    tcurl_reps=user["max_tcurls"]
    new_reps=tcurl_reps+diff*2
    print(f"Do {new_reps} tricep curls")


def generate_shoulderpress(user,diff):
    spress_reps=user["max_spresses"]
    new_reps=spress_reps+diff*2
    print(f"Do {new_reps} shoulder presses")


def generate_chestpress(user,diff):
    cpress_reps=user["max_cpresses"]
    new_reps=cpress_reps+diff*2
    print(f"Do {new_reps} chest presses")


def generate_lateralraise(user,diff):
    lraise_reps=user["max_lraises"]
    new_reps=lraise_reps+diff*2
    print(f"Do {new_reps} lateral raises")


def weights(user,diff):
    print("Your workout with weights is as follows:")

    exercises=["bicep curl","tricep curl","shoulder press","chest press","lateral raise"]
    workout=[]

    exercise_counts=[5,7,10,12]
    for i in range(exercise_counts[diff]):
        workout.append(random.choice(exercises))

    for exercise in workout:
        if exercise=="bicep curl":
            generate_bcurl(user,diff)
        elif exercise=="tricep curl":
            generate_tcurl(user,diff)
        elif exercise=="shoulder press":
            generate_shoulderpress(user,diff)
        elif exercise=="chest press":
            generate_chestpress(user,diff)
        elif exercise=="lateral raise":
            generate_lateralraise(user,diff)
user={"max_bcurls":2,"max_tcurls":4,"max_spresses":6,"max_cpresses":8,"max_lraises":10}
diff=2
weights(user,diff)