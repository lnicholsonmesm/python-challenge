'''
- The total number of months included in the dataset
- The net total amount of "Profit/Losses" over the entire period
- The average of the changes in "Profit/Losses" over the entire period
- The greatest increase in profits (date and amount) over the entire period
- The greatest decrease in losses (date and amount) over the entire period
'''

#**************************
# Step 1: Import CSV
#**************************

import csv
import os #use to find the file

budget = [] #my csv file will become a list of lists

csvpath = os.path.join('Resources', 'budget_data.csv') #variable-ify the relative file path

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    budget_headers = next(csvreader)
    for variable_that_is_a_row_list in csvreader:
        budget.append(variable_that_is_a_row_list) #append each row to a list (budget)


#print(budget_headers + budget[0:3])


# (thingamabob for thingamabob in budget)
#for rowchunk in budget:
##print(budget[0][0])
#print(budget[:][0][0])
#print(budget[0])

sign = "uncalculated"
dates = []
moneys = []

for piece in range(0, len(budget), 1):
    dates.append(budget[piece][0])
    moneys.append(budget[piece][1])

# print(dates)
# print(moneys)
moneys = [float(money) for money in moneys]
# Calculate total Profit/Losses
revenue = sum(moneys) #revenue is the sum of monies
#print(revenue)

num_months = len(dates)

if revenue > 0:
    sign = "positive"
    revenuetype = "profit"
elif revenue < 0:
    sign= "negative"
    revenuetype = "loss"
elif revenue == 0:
    sign = "zero"
    revenuetype = 'earnings'
    pass

#if sum([float(money) for money in moneys]) 
# print(revenue)

#i'm gonna get columns--I could take each row and pick the first value (second, third) from it, but that will be at least if not more work than keeping each row as a thing

# Calculate change in Profit/Losses over period; find average
#the change in profits are assumed to be the values reported. in the first month, there was, for example (and not in reality), a $5 profit recorded. In month two there was a $10 loss. so the change in revenue...so am i taking the difference of each month and then average it??

#this makes no sense. like what the hell is this data. what am i even doing. but at least i'm doing more complicated math here, i guess. more complicated coding.....

#num_months = # of months; may cause off by 1 error

#print(moneys)
mom_delta = [] #monthovermonth delta. aka yo mama.

for counterbit in range(0, len(moneys)-1):
    mom_delta.append(moneys[counterbit+1] - moneys[counterbit])

avg_change = sum(mom_delta)/len(mom_delta)

# for chunk in moneys:
# Find max change in profits (increase)
max_delta = max(mom_delta)
# Find max change in profits (decrease)
min_delta = min(mom_delta)
corresponding_months = dates[1:]
increase_month = corresponding_months[mom_delta.index(max_delta)]
decrease_month = corresponding_months[mom_delta.index(min(mom_delta))]

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {num_months}")
print(f"Total: ${revenue:.2f}")
print(f"Greatest Increase in Profits: {increase_month} (${max_delta:.2f}) \nGreatest Decrease in Profits: {decrease_month} (${min_delta:.2f}) \n")

print(f"Revenues for our company were {sign}; profit and loss totals across months summed to a net {revenuetype} of ${revenue:.2f}, with an average change of ${avg_change:.2f}. The greatest net positive change in profits were in {increase_month} at a profit of ${max_delta:.2f} and the greatest decrease in profits resulted in {decrease_month} with a net loss of ${min_delta:.2f}.")

#create a file in a place with a name
#f = open('FinancialAnalysis.txt', 'w') this would make the file

filepath = os.path.join('Analysis', 'analysis.txt') 
f = open(filepath, 'w')
f.writelines(
    [
        "Financial Analysis\n", 
        "----------------------------\n",
         f"Total Months: {num_months}\n",
         f"Total: ${revenue:.2f}\n",
         f"Greatest Increase in Profits: {increase_month} (${max_delta:.2f}) \nGreatest Decrease in Profits: {decrease_month} (${min_delta:.2f})\n\n",
         f"Revenues for our company were {sign}; profit and loss totals across months summed to a net {revenuetype} of ${revenue:.2f}, with an average change of ${avg_change:.2f}. The greatest net positive change in profits were in {increase_month} at a profit of ${max_delta:.2f} and the greatest decrease in profits resulted in {decrease_month} with a net loss of ${min_delta:.2f}."
    ]
)
f.close()
