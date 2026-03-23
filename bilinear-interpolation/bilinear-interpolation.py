def bilinear_resize(image, new_h, new_w):
    """
    Resize a 2D grid using bilinear interpolation.
    """
    import math
    # Write code here
    new_image = [[0]*new_w for _ in range(new_h)]
    old_h, old_w = len(image), len(image[0])
    
    for i in range(new_h):
        for j in range(new_w):
            src_y = i * (old_h - 1)/(new_h - 1) if new_h != 1 else 0
            src_x = j * (old_w - 1)/(new_w - 1) if new_w != 1 else 0
            y0, x0 = math.floor(src_y), math.floor(src_x)
            dy, dx = src_y%1, src_x%1

            y1, x1 = min(y0 + 1, old_h - 1), min(x0 + 1, old_w - 1)
            a00 = image[y0][x0]*(1-dy)*(1-dx)
            a10 = image[y1][x0]*dy*(1-dx)
            a01 = image[y0][x1]*(1-dy)*dx
            a11 = image[y1][x1]*dy*dx
            new_image[i][j] = a00 + a10 + a01 + a11
    return new_image