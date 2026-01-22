def solution(wallpaper):
    R=len(wallpaper)
    C=len(wallpaper[0])
    
    min_x=C
    max_x=0
    min_y=R
    max_y=0
    
    for y in range(R):
        for x in range(C):
            if wallpaper[y][x]=='#':
                min_y = min(min_y, y)
                min_x = min(min_x, x)
                max_y = max(max_y, y)
                max_x = max(max_x, x)
    
    answer=[min_y,min_x,max_y+1,max_x+1]
    return answer

    