def morphological_op(image, kernel, operation):
    """
    Apply morphological erosion or dilation to a binary image.
    """
    # Write code here
    import numpy as np
    
    image = np.asarray(image)
    kernel = np.asarray(kernel)
    k = kernel.shape[0]
    
    padding = k//2
    padded = np.pad(image, padding, mode="constant", constant_values=0)

    H,W = image.shape
    output = np.zeros_like(image)
    for i in range(H):
        for j in range(W):
            region = padded[i : i + k, j : j + k]
            
            if operation == "erode":
                if np.all(region[kernel == 1] == 1):
                    output[i][j] = 1
            if operation == "dilate":
                if np.any(region[kernel == 1]==1):
                    output[i][j] = 1
    return output.tolist()
    