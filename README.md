# Python Challenge
## General Description
This repository includes two Python projects: PyBank and PyPoll. These projects use several Python functionalities for data analysis such as:
- Reading a CSV file
- Manipulating data from the CSV file
- The use of arrays and dictionaries
- Writing text files
### PyBank Project
#### Main Objective
This project analyzes the financial records of a company. The financial data is included in the Resources folder and is called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses. The program is called main and calculates the following information:
- Total number of months included in the dataset
- Net total amount of "Profit/Losses" over the entire period
- Average of the changes in "Profit/Losses" over the entire period
- The greatest increase in profits over the entire period (Date and Amount)
- The greatest decrease in profits over the entire period (Date and Amount)

Once the calculations are done, the program prints the results to the terminal and creates a text file called bank_results.txt with the results of the calculations. This file is included the Analysis folder. 
#### Structure
The program can be divided into 3 parts:

The first part is about reading the CSV file. For this, the os and csv libraries were imported. Each line was read using a for loop.
The second part focuses on the calculations based on the retrieved data in each iteration of the for loop:
- An if statement to initiliaze the variables for the first iteration
- there is a counter to get the total of months included in the dataset: **month_counter**
- **total_balance** adds all the values of the "Profit/Losses" column 
- **change** calculates the change in balance versus the last balance value
- An if statement to verify if the "Profit/Losses" value that is being analyzed is greater or less than the ones archived in two arrays: **increase** and **decrease**. These arrays include the date and profit/loss information.
- Finally the average change **avg_chg** is calculated with all the information collected from the file
The third part is the displaying of the information:
- print statement that shows the results in the terminal
- a text file called bank_results.txt is created using the same message

### PyPoll Project
#### Main Objective
This project analyzes the poll data gathered during the voting process of a small rural town. The poll data is included in the Resources folder and is called election_data.csv. The dataset is composed of three columns: Voter ID, County and Candidate. The program is called main and calculates the following information:
- The total number of votes cast
- A complete list of candidates who received votes
- The percentage of the votes each candidate won
- The total number of votes each candidate won
- The winner of the election based on popular vote

Once the calculations are done, the program prints the results to the terminal and creates a text file called poll_results.txt with the results of the calculations. This file is included the Analysis folder. 
#### Structure
The program can be divided into 3 parts:

The first part is about reading the CSV file. For this, the os and csv libraries were imported. Each line was read using a for loop.
The second part focuses on the calculations based on the retrieved data in each iteration of the for loop:
- An if statement to initiliaze the variables for the first iteration
- A dictionary **poll_dic** is used to concentrate the candidates and their votes
- An if statement is used to verify if the candidate is already included in the **poll_dic**. If it is then, a new vote is added to that candidate, if not the candidate name is added to the dictionary
- Once the dictionary is filled with the election data. A for loop is used to retrieved the results and create the message **final_msg** that is going to be displayed.
The third part is the displaying of the information:
- print statement that shows the results in the terminal
- a text file called poll_results.txt is created using the same message

### General Considerations
The **bold** characters refer to the name of the variables used in the programs
