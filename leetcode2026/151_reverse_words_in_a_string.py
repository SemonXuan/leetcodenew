class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))

# class Solution:
#     def reverseWords(self, s: str) -> str:
#         i, j = len(s) - 1, len(s) - 1
#         revs = ""
#         point = True
#         while i >= 0:
#             if s[i] != " " and point:
#                 j = i
#                 point = False
#             if s[i] != " " and (i - 1) >= 0  and s[i-1] == " ":
#                 revs = revs + s[i:j+1] + " "
#                 point = True    
#             i -= 1
#         return revs[:-1] if s[0] == " " else revs + s[:j+1]

