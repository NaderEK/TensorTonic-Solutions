import numpy as np

def _sigmoid(x):
    """Numerically stable sigmoid function"""
    return np.where(x >= 0, 1.0/(1.0+np.exp(-x)), np.exp(x)/(1.0+np.exp(x)))

def _as2d(a, feat):
    """Convert 1D array to 2D and track if conversion happened"""
    a = np.asarray(a, dtype=float)
    if a.ndim == 1:
        return a.reshape(1, feat), True
    return a, False

def gru_cell_forward(x, h_prev, params):
    """
    Implement the GRU forward pass for one time step.
    Supports shapes (D,) & (H,) or (N,D) & (N,H).
    """
    D = params["Wz"].shape[0]
    H = params["Wz"].shape[1]
    
    x, was_1d = _as2d(x, D)
    h_prev, _ = _as2d(h_prev, H)
    
    # Write code here

    Wz, Uz, bz = params["Wz"], params["Uz"], params["bz"]
    Wr, Ur, br = params["Wr"], params["Ur"], params["br"]
    Wh, Uh, bh = params["Wh"], params["Uh"], params["bh"]

    zt = _sigmoid(x @ Wz + h_prev @ Uz + bz)
    rt = _sigmoid(x @ Wr + h_prev @ Ur + br)
    ht_hat = np.tanh(x @ Wh + (rt* h_prev)@Uh + bh)

    ht = (1-zt)*h_prev + zt * ht_hat

    return ht.flatten() if was_1d else ht
    