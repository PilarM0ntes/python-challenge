import os
import csv

#Assigns the path file
vote_path = os.path.join('Resources', 'election_data.csv')

#Opens the file
with open(vote_path, 'r') as vote_file:
    file_reader = csv.reader(vote_file, delimiter = ',')
    next(vote_file) #Skips the headers

    #Initializes the files that are needed for the calculations
    total_votes = 0
    poll_dic = {}

    #Starts reading the file
    for row in file_reader:
        #Gets the candidates name
        candidate = row[2]
        #Calculates the number of votes
        total_votes = total_votes + 1
        #Verifies if the candidate is already in the dictionary
        if candidate in poll_dic:
            #Increases by 1 the number of stored votes
            votes = poll_dic[candidate] + 1
            poll_dic[candidate] = votes
        else:
            #Adds the candidate to the poll_dic
            poll_dic[candidate] = 1

#Creates the string that will be printed
final_msg = 'Election Results \n--------------------\n'
final_msg = final_msg + 'Total votes: ' + str(total_votes) + '\n'
final_msg = final_msg + '--------------------\n'

#Calculates the result of the polls
first_it = True
prev_val = 0
winner = ''

for key,val in poll_dic.items():
    percent = "{:.3f}".format((val/total_votes) *100)
    final_msg = final_msg + key + ': ' + str(percent) +'% ('+str(val)+')\n'
    if first_it == True:
        prev_val = val
        winner = key
        first_it = False
    elif val > prev_val:
        prev_val = val
        winner = key

#Includes the winner in the message
final_msg = final_msg + '--------------------\nWinner: '
final_msg = final_msg + winner + '\n--------------------'

#Prints the result in the terminal
print(final_msg)

#Creates a text file with the results
results_path = os.path.join('Analysis','poll_results.txt')

with open(results_path, 'w') as txtfile:
    txtfile.write(final_msg)