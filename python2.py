Given list is [2,3,6,6,5] . The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score.

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    
arr.sort()
max_val = arr[len(arr)- 1]

second_runner=[]

for i in arr:
    if i < max_val:
        second_runner.append(i)
    else:
        continue
max_val = second_runner[len(second_runner)- 1]
print(max_val)
