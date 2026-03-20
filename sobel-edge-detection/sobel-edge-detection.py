def sobel_edges(image):
    """
    Apply the Sobel operator to detect edges.
    """
    import numpy as np
    # Write code here
    image = np.asarray(image)
    Kx = np.array([
        [-1,0,1],
        [-2,0,2],
        [-1,0,1]
    ])
    Ky = np.array([
        [-1,-2,-1],
        [0,0,0],
        [1,2,1]
    ])
    k = Kx.shape[0]
    padding = k//2

    padded = np.pad(image, padding, mode="constant", constant_values = 0)

    H,W = image.shape
    output = np.zeros_like(image, dtype="float")
    for i in range(H):
        for j in range(W):
            region = padded[i:i+k, j:j+k]
            Gx = np.sum(region*Kx)
            Gy = np.sum(region*Ky)
            output[i][j] = np.sqrt(Gx**2 + Gy**2)
    return output.tolist()