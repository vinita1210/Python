Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

from decimal import Decimal
if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    
score=[]
for i in student_marks:
    if i == query_name:
        score = student_marks.get(i)
        sum_score = 0.00
        c=0
        for i in score:
            k = "{:.2f}".format(i)
            sum_score = sum_score + float(k)
            c=c+1
        break
    else:
        continue
main_score=float("{:.2f}".format(sum_score))
sol = main_score/c
main_sol="{:.2f}".format(sol)
print(main_sol)
