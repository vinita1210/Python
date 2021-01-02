class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #print(strs)
        output=''
        value=''
        if len(strs) != 0:
            min_len=len(strs[0])
        #print(min_len)
        for i in strs:
            if (len(i) < min_len):
                min_len = len(i)
                value = i
        #print(value)        
        #print(min_len)
        main_str = [x for x in strs if x != value] 
        #print(main_str)
        #print("value of length : " + str(len(main_str)) )
        if value != '':
            for i in range(min_len):
                #print(i)
                c=0
                val = value[i]
                for x in main_str:
                    if val in x[i]:
                        c= c+1
                    else:
                        break
                #print("value of c : " + str(c) )                      
                if c == len(main_str):            
                    output = output + value[i]            
        return output
           
