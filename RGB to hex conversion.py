import math
def rgb(r,g,b):
    if r > 255:
        r = 255
    elif r < 0:
        r = 0
    if g > 255:
        g = 255
    elif g < 0:
        g = 0
    if b > 255:
        b = 255
    elif b < 0:
        b = 0
    
    hex = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
    rd = math.floor(r/16)
    rh = str(hex[rd])+str(hex[r-(rd*16)])
    gd = math.floor(g/16)
    gh = str(hex[gd])+str(hex[g-(gd*16)])
    bd = math.floor(b/16)
    bh = str(hex[bd])+str(hex[b-(bd*16)])
    return rh + gh + bh

print(rgb(30, 55, 255))