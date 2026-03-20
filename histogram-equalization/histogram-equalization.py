def histogram_equalize(image):
    """
    Apply histogram equalization to enhance image contrast.
    """
    # Write code here
    import numpy as np
    img = np.asarray(image)

    hist = np.zeros(256)
    img_flat = img.flatten()
    for i in img_flat:
        hist[i]+=1
    cdf = np.cumsum(hist)
    cdf_min = cdf[cdf > 0].min()
    cdf_max = cdf.max()
    if cdf_max == cdf_min:
        return np.zeros_like(image).tolist()

    ''' 
    H,W = img.shape
    
    for i in range(len(img_flat)):
        v = img_flat[i]
        new_val = np.round((cdf[v] - cdf_min)*255/(cdf_max - cdf_min))
        img_flat[i] = new_val
    new_image = img_flat.reshape((H,W))
    '''
    equalized = np.round((cdf - cdf_min)*255/(cdf_max - cdf_min))
    new_image = equalized[img]
    
    return new_image.tolist()