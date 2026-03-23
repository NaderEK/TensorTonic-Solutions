def rotate_image(image, angle_degrees):
    """
    Rotate the image counterclockwise by the given angle using nearest neighbor interpolation.
    """
    # Write code here
    import math

    angle_radian = math.radians(angle_degrees)
    H,W = len(image), len(image[0])
    new_image = [[0]*W for _ in range(H)]

    cy = (H - 1)/2
    cx = (W - 1)/2

    for i in range(H):
        dy = i - cy
        for j in range(W):
            dx = j - cx

            src_y = round(cy + dy*math.cos(angle_radian) + dx*math.sin(angle_radian))
            src_x = round(cx - dy*math.sin(angle_radian) + dx*math.cos(angle_radian))

            if not 0 <= src_y < H:
                src_y = 0
            if not 0 <= src_x < W:
                src_x = 0
            new_image[i][j] = image[src_y][src_x]
    return new_image
            