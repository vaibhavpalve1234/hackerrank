
# class Solution:
#     def toLowerCase(self, str: str) -> str:
#         for i in  str:
#             if ord(i)>=65 and ord(i)<90:
#                 str=str.replace(i,chr(ord(i)+32))
#         return str
# s=Solution()
# print(s.toLowerCase("Hello"))