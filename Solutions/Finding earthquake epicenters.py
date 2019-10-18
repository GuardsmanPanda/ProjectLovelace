v = 6.0  # velocity of seismic waves [km/s]


def get_intersections(x1, y1, r1, x2, y2, r2):
    vx, vy = x1-x2, y1-y2
    v_len = (vx**2+vy**2)**0.5
    dist = (r2**2 - r1**2 + v_len**2)/(2*v_len)
    #print(dist)
    h = (r2**2-dist**2)**0.5
    ux, uy = vx/v_len, vy/v_len
    #print(ux, uy)
    return (x2+ux*dist - uy*h, y2+uy*dist + ux*h), (x2 + ux * dist + uy * h, y2 + uy * dist - ux * h)


def earthquake_epicenter(x1, y1, t1, x2, y2, t2, x3, y3, t3):
    a, b = get_intersections(x1, y1, t1*6, x2, y2, t2*6)
    c, d = get_intersections(x1, y1, t1*6, x3, y3, t3*6)
    #print(a, b, c, d)
    distance = min((a[0]-c[0])**2 + (a[1]-c[1])**2, (a[0]-d[0])**2 + (a[1]-d[1])**2)
    if distance < 1:
        return a[0], a[1]
    return b[0], b[1]


print(earthquake_epicenter(8.382353226, -58.00372081, 12.860754193, -13.590571819, 73.976069096, 22.847488548, 98.20629093856405, 28.647397287192234, 10.530134050368321))