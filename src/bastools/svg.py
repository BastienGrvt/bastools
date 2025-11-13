from ._imports import *
import svgwrite


def svg_draw(x_min, x_max, N, unit_size, foo, file_path="/svg_graph.svg"):

    # Computation
    X = np.linspace(x_min, x_max, N)
    Y = np.array([foo(x) for x in X])

    # Size param
    y_min, y_max = np.min(Y), np.max(Y)
    X_size, Y_size = (x_max - x_min) * unit_size, (y_max - y_min) * unit_size

    # SVG creation
    dwg = svgwrite.Drawing(file_path, size=(X_size, Y_size))

    # Move to first point
    x0 = (X[0] - x_min) * unit_size
    y0 = (y_max - Y[0]) * unit_size
    path = dwg.path(d=f"M {x0} {y0}", stroke="black", fill="none", stroke_width=2)

    # Draw the curve
    for x, y in zip(X[1:], Y[1:]):
        x_pxl = (x - x_min) * unit_size
        y_pxl = (y_max - y) * unit_size
        path.push(f"L {x_pxl} {y_pxl}")


    dwg.add(path)
    dwg.save()
    return dwg
