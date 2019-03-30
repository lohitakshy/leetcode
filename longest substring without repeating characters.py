Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
             
             
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = ''
        maxle = 0
        count = 0
        if len(s) == 1:
            return 1   
        for i in range(len(s)):
            #print(result)
            if s[i] not in result:
                result += s[i]
                count+=1
            else:
                if maxle < count:
                    maxle = count
                if s[i] == s[i-1]:
                    result = s[i]
                    count = 1
                else:
                    num = result.index(s[i])
                    result = result[num+1:]
                    result+=s[i]
                    count = len(result)
                    
        if count >= maxle:
            maxle = count
                   
        return maxle

      
      
 -------------------------------------------

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = ''
        maxle = 0
        if len(s) == 1:
            return 1
        #if len(s) == len(set(s)):
         #   return len(s)
            
        for i in range(len(s)):
            dict1 = {}
            result = s[i]
            dict1[s[i]] = 1
            for j in range(i+1,len(s)):
                if s[j] not in dict1:
                    result+=s[j]
                    dict1[s[j]] = 1   
                else:
                    break
            if len(result) > maxle:
                maxle = len(result)
                result = ""
                #print(maxle)
                    
            
        return maxle
