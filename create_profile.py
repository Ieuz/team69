def inpt(ting):
    outpt = ""
    while outpt == "":
        outpt = input(ting)

    return outpt
        

def create_profile():
    categories = ["running", "indoor cardio", "weight training", "bodyweight training"]
    equipment = ["dumbells", "resistance band", "barbell", "pullup bar"]

    
    name = input("Please enter your name: ")
    print("Categories:\nrunning,\nindoor cardio,\nweight training,\nbodyweight training")
    print("Which of the above workouts are you interested in? Please enter your answers as a list seperated by commas\n(In the format 'running,indoor cardio, etc.')")
    user_cats = input(">>>")
    user_cats_lst = user_cats.split(",")
    cats_lst = []
    ccl = False


    for x in range(len(user_cats_lst)):
        user_cats_lst[x] = (user_cats_lst[x]).strip()
    

    for wrkout in user_cats_lst:
        if wrkout in categories:
            if wrkout not in cats_lst:
                cats_lst.append(wrkout)
        else:
            workout = wrkout
            while workout not in categories:
                ccl = False
                print(f"Workout {workout} was not recognised, type the workout you meant or type CANCEL to cancel")
                workout = input(">>>")
                if workout == "CANCEL" or workout == "cancel":
                    ccl = True
                    break
            if ccl != True:
                cats_lst.append(workout)

    if "running" in cats_lst:
        targ_dist = inpt("What is your target distance in km?")
        max_dist = inpt("What is your current estimated maximum distance in km?")
        avg_pace = float(inpt("What is your average pace in minutes per kilometer? (enter as decimal with a decimal point)"))
        max_sprint = inpt("What is your maximum sprint distance in metres?")


    print("Please enter which equipment you own from this list, seperated by commas:\ndumbells, resistance band,\nbarbell, pullup bar")
    user_eqip = input(">>>")
    user_eqip_lst = user_eqip.split(",")
    equipment_list = []


    for x in range(len(user_eqip_lst)):
        user_eqip_lst[x] = (user_eqip_lst[x]).strip()
    

    for equipment_piece in user_eqip_lst:
        if equipment_piece in equipment:
            if equipment_piece not in equipment_list:
                equipment_list.append(equipment_piece)
        else:
            equip_piec = equipment_piece
            while equip_piec not in equipment:
                ccl = False
                print(f"Equipment piece {equipment_piece} was not recognised, type the equipment you meant or type CANCEL to cancel")
                equip_piec = input(">>>")
                if equip_piec == "CANCEL" or equip_piec == "cancel":
                    ccl = True
                    break
            if ccl != True:
                equipment_list.append(equip_piec)
    workout_stats = {}
    if "bodyweight" in cats_lst or "weight training" in cats_lst or "indoor cardio" in cats_lst:
        current_plank = {}
        plankstats = ""
        while len(plankstats.split(",")) != 2:
            plankstats = inpt("Please enter how long you can do a plank for in the format mins,secs (i.e. '3,20'):")
        plankstats_lst = plankstats.split(",")
        current_plank["mins"] = plankstats_lst[0]
        current_plank["secs"] = plankstats_lst[1]

    
    if "bodyweight" in cats_lst or "indoor cardio" in cats_lst:
        workout_stats["max_pressups"] = inpt("Enter your max pressups:")
        workout_stats["max_squats"] = inpt("Enter your max squats:")
        workout_stats["max_situps"] = inpt("Enter your max situps:")
        workout_stats["max_running_time"] = inpt("Enter your max running on the spot time in seconds:")
        workout_stats["max_high_knees"] = inpt("Enter your max high knees time in seconds:")
        workout_stats["max_burpees"] = inpt("Enter your max burpees:")
        workout_stats["max_skaters"] = inpt("Enter your max skater time in seconds:")
        workout_stats["max_mountain_climbers"] = inpt("Enter your max mountain climber time in seconds:")
        workout_stats["max_plank"] =(int(plankstats_lst[0])*60) + int(plankstats_lst[1])
        workout_stats["max_side_plank"] = inpt("Enter your max side plank time in seconds:")
        workout_stats["max_star_jumps"] = inpt("Please enter your max star jumps:")
        workout_stats["max_tuck_jumps"] = inpt("Please enter your max tuck jumps:")
        for key in workout_stats.keys():
            workout_stats[key] = int(workout_stats[key])
    
    if "weight training" in cats_lst:
        workout_stats["max_barbcurls"] = inpt("Please enter your max barabell curls:")
        workout_stats["max_barbsquats"] = inpt("Please enter your max barbell squats:")
        workout_stats["max_benchpressreps"] = inpt("Please enter your max bench press reps:")
        workout_stats["max_deadlifts"] = inpt("Please enter your max deadlifts:")
        workout_stats["max_barbspresses"] = inpt("Please enter your max barbell shoulder presses:")

        workout_stats["max_pullups"] = inpt("Please enter your max pullups:")
        workout_stats["max_chinups"] = inpt("Please enter your max chinups:")
        workout_stats["max_muscleups"] = inpt("Please enter your max muscle ups:")
        workout_stats["max_ktes"] = inpt("Please enter your max knee to elbow reps:")
        workout_stats["max_hkrs"] = inpt("Please enter your max hanging knee raises:")

        workout_stats["max_onearmcurls"] = inpt("Please enter your max one arm bicep curls:")
        workout_stats["max_flyes"] = inpt("Please enter your max flyes:")
        workout_stats["max_frsquats"] = inpt("Please enter your max front squats:")
        workout_stats["max_splitters"] = inpt("Please enter your max splitters:")
        workout_stats["max_latwalks"] = inpt("Please enter your max lateral walk reps:")

        workout_stats["max_bcurls"] = inpt("Please enter your max bicep curls:")
        workout_stats["max_tcurls"] = inpt("Please enter your max tricep curls:")
        workout_stats["max_spresses"] = inpt("Please enter your max shoulder presses:")
        workout_stats["max_cpresses"] = inpt("Please enter your max chest presses:")
        workout_stats["max_lraises"] = inpt("Please enter your max lateral raises:")
        for i in workout_stats:
            i = int(i)
    

    
    


    name_file = name + ".csv"


    with open(name_file, "w") as f:
        f.write(name+"\n")
        f.write(str(cats_lst)[1:-1]+"\n")
        f.write(str(equipment_list)[1:-1]+"\n")
        if "running" in cats_lst:
            f.write(targ_dist + "," + max_dist + "," + str(int(avg_pace)) + "," + str(((avg_pace*60) % 60)) + "," + str(max_sprint) + "\n")

        f.write("current_plank_mins," + current_plank["mins"] + "\n")
        f.write("current_plank_secs," + current_plank["secs"] + "\n")

        for key in workout_stats:
            f.write(key + "," + str(workout_stats[key]) + "\n")
