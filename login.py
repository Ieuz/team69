def read_profile(name):
    users = {}
    users["Ieuan"] = {"max_exercises":{"current_plank":{"mins":2, "secs":40},
        "max_pressups":30, "max_squats":15,
        "max_situps":30, "max_tuck_jumps":12,
        "max_star_jumps":30, "max_side_plank":2,
        "max_plank":2, "max_up_down_plank":2, "max_mountain_climbers":45,
        "max_skaters":45, "max_burpees":25, "max_high_knees":50, "max_running_time":30,
                                 }, "difficulty":2}
    return users[name]

def login():
    cont = True
    
    while cont:
        print("Would to log in or sign up?")
        login_bool = input(">>>")
        
        if login_bool.lower() == "sign up":
            create_profile()
            cont = False
            
        elif login_bool.lower() == "log in":
            logging_in = True
            while logging_in:
                try: 
                    print("What is your profile name?")
                    profile_name = input(">>>")
                    user = read_profile(profile_name)
                    logging_in = False
                    cont = False
                    return user
                except:
                    print("This profile name does not exist. Please try again.")
        else:
            print("This is not a valid input. Please type 'log in' or 'sign up'.")
