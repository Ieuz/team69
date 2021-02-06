def inpt(ting):
    outpt = ""
    while outpt == "":
        outpt = input(ting)

    return outpt
        

def create_profile():
    categories = ["running", "indoor cardio", "weight training", "muscle groups", "bodyweight training", "core strength"]
    equipment = ["dumbells", "resistance band", "barbell", "pullup bar"]

    
    name = input("Please enter your name: ")
    print("Categories:\nrunning, indoor cardio,\nweight training,\nmuscle groups, bodyweight training,\ncore strength\n\n")
    print("Which categories of workout are you interested in? Please enter your answers as a list seperated by commas\n(In the format 'running,core strength,indoor cardio')")
    user_cats = input(">>>")
    user_cats_lst = user_cats.split(",")
    cats_lst = []
    ccl = False
    

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
        avg_pace = inpt("What is your average pace in minutes per kilometer?")


    print("Please enter which equipment you own from this list, seperated by commas:\ndumbells, resistance band,\nbarbell, pullup bar")
    user_eqip = input(">>>")
    user_eqip_lst = user_eqip.split(",")
    equipment_list = []
    

    for equipment_piece in user_eqip_lst:
        if equipment_piece in equipment:
            if equipment_piece not in equipment_list:
                equipment_list.append(equipment_piece)
        else:
            equip_piec = equipment_piece
            #print(equip_piec)
            #print(equip_piec in equipment)
            #print(equipment)
            while equip_piec not in equipment:
                ccl = False
                print(f"Equipment piece {equipment_piece} was not recognised, type the equipment you meant or type CANCEL to cancel")
                equip_piec = input(">>>")
                if equip_piec == "CANCEL" or equip_piec == "cancel":
                    ccl = True
                    break
            if ccl != True:
                equipment_list.append(equip_piec)

                
    current_plank = {}
    plankstats = ""
    while len(plankstats.split(",")) != 2:
        plankstats = inpt("Please enter how long you can do a plank for in the format mins,secs (i.e. '3,20'):")
    plankstats_lst = plankstats.split(",")
    current_plank["mins"] = plankstats_lst[0]
    current_plank["secs"] = plankstats_lst[1]
    workout_stats = {}
    workout_stats["max_pressups"] = inpt("Enter your max pressups:")
    workout_stats["max_squats"] = inpt("Enter your max squats:")
    workout_stats["max_situps"] = inpt("Enter your max situps:")
    workout_stats["max_running_time"] = inpt("Enter your max running time in seconds:")
    workout_stats["max_high_knees"] = inpt("Enter your max high knees time in seconds:")
    workout_stats["max_burpees"] = inpt("Enter your max burpees:")
    workout_stats["max_skaters"] = inpt("Enter your max skater time in seconds:")
    workout_stats["max_mountain_climbers"] = inpt("Enter your max mountain climber time in seconds:")
    workout_stats["max_up_down_plank"] = inpt("Enter your max up down plank time in seconds:")
    workout_stats["max_plank"] =(int(plankstats_lst[0])*60) + int(plankstats_lst[1])
    workout_stats["max_side_plank"] = inpt("Enter your max side plank time in seconds:")
    workout_stats["max_star_jumps"] = inpt("Please enter your max star jump time in seconds:")
    workout_stats["max_tuck_jumps"] = inpt("Please enter your max tuck jumps:")
    
    


    

    name_file = name + ".csv"


    with open(name_file, "w") as f:
        f.write(name+"\n")
        f.write(str(cats_lst)[1:-1]+"\n")
        f.write(str(equipment_list)[1:-1]+"\n")
        if "running" in cats_lst:
            f.write(targ_dist + "," + max_dist + "," + avg_pace + "\n")

        f.write("current_plank_mins," + current_plank["mins"] + "\n")
        f.write("current_plank_secs," + current_plank["secs"] + "\n")

        for key in workout_stats:
            f.write(key + "," + str(workout_stats[key]) + "\n")

create_profile()
