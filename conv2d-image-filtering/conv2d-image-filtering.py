def conv2d(image, kernel, stride=1, padding=0):
    """
    Apply 2D convolution to a single-channel image.
    """
    # Write code here
    import numpy as np
    image, kernel = np.asarray(image), np.asarray(kernel)
    H,W = image.shape
    Kh, Kw = kernel.shape
    
    Hout = (H + 2*padding - Kh)//stride  + 1
    Wout = (W + 2*padding - Kw)//stride  + 1

    padded = np.pad(image, padding, mode="constant", constant_values=0)
    output = np.zeros((Hout, Wout))
    for i in range(Hout):
        for j in range(Wout):
            y = i*stride
            x = j*stride
            region = padded[y:y+Kh, x:x+Kw]
            output[i][j] = np.sum(region*kernel)
    return output.tolist()