class Solution:
    def isValid(self, s: str) -> bool:
        open_par = ["(","[","{"]
        par_dict = {"(":")","[":"]","{":"}"}
        st = []
		# empty string is not valid
        if not s: 
            return False
        
        for p in s:
            print(p)
            if p in open_par:  # only append open parentheses
                st.append(p)
                print(st)
            elif st and p == par_dict[st.pop()]: # do nothing if paired
                print(st)
                pass
            else:
                return False
        # if stack is empty then all has been paired   
        return False if st else True
