import polygons
import semicircles
import csv

# mass, point_x, point_y
def merge_point_masses(masses: list[float], points: list[list[float]]) -> list[float, float, float]:
    totalObjects = len(masses)
    totalMass = sum(masses)

    com_x = 0
    com_y = 0
    for i in range(totalObjects):
        com_x += masses[i] * points[i][0]
        com_y += masses[i] * points[i][1]
    
    com_x /= totalMass
    com_y /= totalMass

    return [totalMass, com_x, com_y]

with open("polygons.csv", "r") as file:
    reader = csv.reader(file)
    reader.__next__()

    areas: list[float] = []
    centroids: list[list[float]] = []
    vertices: list[list[float]] = []

    isNegativeSpace = False

    for row in reader:
        if row[0] != "" and len(vertices) > 0:
            data: list[float, float, float] = polygons.centroid_and_area(vertices)
            areas.append(-data[0] if isNegativeSpace else data[0])
            centroids.append([data[1], data[2]])
            vertices.clear()
        vertice: list[float] = [float(row[1]), float(row[2])]
        vertices.append(vertice)

        if row[0] == "-":
            isNegativeSpace = True
        elif row[0] == "p":
            isNegativeSpace = False
    
    data: list[float, float, float] = polygons.centroid_and_area(vertices)
    areas.append(-data[0] if isNegativeSpace else data[0])
    centroids.append([data[1], data[2]])
    vertices.clear()
    
    single_point_mass = merge_point_masses(areas, centroids)
    mass = single_point_mass[0]
    com = [single_point_mass[1], single_point_mass[2]]

    print(mass)
    print(com)

with open("semicircles.csv", "r") as file:
    reader = csv.reader(file)
    reader.__next__()

    areas: list[float] = []
    centroids: list[list[float]] = []
    corners: list[list[float]] = []

    isNegativeSpace = False
    isUp = False

    for row in reader:
        if row[0] != "" and len(corners) > 0:
            data: list[float, float, float] = semicircles.centroid_and_area(corners[0], corners[1], isUp)
            areas.append(-data[0] if isNegativeSpace else data[0])
            centroids.append([data[1], data[2]])
            corners.clear()

        if row[0] == "-":
            isNegativeSpace = True
        elif row[0] == "p":
            isNegativeSpace = False
        
        if row[1] == "d":
            isUp = False
        elif row[1] == "u":
            isUp = True
        
        corner: list[float] = [float(row[2]), float(row[3])]
        corners.append(corner)
    
    data: list[float, float, float] = semicircles.centroid_and_area(corners[0], corners[1], isUp)
    areas.append(-data[0] if isNegativeSpace else data[0])
    centroids.append([data[1], data[2]])
    corners.clear()
    
    single_point_mass = merge_point_masses(areas, centroids)
    mass = single_point_mass[0]
    com = [single_point_mass[1], single_point_mass[2]]

    print(mass)
    print(com)

