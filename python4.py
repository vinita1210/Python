list_main=[]

def append(list1,value):
    list1.append(value)
    
def insert_val(list1,index,value):
    list1.insert(index,value) 

def remove(list1,value):
    list1.remove(value) 

def sort(list1):
    list1.sort() 
   
def pop(list1):
    list1.pop() 
    
def print_val(list1):
    print(list1)  

def reverse(list1):
    list_main = list1.reverse()    
   
if __name__ == '__main__':
    N = int(raw_input())
    for _ in range(N):
        value = raw_input().split()
        #print value
        val1 = value[0]
        if val1 == 'insert':
            val2=int(value[1])
            val3=int(value[2])
            insert_val(list_main,val2,val3)
        elif val1 == 'print':
            print_val(list_main) 
        elif val1 == 'remove': 
            val2 = int(value[1])
            remove(list_main,val2)  
        elif val1 == 'append': 
            val2 = int(value[1])  
            append(list_main,val2)
        elif val1 == 'sort':
            sort(list_main) 
        elif val1 == 'pop':
            pop(list_main)
        elif val1 == 'reverse':
            reverse(list_main)
                



