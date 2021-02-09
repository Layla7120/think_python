def recurse(n, s):
    # n의 값이 0이면 s 출력
    if n==0:
        print(s)
    # n의 값이 0이 아니라면 n의 값: n-1, s의 값: n + s로 대체되어 다시 recurse 함수로 들어감
    else:
        recurse(n - 1, n + s)


recurse(3, 0)
recurse(-1, 0)