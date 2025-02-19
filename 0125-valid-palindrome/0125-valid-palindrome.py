import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
    

        def preprocess_string(s):
            return re.sub(r'[^a-z0-9]', '', s.lower())

        string= preprocess_string(s)
        reversestring= string[::-1]
        if string==reversestring:
            return True
        else:
            return False

            

        

        