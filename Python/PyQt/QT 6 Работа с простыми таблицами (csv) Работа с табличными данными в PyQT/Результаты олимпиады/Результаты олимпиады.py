import csv

school_num, class_num = input().split()
school_num = int(school_num)
class_num = int(class_num)

with open('rez.csv', 'r', encoding='utf-8') as file:
    data = list(csv.DictReader(file, delimiter=','))

result = {}

for row in data:
    cur_school_num = int(row['login'].split('-')[2].lstrip('0'))
    cur_class_num = int(row['login'].split('-')[3].lstrip('0'))

    if school_num == cur_school_num and class_num == cur_class_num:
        username = row['user_name'].rsplit(maxsplit=2)[1]
        score = row['Score']

        if int(score) not in result.keys():
            result[int(score)] = [username]
        else:
            result[int(score)].append(username)


for score, name in sorted(result.items(), key=lambda x: x[0], reverse=True):
    if len(name) > 1:
        rev_names_list = sorted(name, reverse=True)
        for n in rev_names_list:
            print(n, score)
    else:
        print(name[0], score)
