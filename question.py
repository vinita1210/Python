Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Input: s = "3[a2[c]]"
Output: "accaccacc"

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"

sol:


def decodeString(s):
    d =0
    start = 0
    c=0
    print(s)
    value = ''
    close_index=0
    for i in range(len(s)):
        d = 0
        if s[i] == '[':
            
            if start == 0:
                value = value + s[0:i-1]
            
            #print b
            if c == 0 :
                if close_index == 0:
                    b = s[i-1]
                    start_index = i + 1
                    #print ("start_index:" +  str(start_index))
                    #d=0
                    start+=1
                else:
                    b = s[i -1]
                    #print "else" + str(close_index)
                    start_index = i + 1
                    mid_val = s[close_index + 1:start_index -2 ] 
                    value = value + mid_val
                    #print ("value_Chck" + mid_val)
                    
                    #print ("start_index:" +  str(start_index))
                    #d=0
                    start+=1
            c = c + 1
            
        elif s[i] == ']':
            c = c-1
            close_index = i 
            #print ("close_index:" + str(close_index))
            d = d+1
        if d != 0:
            #print b
            for j in range(int(b)):
                if c == 0:
                    #print (s[start_index:close_index])
                    #print j
                    value = value + (s[start_index:close_index])
                    #print value
    if close_index <= len(s) :
        value = value + s[close_index+1:]
        print(value)
        
    if '[' in value:
        #print(value)
        decodeString(value)
        
        

a = "mon3[asun2[c]]mon"        
#sol = Solution()       
decodeString(a)       