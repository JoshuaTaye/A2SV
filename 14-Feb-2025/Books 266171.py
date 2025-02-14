# Problem: Books - https://codeforces.com/contest/279/problem/B

[n, time] = list(map(int, input().split()))
books = list(map(int, input().split()))
left = 0
max_books = 0
book_sum = 0

for right in range(n):
    book_sum += books[right]
    while book_sum > time:
        book_sum -= books[left]
        left += 1
    max_books = max(max_books, right - left + 1)
print(max_books)


