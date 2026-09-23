class Solution:
    def compress(self, chars: list[str]) -> int:
        s = ""
        num = 1
        for char in chars:
            if len(s) == 0:
                s = char
            elif s[-1] == char:
                num += 1
            else:
                if num > 1:
                    s += str(num)
                s += char
                num = 1 
        if num > 1:
            s += str(num)
        chars[:] = list(s)
        return len(chars)