# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        def solve(x, inp):
            output = [[]]
            j = 0
            while j < len(inp):
                while j < len(inp) and not inp[j].isnumeric():
                    output[-1].append(inp[j])
                    j += 1
                if j < len(inp):
                    output.append([])
                if j < len(inp) and inp[j].isnumeric():
                    res = []
                    val = []
                    while inp[j].isnumeric():
                        val.append(inp[j])
                        j += 1
                    stack = 0
                    while j < len(inp):
                        if inp[j] == "[":
                            stack += 1
                        elif inp[j] == "]":
                            stack -= 1
                        res.append(inp[j])
                        if not stack:
                            break
                        j += 1
                    res.append(inp[j])
                    val = "".join(val)
                    output[-1].append(solve(val, res))
                j += 1
            j = []
            for i in output:
                for k in i:
                    if k != "[" and k != "]":
                        j.append(k)
            return int(x) * "".join(j)
        return solve(1, s)


