#HOW TO USE: Pass in the name of the profile you want to read, this file must exist
#This will then return a dictionary of the persons information in the following format:
#{name: NAME, categories: [LIST OF CATEGORIES], equipment: [LIST OF EQUIPMENT]
#running: {targ_dist: TARGET_DISTANCE, max_dist: CURRENT_MAX_DISTANCE, avg_pace: AVERAGE_PACE}}

def read_profile(name):
    profile = {}
    filename = name + ".csv"


    with open(filename, "r") as f:
        for index, line in enumerate(f):
            if index == 0:
                profile["name"] = line[:-1]
            elif index == 1:
                profile["categories"] = line.split(",")
                profile["categories"][-1] = profile["categories"][-1][:-1]
                for num, ctgry in enumerate(profile["categories"]):
                    profile["categories"][num] = (profile["categories"][num]).replace("'", "")
                    profile["categories"][num] = (profile["categories"][num]).strip()
            elif index == 2:
                profile["equipment"] = line.split(",")
                profile["equipment"][-1] = profile["equipment"][-1][:-1]
                for num, eqpmt in enumerate(profile["equipment"]):
                    profile["equipment"][num] = (profile["equipment"][num]).replace("'", "")
                    profile["equipment"][num] = (profile["equipment"][num]).strip()
            elif index == 3 and line.split(",")[0] != "current_plank_mins":
                profile["running"] = {}
                profile["running"]["distance"] = {}
                profile["running"]["avg_pace"] = {}
                profile["running"]["sprint"] = {}
                for ind, element in enumerate(line.split(",")):
                    if ind == 0:
                        profile["running"]["distance"]["targ_dist"] = int(element)
                    elif ind == 1:
                        profile["running"]["distance"]["max_dist"] = int(element)
                    elif ind == 2:
                        profile["running"]["avg_pace"]["mins"] = int(float(element))
                    elif ind == 3:
                        profile["running"]["avg_pace"]["secs"] = int(float(element))
                    elif ind == 4:
                        profile["running"]["sprint"]["distance"] = int(element)

            elif index > 3:
                lne = line.split(",")
                profile[lne[0]] = lne[1][:-1]

    return(profile)
