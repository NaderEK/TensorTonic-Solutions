import numpy as np

def batch_generator(X, y, batch_size, rng=None, drop_last=False):
    """
    Randomly shuffle a dataset and yield mini-batches (X_batch, y_batch).
    """
    # Write code here
    X, y = np.asarray(X), np.asarray(y)
    indecies = np.arange(len(y))

    if rng:
        rng.shuffle(indecies)
    else:
        np.random.shuffle(indecies)

    X, y = X[indecies], y[indecies]

    for i in range(0, len(y), batch_size):
        if drop_last and i+batch_size > len(y):
            break
        batch_x = X[i:i+batch_size]
        batch_y = y[i:i+batch_size]
        yield batch_x, batch_y
    