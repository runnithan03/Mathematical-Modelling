from math import pi

def point_on_ray(point,ray):
    x=point[0]
    y=point[1]
    start_x=ray[0][0]
    start_y=ray[0][1]
    angle = ray[1] 
    
    if angle == pi or angle==-pi or angle== pi/2 or angle==-pi/2 or angle==0:
        if angle == pi or -pi:
            if x<start_x and y==start_y:
                return True
            else:
                return False
        if angle == pi/2:
            if x==start_x and y>start_y:
                return True
            else:
                return False
        if angle == -pi/2:
            if x==start_x and y<start_y:
                return True
            else:
                return False
        if angle ==0:
            if x>start_x and y==start_y:
                return True
            else:
                return False
    else:
        if angle>0 and angle<pi/2:
            if x>start_x and y>start_y:
                return True
            else:
                return False
        if angle >pi/2 and angle < pi:
            if x<start_x and y>start_y:
                return True
            else:
                return False
        if angle <0 and angle>-pi/2:
            if x>start_x and y<start_y:
                return True
            else:
                return False
        if angle <-pi/2 and angle >-pi:
            if x<start_x and y<start_y:
                return True
            else:
                return False
    

print(point_on_ray([5,5],[[2,2],0]))
            
    
    