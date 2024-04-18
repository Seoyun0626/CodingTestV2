def bfs(i, visited, computers):
    visited[i] = 1
    print(i, visited, computers)

    for j in range(len(computers)):
        if computers[i][j] == 1 and visited[j] == 0:
            bfs(j, visited, computers)


def solution(n, computers):
    answer = 0
    visited = [0] * n

    for i in range(n):
        for j in range(n):
            if i == j:
                computers[i][j] = 0
    print(computers)

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and visited[i] == 0:
                answer += 1
                print("enter bfs", i, visited, computers)
                bfs(i, visited, computers)
    print("answer", answer)
    print("visited", visited)

    return answer

# solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
# solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])