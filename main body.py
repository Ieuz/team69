def main(users):
 
    print("Welcome to the fitness tracker 3000!")
    
    user = login()
    
    cont = "Y"
    while cont == "Y":
                
        print("Please enter a command or type 'HELP' for a list of commands.")
        commands = {"HELP":"Lists all commands", "QUIT": "Quits the program"}
        inp = input(">>>")
        
        #try:
        if inp.upper() == "BODYWEIGHT":
            bodyweight(users["Ieuan"]["max_exercises"], users["Ieuan"]["difficulty"])
        elif inp.upper() == "CARDIO":
            cardio_workout(users["Ieuan"]["max_exercises"], users["Ieuan"]["difficulty"])
        elif inp.upper() == "HELP":
            print("Here is a list of all commands:")
            for command in commands:
                print(command, ":", commands[command])

        elif inp.upper() == "QUIT":
            print("See you next time!")
            break

        else:
            assert False
            
        #except error as e:
            #print("Program error, please try again.", e)
    
    

main(users)
