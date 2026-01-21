
def solution(maps):
    R=len(maps)
    C=len(maps[0])
    visited = [[0 for col in range(C)] for row in range(R)]
    answer = []
    
    for y in range(R):
        for x in range(C):
            if maps[y][x]!='X' and not visited[y][x]:
                
                max_value=0
                queue=[(y,x)]
                visited[y][x]=1 # 시작점 방문 처리
                
                while(queue):
                    cur_y,cur_x=queue.pop(0)
                    max_value+=int(maps[cur_y][cur_x])
                    
                    for dx,dy in [(0,1), (0,-1), (1,0), (-1,0)]: # 상 하 좌 우
                        ny=cur_x+dx
                        nx=cur_y+dy
                        
                        if 0 <= ny < R and 0 <= nx < C and maps[ny][nx] != 'X' and not visited[ny][nx]:
                            visited[ny][nx]=1 # 다음 점 방문 처리
                            queue.append((ny,nx))
                
                answer.append(max_value)
    answer.sort()
    if answer:
        return answer
    else:
        return [-1]
