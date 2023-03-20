import time

def temps():
    heures = int(input("heures : "))
    minutes = int(input("minutes : "))
    secondes = int(input("secondes : "))

    
    while heures<24:     
        while minutes<60:
            
            if minutes < 60:
                minutes = minutes+1
            
            if secondes<60:
                
                if secondes < 60:
                    secondes = secondes+1
                print(heures,':',minutes,':',secondes)
            
            if heures > 60 :
                heures = heures+1
temps()

#  Fonction pour l'heure
 








# alarmeh = int(input("alarme h : "))
    # alarmem = int(input("alarme m : "))
    # alarmes = int(input("alarme s : "))



# if alarmeh == heures:
                #     if alarmem == minutes:
                #         if alarmes == secondes:
                #             print("debout")

















