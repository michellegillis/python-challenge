import os
import csv

budgetdata = os.path.join("Resources", "budget_data.csv")
with open(budgetdata) as csvfile:
    #csv.reader = object from csv import to read csv
    csvreader = csv.reader(csvfile, delimiter=",")
    firstrow = next(csvreader)
    previousval = int(firstrow[1])
    totalchange = 0
    totalmonths = 0
    totalprofit = 0
    profitchange = []
    for row in csvreader:
        #sum profits
        totalprofit += int(row[1])
        totalmonths += 1
        totalchange = totalchange + int(row[1]) - previousval
        previousval = int(row[1])
        profitchange.append(totalchange)
        profitinc = max(profitchange)
        profitdec = min(profitchange)
    print("Financial Analysis")
    print("Total Months: " + str(totalmonths))
    print("Total: $" + str(totalprofit))
    print("Average Change: " + str(totalchange/totalmonths))
    print("Greatest Increase: " + str(profitinc))
    print("Greatest Decrease: " + str(profitdec))

write_file = open(os.path.join("analysis", "pybankoutput.txt"), 'w+')
write_file.write("Financial Analysis\n")


     
        
   
    

   
    
    
    
            
    






