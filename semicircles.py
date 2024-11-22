import math

# area, com_x, com_y
def centroid_and_area(corner1: list[float], corner2: list[float], isUp: bool) -> list[float, float, float]:
    radius = math.sqrt((corner1[0] - corner2[0])**2 + (corner1[1] - corner2[1])**2)/2
    center = [(corner1[0] + corner2[0]) / 2, (corner1[1] + corner2[1]) / 2]

    slope_of_perpendicular = -1/((corner2[1] - corner1[1]) / (corner2[0] - corner1[0]))
    angle_of_perpendicular = math.atan(slope_of_perpendicular)

    distance_to_com = 4 * radius / (3 * math.pi)

    if (slope_of_perpendicular > 0 and isUp) or (slope_of_perpendicular < 0 and not isUp):
        com = [center[0] + math.cos(angle_of_perpendicular) * distance_to_com, center[1] + math.sin(angle_of_perpendicular) * distance_to_com]
    else:
        com = [center[0] - math.cos(angle_of_perpendicular) * distance_to_com, center[1] - math.sin(angle_of_perpendicular) * distance_to_com]
    
    area = math.pi * radius**2 / 2

    return [area, com[0], com[1]]
