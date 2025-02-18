# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

n, k, q = map(int, input().split())
recipes = []
questions = []
for _ in range(n):
    recipes.append(list(map(int, input().split())))

counter = [0]*200001
checker = [0]*200001
for recipe in recipes:
    counter[recipe[0]] += 1
    if recipe[1]+1 <= 200000:
        counter[recipe[1]+1] -= 1

for p in range(1, 200001):
    counter[p] += counter[p-1]

for s in range(1, 200001):
    if counter[s] >= k:
        checker[s] = 1

for o in range(1, 200001):
    checker[o] += checker[o-1]
for _ in range(q):
    questions.append(list(map(int, input().split())))
for question in questions:
    print(checker[question[1]] - checker[question[0]-1])





