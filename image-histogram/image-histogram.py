def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    # Write code here
    image_flat = []
    for i in image:
        image_flat.extend(i)
    histogram = [0]*256

    for i in image_flat:
        histogram[i] +=1
    return histogram