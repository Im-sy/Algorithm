from collections import deque


def solution(board, moves):
    answer = 0
    trans_board = [deque([row[i] for row in board if row[i] != 0]) for i in range(len(board[0]))]
    result = []
    for move in moves:
        if trans_board[move-1]:
            doll = trans_board[move-1].popleft()
            if result:
                if result[-1] == doll:
                    result.pop()
                    answer += 2
                else:
                    result.append(doll)
            else:
                result.append(doll)
    return answer


print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))
