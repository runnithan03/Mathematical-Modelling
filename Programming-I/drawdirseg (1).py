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

draw_directed_segment([[0,1], [1,0]], 'green')
draw_directed_segment([[-1.5,-1.5], [-1.4,-1.5]], 'cyan')
draw_directed_segment([[1.5,-1.5], [1.47,-1.45]], 'green')
draw_directed_segment([[1,1], [0,1]], [0, 1, 0])
plt.show()