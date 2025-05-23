def lines_intersect(line1,line2):
    line1_x=line1[0]
    line1_y=line1[1]
    line1_c=line1[2]
    line2_x=line2[0]
    line2_y=line2[1]
    line2_c=line2[2]
    denom=line1_x*line2_y-line1_y*line2_x
    lst=[]
    if denom==0:
        return "None"
    else:
        num_x=line1_y*line2_c-line1_c*line2_y
        num_y=line1_c*line2_x-line1_x*line2_c
        x=num_x/denom
        y=num_y/denom
        lst.append(x)
        lst.append(y)
        return lst
