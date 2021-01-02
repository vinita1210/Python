class Solution:
    def isPalindrome(self, x: int) -> bool:
        print(x)
        value=''
        max_len = len(str(x))
        no = str(x)
        for i in range(len(str(x))):
            value=value+ no[max_len - (i + 1)]
            
        return bool(value == no)

class Solution(object):
def isPalindrome(self, x):
"""
:type x: int
:rtype: bool
"""
if "{}".format(x)=="{}".format(x)[::-1]:
return True
else:
return False
