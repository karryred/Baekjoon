def solution(board):
    danger=set()
    R=len(board)
    C=len(board[0])
    
    for y in range(R):
        for x in range(C):
            if board[y][x]==1:
                danger.add((y,x))
                for dy,dx in [(1,0),(-1,0),(0,-1),(0,1),(1,1),(1,-1),(-1,1),(-1,-1)]:
                    ny=y+dy
                    nx=x+dx
                    if 0<=ny<R and 0<=nx<C:
                        danger.add((ny,nx))
                    
    answer = R*C - len(danger)
    return answer