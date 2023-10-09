import csv

file_loc = 'data\pb_num_2010_oct_2023.csv'
lotto_check = {}
power_check = {}

def format_lotto_list(csv_file):
    temp_lst = []

    with open(csv_file, newline='') as csvfile:
        lottoreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in lottoreader:
            temp_lst.append(row[1])

    lotto_num_list = [] 

    for win_num in temp_lst[1:]:
        words = win_num.split(' ')
        lotto_num_list.append(words)

    return lotto_num_list

def instance_count():
    lotto_file = format_lotto_list(file_loc)
    count = 0

    for lst in lotto_file:
        #print(lst)
        for num in lst:
            if count == 5:
                var_check = power_check
                count = 0
            else:
                var_check = lotto_check
                count += 1
            
            if num in var_check:
                var_check[num] += 1
            else:
                var_check[num] = 0
               
            #print(num)
    sort_dict(lotto_check)
    sort_dict(power_check)

def sort_dict(dict_file):
    my_keys = list(dict_file.keys())
    my_keys.sort()
    sorted_dict = {i: dict_file[i] for i in my_keys}

    print(sorted_dict)

instance_count()
#print(lotto_check)
