#assuming point lies on line in which segment belongs
def point_on_segment(point,seg):
    a=point[0]
    b=point[1]
    c=seg[0][0]
    d=seg[0][1]
    e=seg[1][0]
    f=seg[1][1]
    rounding = 10e-15
    if a>max(c,e) or a <min(c,e):
        if a-max(c,e)>rounding:
            return False
        if min(c,e) - a > rounding:
            return False
        else:
            return True
    if b>max(d,f) or a <min(d,f):
        if b-max(d,f)>rounding:
            return False
        if min(d,f) - b > rounding:
            return False
        else:
            return True
    
