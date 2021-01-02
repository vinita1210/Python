Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Input: s = "3[a2[c]]"
Output: "accaccacc"

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"

sol1 :


class Solution:
    def decodeString(self, s: str) -> str:
        d =0
        start = 0
        c=0
        #print(s)
        value = ''
        close_index=0
        check=0
        for i in range(len(s)):
            d = 0
            if s[i] == '[':
                check = check+1
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
                check = check+1
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
            if check == 0:
                value = value + s[close_index:]
                #print(value)
            else:
                value = value + s[close_index+1:]
        if '[' in value:
            #print("chck : "+ value)
            value1 = Solution.decodeStringAgain(self,value)
            #print("value1 : " + value1)
            return value1
        else:
            return value    

    def decodeStringAgain(self,s):
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
            #print(value)
        return value                
 
 
#sol = Solution()    
#sol.decodeString('3[a2[c]]')             

abc3[cd]xyz

Sol 2:
    
class Solution:
    def _init_(self): 
        self.top = -1 
        self.array = [] 
        self.output = ''
    def isEmpty(self): 
        return True if self.top == -1 else False
    
    def pop(self): 
        if not self.isEmpty(): 
            self.top -= 1
            return self.array.pop() 
        else: 
            return "0"
    
    def push(self, op): 
        self.top += 1
        self.array.append(op)
    
    def decodeString(self, s: str) -> str:
        exp = s+']'
        for x,i in enumerate(exp):
            if i.isalpha(): 
                self.output = self.output + i
            elif i  == '[': 
                self.output = self.output + i
            elif i == ']':
                a = self.pop()
                if self.output.rfind('[') != -1:
                    new_str = self.output[self.output.rfind('[')+1:]
                    self.output = self.output[:self.output.rfind('[')]
                    for _ in range(int(a)):
                        self.output = self.output + new_str
            else:
                if exp[x-1].isdigit():
                    continue
                if exp[x+1].isdigit():
                    if exp[x+2].isdigit():
                        print(exp[x:x+3])
                        self.push(exp[x:x+3])
                    else:
                        print(exp[x:x+2])
                        self.push(exp[x:x+2])
                else:
                    self.push(i)
  
        answer = "".join(self.output)
        return answer
        
abc3[cd]xyz        
mon3[asun2[c]]mon
        
