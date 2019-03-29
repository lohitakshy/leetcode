You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.


solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        list1 = []
        count = 0
        if l1.next == None and l2.next == None and l1.val+l2.val >= 10:
            return [(l1.val+l2.val)%10,1] 
        while l1 or l2 or carry!=0:
            if l1==None:
                val1 = 0
            else:
                val1 = l1.val
                l1 = l1.next
            if l2 == None:
                val2 = 0
            else:
                val2 = l2.val
                l2 = l2.next
            sum1 = val1+val2
            #print(sum1)
            if carry == 0:
                if sum1 >= 10:
                    carry = 1
                    list1.append(sum1%10)
                else:
                    list1.append(sum1)        
            else:
                sum1+=carry
                if sum1 >= 10:
                    carry = 1
                    list1.append(sum1%10)
                else:
                    list1.append(sum1)
                    carry = 0
        return list1
            
-----------------
--------------------------------------
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    
        i = 1
        num1 = 0
        num2 = 0
        while l1:
            num1 += (l1.val) * i
            i*=10
            l1 = l1.next
        i = 1
        while l2:
            num2 += (l2.val) * i
            i*=10
            l2 = l2.next
        sum1 = num1+num2
        if sum1 == 0:return [0]
        list1 = []
        while sum1>=1:
            list1.append(sum1%10)
            sum1 = sum1//10
        return list1
            
        
