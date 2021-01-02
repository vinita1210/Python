class Solution:
    def reverse(self, x: int) -> int:
        print(x)
        no = str(x)
        max_len = len(str(x))
        #print(max_len)
        value=''
        if x > 0 :
            for i,val in enumerate(str(x)):
                #print(val)
                #print(i)
                value=value + no[max_len - (i+1)]
                value.lstrip('0')        
        elif x<0 :
            value = value + no[0]
            for i,val in enumerate(no[1:]):
                value=value + no[max_len - (i+1)]
                    
            value = value[0] + value[1:].lstrip('0')
        else:
            value = x
            
        if abs(int(value)) >= 2**31:     
            return 0
        else: 
            return int(value)
