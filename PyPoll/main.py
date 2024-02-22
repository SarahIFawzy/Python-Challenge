import os
import csv

election_data = os.path.join("Resources","election_data.csv")

candidate_count = {}
total_votes = 0
name_1 = []
name_2 = []
name_3 = []
count_1 = []
count_2 = []
count_3 = []

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

    csv_header = next(csvreader)

    for row in csvreader:
        candidate = row[2]
        total_votes += 1
        
        if candidate in candidate_count:
            candidate_count[candidate]=candidate_count[candidate]+1
        else:
            candidate_count[candidate]=1

    keys = str(candidate_count.keys())
    values = str(candidate_count.values())

    split_keys = keys.split(", ")
    split_keys = str(split_keys).split("'")

    name_1.append(split_keys[1])
    name_1=str(name_1)[2:]
    name_1=str(name_1)[:-2]
    name_2.append(split_keys[3])
    name_2=str(name_2)[2:]
    name_2=str(name_2)[:-2]
    name_3.append(split_keys[5])
    name_3=str(name_3)[2:]
    name_3=str(name_3)[:-2]

   
    split_values = values.split(", ")
    # split_values = str(split_values).split("'")
   
    count_1.append(split_values[0])
    count_1=str(count_1)[15:]
    count_1=str(count_1)[:-2]
    count_2.append(split_values[1])
    count_2=str(count_2)[2:]
    count_2=str(count_2)[:-2]
    count_3.append(split_values[2])
    count_3=str(count_3)[2:]
    count_3=str(count_3)[:-4]

    name_1_prct = round(int(count_1)/int(total_votes)*100,3)
    name_2_prct = round(int(count_2)/int(total_votes)*100,3)
    name_3_prct = round(int(count_3)/int(total_votes)*100,3)

    winner = name_1
    if int(count_2) > int(count_1) and int(count_2) > int(count_3):
        winner = name_2
    elif int(count_3) > int(count_1) and count(count_3) > count(count_2):
        winner = name_3

    print('Election Results')
    print(' ')
    print('------------------------------------')
    print(' ')
    print(f"Total Votes: {total_votes}")
    print(' ')
    print('------------------------------------')
    print(' ')
    print(f'{name_1}: {name_1_prct}% ({count_1})')
    print(' ')
    print(f'{name_2}: {name_2_prct}% ({count_2})')
    print(' ')
    print(f'{name_3}: {name_3_prct}% ({count_3})')
    print(' ')
    print('------------------------------------')
    print(' ')
    print(f'Winner: {winner}')
    print(' ')
    print('------------------------------------')
  
    output_path = os.path.join("Analysis", "pypoll_results.csv")
    with open(output_path, 'w') as csvfile:

        csvwriter = csv.writer(csvfile, delimiter=',')

        
        csvwriter.writerow(['Election Results'])
        csvwriter.writerow([' '])
        csvwriter.writerow(['------------------------------------'])
        csvwriter.writerow([' '])
        csvwriter.writerow([f"Total Votes: {total_votes}"])
        csvwriter.writerow([' '])
        csvwriter.writerow(['------------------------------------'])
        csvwriter.writerow([' '])
        csvwriter.writerow([f'{name_1}: {name_1_prct}% ({count_1})'])
        csvwriter.writerow([' '])
        csvwriter.writerow([f'{name_2}: {name_2_prct}% ({count_2})'])
        csvwriter.writerow([' '])
        csvwriter.writerow([f'{name_3}: {name_3_prct}% ({count_3})'])
        csvwriter.writerow([' '])
        csvwriter.writerow(['------------------------------------'])
        csvwriter.writerow([' '])
        csvwriter.writerow([f'Winner: {winner}'])
        csvwriter.writerow([' '])
        csvwriter.writerow(['------------------------------------'])