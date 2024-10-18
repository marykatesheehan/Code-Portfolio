#Mary Kate Sheehan
#10/11/2023
#Nested loops for printing digital clock

#Hours loop:
for hours in range(24): #One repetition and wait for minutes loop and seconds loop to finish
    #Minutes loop
    for minutes in range(60): #One repetition and wait for seconds loop to finish
        #Seconds loop
        for seconds in range(60):
            print(hours, ":", minutes, ":", seconds)
