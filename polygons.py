# (area, centriod_x, centriod_y)
def centroid_and_area(vertices: list[list[float]]) -> list[float, float, float]:
    numVertices = len(vertices)
    vertices.append(vertices[0])

    area = 0
    c_x = 0
    c_y = 0

    for i in range(numVertices):
        x_i, y_i = vertices[i]
        x_next, y_next = vertices[i + 1]
        cross_product = (x_i * y_next - x_next * y_i)
        area += cross_product
        c_x += (x_i + x_next) * cross_product
        c_y += (y_i + y_next) * cross_product

    # Finalize calculations
    area *= 0.5
    area = abs(area)
    c_x /= (6 * area)
    c_y /= (6 * area)

    return (area, c_x, c_y)