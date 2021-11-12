def solve(A):
    sum=0
    for a in A:
        if a>=13 and a<=19:
            if a!=15 and a!=16:
                continue

        sum+=a

    return sum

if __name__ == "__main__":
    n = 3
    A = []
    # iterating till the range
    for i in range(n):
        num = int(input())
        A.append(num)

    print(solve(A))