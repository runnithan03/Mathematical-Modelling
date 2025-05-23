from math import tan,pi

def point_on_ray(point,ray):
    pt=ray[0]
    angle=ray[1]
    x=point[0]
    y=point[1]
    if angle == pi/2 or angle == -pi/2:
        if angle == pi/2 and y>pt[1] and pt[0]==x:
            return True
        if angle == -pi/2 and y<pt[1] and pt[0]==x:
            return True
        else:
            return False
    else:
        if angle>=0 and y>=pt[1] or angle <= 0 and y<=pt[1]:
            if tan(angle)>=0 and x>=pt[0] or tan(angle)<= 0 and x<=pt[0]:
                return True
            else:
                return False
        else:
            return False
        
print(point_on_ray([-0.7,1],[[-1.8,2.1],-pi/4]))