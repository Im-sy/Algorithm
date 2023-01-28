def solution(m, n, board):
    answer = 0
    board = list(map(list, zip(*reversed(board))))

    def four_block(graph):
        visited = set()
        for r in range(n - 1):
            for c in range(len(graph[r])-1):
                if graph[r][c + 1] == graph[r + 1][c] == graph[r + 1][c + 1] == graph[r][c] and graph[r][c] != 0:
                    visited.add((r, c))
                    visited.add((r, c+1))
                    visited.add((r+1, c))
                    visited.add((r+1, c+1))
        for i, j in visited:
            graph[i][j] = 0
        return graph, len(visited)

    while True:
        board, cnt = four_block(board)
        if cnt == 0:
            break
        else:
            for i in range(n):
                zeros = board[i].count(0)
                for zero in range(zeros):
                    board[i].remove(0)
                for zero in range(zeros):
                    board[i].append(0)
            answer += cnt

    return answer


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))