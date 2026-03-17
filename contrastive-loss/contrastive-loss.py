import numpy as np

def contrastive_loss(a, b, y, margin=1.0, reduction="mean") -> float:
    """
    a, b: arrays of shape (N, D) or (D,)  (will broadcast to (N,D))
    y:    array of shape (N,) with values in {0,1}; 1=similar, 0=dissimilar
    margin: float > 0
    reduction: "mean" (default) or "sum"
    Return: float
    """
    # Write code here
    a,b,y = np.asarray(a), np.asarray(b), np.asarray(y)

    # Handle shapes
    N = y.shape[0]
    a = a.reshape(N,-1)
    b = b.reshape(N,-1)

    d = np.linalg.norm(a-b, axis=1)

    L = y*d**2 + (1 - y)*np.maximum(0, margin-d)**2

    if reduction == "mean":
        return np.mean(L)
        
    elif reduction == "sum":
        return np.sum(L)
    else:
        return None