t = int(input())

pnt = []

for _ in range(t):
    n = int(input())
    data = [(i,idx) for idx,i in enumerate(list(map(int,input().split())))]
    print('data',data)
    stack = []
    result = []

    result.append((0,0))
    stack.append(data[-1])
    print('stack',stack)

    cnt = 0
    for i in range(len(data)-2,-1,-1):
        while True:
            if stack:
                if data[i][0] == 0:
                    cnt += 1
                    result.append((0,cnt))
                    break
                elif data[i][0] <= stack[-1][0]:
                    result.append(stack[-1])
                    stack.append(data[i])
                    break
                else:
                    stack.pop()
            else:
                result.append((0,data[i][1]))
                stack.append(data[i])
                break
    
    result.reverse()
    print('result',result)

    max = 0
    for i in range(n):
        tmp = result[i][1]-data[i][1]
        if max < tmp:
            max = tmp

    pnt.append(max)


for i in range(t):
    print(f"#{i+1} {pnt[i]}")
    
