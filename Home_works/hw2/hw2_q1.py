n = int(input('number of students: '))
students_1400=[]
students_1401=[]
for i in range(n):
    print('information of student ',i+1)
    name = input('name: ')
    while True:
        try:
            year = int(input('the year of entering: '))
        except ValueError:
            print('year must be a number')
            continue
        if year == 1400 or year==1401:
            break
        else:
            print('year must be 1400 or 1401')
    while True:
        try:
            score1= float(input('score of first lesson: '))
            break
        except ValueError:
            print('score must be a number')
    while True:
        try:
            score2= float(input('score of second lesson: '))
            break
        except ValueError:  
            print('score must be a number')
    while True:
        try:
            score3= float(input('score of third lesson: '))
            break
        except ValueError:
            print('score must be a number')
    average = (score1+score2+score3)/3
    if year==1400:
        students_1400.append([name,score1,score2,score3,average])
    else:
        students_1401.append([name,score1,score2,score3,average])
with open('1400.txt','w') as f:
    for student in students_1400:
        f.write(f'{student[0]}\t{student[1]}\t{student[2]}\t{student[3]}\t{student[4]:.2f}\n')
with open('1401.txt','w') as f:
    for student in students_1401:
        f.write(f'{student[0]}\t{student[1]}\t{student[2]}\t{student[3]}\t{student[4]:.2f}\n')