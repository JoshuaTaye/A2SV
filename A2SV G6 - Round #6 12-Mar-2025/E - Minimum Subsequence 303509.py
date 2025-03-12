# Problem: E - Minimum Subsequence - https://codeforces.com/gym/594077/problem/E

tot = int(input())
for l in range(tot):
    n = int(input())
    x = input()
    zeros = []
    ones = []
    st = []
    for i in range(len(x)):
        tot = len(zeros) + len(ones)
        if x[i] == "0":
            if ones:
                tot = ones.pop()
            zeros.append(tot)
        else:
            if zeros:
                tot = zeros.pop()
            ones.append(tot)
        st.append(tot+1)
    print(len(ones) + len(zeros))
    print(*st)
