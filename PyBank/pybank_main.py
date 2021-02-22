"""
Created on Sat Feb 13 09:41:48 2021
PyBank_YangShi
@author: YangShi
"""
import os, csv

budget_csv=os.path.join('r','..','Resources','budget_data.csv')

month_count=0
budget_sum=0
budget_max=0    #max profit
budget_min=0    #max loss
output_txt=os.path.join("r","..", "analysis","budget_analysis.txt")

with open (budget_csv) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    csvheader=next(csvreader)       #find the header
    for row in csvreader:
        if float(row[1])>=budget_max:
            budget_max=float(row[1])       #record greatest gain
            month_max=row[0]        #record month with greatest gain
        if float(row[1])<=budget_min:       
            budget_min=float(row[1])       #record greatest loss
            month_min=row[0]        #record month with greatest loss
        month_count+=1              #find total number of months
        budget_sum=budget_sum+float(row[1])        #find total profit/losses
if month_count>0:
    budget_average=round(float(budget_sum/month_count),2)     #calc the average

#output to terminal 
print("Financial Analysis")
print("---------------------------------------")
print(f"Total months:  {month_count}")
print(f"Total $ {budget_sum}")
print(f"Average Change: $  {budget_average}")
print(f"Greatest Increase in Profits: $ {month_max} {budget_max}")
print(f"Greasted Decrease in Profits: $ {month_min} {budget_min}")
print("---------------------------------------")

#output to text file
with open (output_txt, "w") as text:
    text.write("Financial Analysis \n -------------------------------\n Total months: ")
    text.write(str(month_count))
    text.write("\n Total $" )
    text.write(str(budget_sum))
    text.write("\n Average Change: $" )
    text.write(str(budget_average))
    text.write("\n Greatest Increase in Profits: ")
    text.write(month_max)
    text.write("  ($")
    text.write(str( budget_max))
    text.write(") \n Greatest Decrease in Profits: ")
    text.write(month_min)
    text.write("  ($")
    text.write(str( budget_min))
    text.write(") \n -------------------------------")