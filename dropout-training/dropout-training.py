import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """
    # Write code here
    x = np.asarray(x)
    if rng:
        random_values = rng.random(x.shape)
    else:
        random_values = np.random.random(x.shape)
    scale = 1/(1-p)

    dropout_pattern = np.where(random_values <= (1-p), scale, 0)
    print(random_values)
    print((1-p))
    print(dropout_pattern)
    dropped_out = x*dropout_pattern

    return dropped_out, dropout_pattern