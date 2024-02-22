import os
import csv

budget_data = os.path.join("Resources","budget_data.csv")

# Track various financial parameters
date = 1
month_of_change = []
gr_mth_change = []
lst_mth_change = []
net_change_list = []
total_pl = 0
change_pl = 0
date_int = 0
greatest_pl = 0
least_pl = 0

with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

    csv_header = next(csvreader)
    first_row = next(csvreader)

    total_pl += int(first_row[1])
    prev_net = int(first_row[1])

    for row in csvreader:
        # Track the total
        date += 1
        total_pl += int(row[1])
        # Track the net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]]

        if net_change > greatest_pl:
            greatest_pl = net_change
            gr_mth_change = row[0]
        elif net_change < least_pl:
            least_pl = net_change
            lst_mth_change = row[0]

    average_change = sum(net_change_list) / len(net_change_list)

    print("Financial Analysis")
    print(' ')
    print('-------------------------------------')
    print(' ')
    print(f'Total moonths: {date}')
    print(' ')
    print(f'Total:  ${total_pl}')
    print(' ')
    print(f'Average Change: ${average_change:.2f}')  
    print(' ')
    print(f'Greatest Increase In Profits: {gr_mth_change} (${greatest_pl})')
    print(' ')
    print(f'Greatest Decrease In Profits: {lst_mth_change} (${least_pl})')

    output_path = os.path.join("Analysis", "pybank_results.csv")
    with open(output_path, 'w') as csvfile:

        csvwriter = csv.writer(csvfile, delimiter=',')

        csvwriter.writerow(["Financial Analysis"])
        csvwriter.writerow([' '])
        csvwriter.writerow(['------------------------------------------------------------'])
        csvwriter.writerow([' '])
        csvwriter.writerow([f'Total moonths: {date}'])
        csvwriter.writerow([' '])
        csvwriter.writerow([f'Total:  ${total_pl}'])
        csvwriter.writerow([' '])
        csvwriter.writerow([f'Average Change: ${average_change:.2f}'])
        csvwriter.writerow([' '])
        csvwriter.writerow([f'Greatest Increase In Profits: {gr_mth_change} (${greatest_pl})'])
        csvwriter.writerow([' '])
        csvwriter.writerow([f'Greatest Decrease In Profits: {lst_mth_change} (${least_pl})'])
       
