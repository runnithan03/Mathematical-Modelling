from matplotlib import pyplot as plt

def draw_directed_segment(dirseg, col):
    pt1 = dirseg [0]
    pt2 = dirseg [1]
    dx = pt2 [0] - pt1 [0]
    dy = pt2 [1] - pt1 [1]
    # This next line is needed to make sure that the axes of the plot
    # include the full range of the directed segment
    plt.plot([pt1[0], pt2[0]], [pt1[1], pt2[1]], '-', color=col)
    plt.quiver(
        pt1[0], pt1[1], dx, dy,
        scale_units='xy', angles='xy', scale=1,
        width=.004,
        color=col
    )

def draw_point(pt,col):
    plt.plot(pt[0],pt[1],'.',color=col)
    
def draw_segment(seg, col):
    pt1 = seg [0]
    pt2 = seg [1]
    # This next line is needed to make sure that the axes of the plot
    # include the full range of the directed segment
    plt.plot([pt1[0], pt2[0]], [pt1[1], pt2[1]], '-', color=col)

def draw_path(path,col):
    n=len(path)
    i=0
    while i<n-1:
        draw_directed_segment([path[i],path[i+1]],col)
        i=i+1

def draw_window(win,col):
    x1=win[0][0]
    x2=win[0][1]
    y1=win[1][0]
    y2=win[1][1]
    draw_segment([[x1,y1],[x2,y1]],col)
    draw_segment([[x1,y2],[x2,y2]],col)
    draw_segment([[x1,y1],[x1,y2]],col)
    draw_segment([[x2,y1],[x2,y2]],col)

draw_point([0, 1], 'red')
draw_point([1, 0], 'blue')
draw_point([1.5, 1], 'pink')
draw_window([[-2, 2], [-1.8, 1.6]], [1,0,0])
draw_directed_segment([[0,1], [1,0]], 'green')
draw_directed_segment([[-1.5,-1.5], [-1.4,-1.5]], 'cyan')
draw_directed_segment([[1.5,-1.5], [1.47,-1.45]], 'green')
draw_directed_segment([[1,1], [0,1]], [0, 1, 0])
draw_path([[-1.75, 0.0], [-1.25, 0.0], [-1.5, 0.5], [-1.0, 1.6]], 'grey')
draw_segment([[-1,-0.5], [1.5, 0.3]], [1, 1, 0])
draw_segment([[-1, 1], [1, -1]], [0.5, 0.5, 0.5])

plt.show()
