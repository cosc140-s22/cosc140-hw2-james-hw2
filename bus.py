#######################################################
#
# COSC 140 Homework 2, "bus trip planner" problem
#
#######################################################

def main():
    departureTime = input("Please enter a departure time in HH:MM ")
    distance = float(input("How far do you need to travel in Km? "))
    stops = input("How many stops are there along the way? ")
    newHours = 0
    newMinutes = 0

    departureList = departureTime.split(":")
    hours = departureList[0]
    minutes = departureList[1]

    if hours[0] == "0":
        hours = hours[1]
    if minutes[0] == "0":
        minutes = minutes[1]

    hours = int(hours)
    minutes = int(minutes)

    travelTime = ((distance / 40.0) * 3600) + (int(stops) * 30) #time in seconds to travel
    travelHours = travelTime // 3600 #hours to travel
    travelTime = round(travelTime - (travelHours * 3600)) #account for some weird 
    travelMinutes =  travelTime // 60 #minutes of travel
    travelSeconds = round(travelTime - (travelMinutes * 60)) #seconds of travel


    if (minutes + travelMinutes) > 60:
        if int(((minutes + travelMinutes) // 60) + travelHours + hours) > 24:
            newHours = int(((minutes + travelMinutes) // 60) + travelHours + hours) - (newHours % 24)
            newMinutes =  int((minutes + travelMinutes) % 60)
            if newMinutes == 60:
                newMinutes = 0
                newHours+=1
        elif int(((minutes + travelMinutes) // 60) + travelHours + hours) == 24:
             newHours = 0
             newMinutes =  int((minutes + travelMinutes) % 60)
        else:
            newHours = int(((minutes + travelMinutes) // 60) + travelHours + hours)
            newMinutes =  int((minutes + travelMinutes) % 60)
            if newMinutes == 60:
                newMinutes = 0
                newHours+=1
    else:
        newMinutes = int((minutes + travelMinutes))
        newHours = int(travelHours + hours)
        if newMinutes == 60:
                newMinutes = 0
                newHours+=1
        if newHours > 24:
            newHours = newHours % 24
        elif newHours == 24:
            newHours = 0

    if newHours < 10:
        newHours = "0" + str(newHours)
    if newMinutes < 10:
        newMinutes = "0" + str(newMinutes)
    travelSeconds = int(travelSeconds)
    if travelSeconds == 0:
        travelSeconds = "00"
    
    print("Arrival time: " + str(newHours) + ":" + str(newMinutes) + ":" + str(travelSeconds))
    


    

if __name__ == "__main__":
    main()


