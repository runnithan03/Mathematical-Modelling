from matplotlib import pyplot as plt

def draw_segment(seg, col):
    pt1 = seg [0]
    pt2 = seg [1]
    # This next line is needed to make sure that the axes of the plot
    # include the full range of the directed segment
    plt.plot([pt1[0], pt2[0]], [pt1[1], pt2[1]], '-', color=col)

draw_segment([[-1,-0.5], [1.5, 0.3]], [1, 1, 0])
draw_segment([[-1, 1], [1, -1]], [0.5, 0.5, 0.5])

print(min(5,23))