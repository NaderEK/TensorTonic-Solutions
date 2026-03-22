import numpy as np

def kfold_split(N, k, shuffle=True, rng=None):
    """
    Returns: list of length k with tuples (train_idx, val_idx)
    """
    # Write code here
    indecies = np.arange(N)

    if shuffle:
        if rng:
            rng.shuffle(indecies)
        else:
            np.random.shuffle(indecies)

    folds = np.array_split(indecies, k)
    results = []
    for i in range(k):
        val_idx = folds[i]
        train_idx = np.concatenate([folds[j] for j in range(k) if j != i])
        results.append((train_idx, val_idx))

    return results