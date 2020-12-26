There are  students in this class whose names and grades are assembled to build the following list:

python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

The lowest grade of 37.2 belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.


sol:

list1=[]
python_students=[]
for i in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    list1 = [name,score]
    python_students.append(list1)
      
def Sort(python_students):
    python_students.sort(key = lambda x :x[1])
    return python_students

Sort(python_students)    

var = python_students[0][1]

for i in python_students:
    if i[1] > var:
        second_max = i[1]
        break
    else:
        continue    
second_low=[]
for i in python_students:
    if i[1] == second_max:
        second_low.append(i)
    else:
        continue    

second_low.sort(key = lambda x:x[0])

for i in second_low:
    print i[0]
