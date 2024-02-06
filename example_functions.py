def goursat_tangle(x, y, z):
    a, b, c = 0.0, -5.0, 11.8
    return (
        x**4
        + y**4
        + z**4
        + a * (x**2 + y**2 + z**2) ** 2
        + b * (x**2 + y**2 + z**2)
        + c
    )
