# impot libraries
import os
import csv

# create and define all varibles needed
totalMonths = 0
totalRevenue = 0
avgRevenueChange = 0
greatestRevIncDate = "Date1"
greatestRevIncAmt = 0
greatestRevDecDate = "Date2"
greatestRevDecAmt = 0
totalRevenueChange = 0
prevRevenue = 0

csvpath = os.path.join("data","budget_data.csv")
#print(csvpath)
with open(csvpath, newline='') as bankdata:
    #skip the header row
    bankdata.readline()

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(bankdata, delimiter=',')

    #  Each row is read as a row
    for row in csvreader:
        print(row)
        totalRevenue = totalRevenue + int(row[1])
        totalMonths = totalMonths +1
        revIncrease = int(row[1]) - prevRevenue
        totalRevenueChange = totalRevenueChange + revIncrease
        prevRevenue =  int(row[1])

        #firgure the math
        if(revIncrease > greatestRevIncAmt):
             greatestRevIncAmt = revIncrease
             greatestRevIncDate = row[0]
        
        if(revIncrease < greatestRevDecAmt):
            greatestRevDecAmt = revIncrease
            greatestRevDecDate = row[0]

#figure the math
avgRevenueChange = round(totalRevenueChange/totalMonths,2)

#create and open output file to write resuts to
outputpath = os.path.join("Output","Results.txt")

lines = []
    
resultsfile = open(outputpath, "w")
    
#create the output
lines.append("Financial Analysis")
lines.append("----------------------------")
lines.append("Total Months: "+str(totalMonths))
lines.append("Total Revenue: $" + str(totalRevenue))
lines.append("Average Revenue Change: $"+str(avgRevenueChange))
lines.append("Greatest Increase in Revenue: "+greatestRevIncDate + " ($" + str(greatestRevIncAmt) +")")
lines.append("Greatest Decrease in Revenue: "+greatestRevDecDate + " ($" + str(greatestRevDecAmt) +")")

 ##Write the output to file and console
for line in lines:
    print(line)
    print(line,file=resultsfile)
        
#new line
print()
    
#close the file
resultsfile.close()