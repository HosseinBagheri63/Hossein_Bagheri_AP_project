import csv
std_dict_list=[]
try:
    with open('std_info_4042.txt', 'r') as f:
        headers= [h.strip() for h in f.readline().split(',')]
        for line in f:
            student=[s.strip() for s in line.split(',')]
            std_dict_list.append(dict(zip(headers, student)))
except FileNotFoundError:
    print('File not found')
with open('std_info_4042.csv', 'w' , newline='') as csvfile:
    writer = csv.DictWriter(csvfile, headers)
    writer.writeheader()
    for std in std_dict_list:
        writer.writerow(std)
    