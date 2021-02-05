def main():
 
    print("Welcome to the fitness tracker 3000!")
    
    login()
    
    users = {}
    users["Ieuan"]  = {"equipment":["dumbells"],
                       "max_exercises":{"current_plank":{"mins":2, "secs":40}
                                      , "max_pressups":30, "max_squats":15
                                      , "max_situps":30},
                      "difficulty":2}
    cont = "Y"
    while cont == "Y":
                
        print("Please enter a command or type 'HELP' for a list of commands.")
        commands = {"HELP":"Lists all commands", "QUIT": "Quits the program"}
        inp = input(">>>")
        
        try:
            if inp.upper() == "BODYWEIGHT":
                bodyweight(users["Ieuan"]["max_exercises"], users["Ieuan"]["difficulty"])
            elif inp.upper() == "HELP":
                print("Here is a list of all commands:")
                for command in commands:
                    print(command, ":", commands[command])

            elif inp.upper() == "QUIT":
                print("See you next time!")
                break

            else:
                assert False
            
        except:
            print("Program error, please try again.")
    
    

main()
