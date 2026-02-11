import numpy as np

def _to_2d_numeric(matrix):
    # Accept list or numpy array; return np.ndarray (2D float) or None
    try:
        arr = np.asarray(matrix)
    except Exception:
        return None
    
    if arr.ndim != 2 or arr.size == 0:
        return None
    
    # Reject object/string dtype
    if arr.dtype == object or arr.dtype.kind in {"U", "S"}:
        return None
    
    # Ensure numeric by attempting float conversion
    try:
        arr = arr.astype(float)
    except Exception:
        return None
    
    return arr

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    if axis not in (None, 0, 1):
        return None
    if norm_type not in ('l1', 'l2', 'max'):
        return None
    
    arr = _to_2d_numeric(matrix)
    if arr is None:
        return None
    
    try:
        if norm_type == 'l2':
            denom = np.sqrt(np.sum(arr * arr, axis=axis, keepdims=True))
        elif norm_type == 'l1':
            denom = np.sum(np.abs(arr), axis=axis, keepdims=True)
        else:  # 'max'
            denom = np.max(np.abs(arr), axis=axis, keepdims=True)
        
        denom[denom == 0] = 1.0
        return arr / denom
    except Exception:
        return None
