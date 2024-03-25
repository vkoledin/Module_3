import os
import csv

budget_data_csv=os.path.join("Resources/budget_data.csv")
budget_file= budget_data_csv

financial_analysis = []
total_months = []
total = []
change_list = []
greatest_increase = []
greatest_decrease = []
count=1

with open(budget_data_csv, 'r') as budget_file:
    csv_reader=csv.reader(budget_file)
    header=next(csv_reader)
    for row in csv_reader:
        #print(row)
        total_months.append(row[0])
        total.append(int(row[1]))
        if count>1:
            change=int(row[1])- previous_value
            change_list.append(change)
        count=count+1
        previous_value=int(row[1])



#print(len(total_months))    
#print(sum(total))
avarage_change=round(sum(change_list)/len(change_list),2)
#print(avarage_change)
greatest_increase = ["",0]
greatest_decrease = ["",9999999999]

if  count > 1:
    change=int(row[1])-previous_value
    change_list.append(change)
for change in change_list:
    if  change>greatest_increase[1]:
        
        greatest_increase[1] = change
    if  change<greatest_decrease[1]:
        
        greatest_decrease[1]= change
        change=int(row[1])
        count+=1

output=(
f"Financial Analysis\n"
f"----------------------------\n"
f"Total Months: {len(total_months)}\n"
f"Total: ${sum(total)}\n"
f"Average Change: ${avarage_change}\n"
f"Greatest Increase in Profits:{greatest_increase[1]}\n"
f"Greatest Decrease in Profits:{greatest_decrease[1]}" 
)
print(output)
output_txt=os.path.join("analysis/budget_analysis.txt")
with open(output_txt, 'w') as output_file:
    output_file.write(output)



    




    

    