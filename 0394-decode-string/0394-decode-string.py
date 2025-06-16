class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for i in s:
            if i!=']':
                stack.append(i)
            else:
                #find the substring
                substring = ""
                while stack[-1]!='[':
                    substring = stack.pop() + substring
                
                #pop the bracket
                stack.pop()

                #find the number of times
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                
                #Multiply and put back in the stack
                stack.append(int(k) * substring)
        
        return "".join(stack)
            

        