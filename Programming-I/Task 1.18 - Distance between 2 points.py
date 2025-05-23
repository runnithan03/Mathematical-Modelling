def dist2(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    k = dx**2 + dy**2 
    return k**0.5

print(dist2(2,1,7,13))