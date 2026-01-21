def solution(maps):
    R = len(maps)
    C = len(maps[0])
    visited = [[0 for _ in range(C)] for _ in range(R)]
    answer = []
    
    for y in range(R):
        for x in range(C):
            if maps[y][x] != 'X' and not visited[y][x]:
                max_value = 0
                queue = [(y, x)]
                visited[y][x] = 1
                
                while queue:
                    cur_y, cur_x = queue.pop(0)
                    max_value += int(maps[cur_y][cur_x])
                    
                    # dy: 세로 변화량, dx: 가로 변화량
                    for dy, dx in [(1, 0), (-1, 0), (0, -1), (0, 1)]: # 상 하 좌 우
                        ny = cur_y + dy
                        nx = cur_x + dx
                        
                        # ny(세로)는 R과 비교, nx(가로)는 C와 비교
                        if 0 <= ny < R and 0 <= nx < C:
                            if maps[ny][nx] != 'X' and not visited[ny][nx]:
                                visited[ny][nx] = 1
                                queue.append((ny, nx))
                
                answer.append(max_value)
    
    answer.sort()
    return answer if answer else [-1]