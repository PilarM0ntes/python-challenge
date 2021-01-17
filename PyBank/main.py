import os
import csv

#Assigns the path file
bank_path = os.path.join('Resources','budget_data.csv')

#Opens and reads the file
with open(bank_path, 'r') as bank_file:
    file_reader = csv.reader(bank_file, delimiter = ',')
    next(bank_file)
    
    #Initializes the variables that are needed for the calculations
    month_counter = 0 #Holds the number of months that are being analyzed
    total_balance = 0 #Holds the total balance of all analyzed months
    prev_balance = 0 #Holds the previous balance value
    change = 0 #Holds the changes over the entire period
    increase = [] #Holds the information of the greatest increase in profits
    decrease = [] ##Holds the information of the greatest decrease in profits

    for row in file_reader:
        #Assigns the 2 values of row in one variable each
        period = row[0]
        balance = int(row[1])
        
        #Checks if this is the first value. If so, it initializes the arrays that will contain the values
        #that will be used for comparison & assigns the first balance value
        if month_counter == 0:
            increase = [period, balance]
            decrease = [period, balance]
            prev_balance = balance

        change = (prev_balance -balance) + change #calculates the change in balance vs the last balance value
        month_counter = month_counter + 1
        total_balance = total_balance + balance
        prev_balance = balance #Saves the current balance for the next change calculation
        
        #Verifies if the current balance is less than the greatest decrease value registered
        if balance < decrease[1]:
            decrease = [period, balance]
        elif balance > increase[1]:
            increase = [period, balance]

#Calculates the average changes of the time period & formats it to 2 decimals
avg_chg = change/month_counter
avg_chg ="{:.2f}".format(avg_chg)

#Creates the final message
final_msg = 'Financial Analysis \n--------------------\n'
final_msg = final_msg + 'Total months: ' + str(month_counter) + '\n'
final_msg = final_msg + 'Total: $' + str(total_balance) + '\n'
final_msg = final_msg + 'Average change: $' + str(avg_chg) + '\n'
final_msg = final_msg + 'Greatest increase in profits: ' + str(increase[0]) + '($' + str(increase[1]) + ')\n'
final_msg = final_msg + 'Greatest decrease in profits: ' + str(decrease[0]) + '($' + str(decrease[1]) + ')\n'

#Prints the results in the terminal
print(final_msg)

#Creates a text file with the results
results_path = os.path.join('Analysis','bank_results.txt')

with open(results_path, 'w') as txtfile:
    txtfile.write(final_msg)



