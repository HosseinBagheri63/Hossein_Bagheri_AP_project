scores_sum=0
count=0 
score=''
bad_string='\t \n \\ | /'
with open(r"C:\beta\alfa.dat") as scores:
    while True:
        char=scores.read(1)
        if not char:
            if score:
                scores_sum=scores_sum+float(score)
                count=count+1
            break
        elif char in bad_string:
            if score:
                scores_sum=scores_sum+float(score)
                count=count+1
            score=''
        else:
            score=score+char
if count!=0:
    average=scores_sum/count
else:
    print('no scores')
    exit()

score=''
least_diff=float('inf')
with open(r"C:\beta\alfa.dat") as scores:
    while True:
        char=scores.read(1)
        if not char:
            if score:
                if abs(float(score)-average)<least_diff:
                    least_diff=abs(float(score)-average)
                score=''
            break
                
        elif char in bad_string:
            if score:
                if abs(float(score)-average)<least_diff:
                    least_diff=abs(float(score)-average)
                score=''
        else:
            score=score+char

scores = open(r"C:\beta\alfa.dat")
new_scores = open(r"C:\beta\alfa_new.dat","w")
score=''
while True:
    char=scores.read(1)
    if not char:
        if score!='':
            if abs(float(score)-average)==least_diff:
                new_scores.write(score+'*')
            else:
                new_scores.write(score)
        break
    elif char in bad_string:
        if score!='':
            if abs(float(score)-average)==least_diff:
                new_scores.write(score+'*'+char)
            else:
                new_scores.write(score+char)
            score=''
        else:
            new_scores.write(char)
    else:
        score=score+char
scores.close()
new_scores.close()