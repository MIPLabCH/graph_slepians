import numpy as np

def normalize_adjmat(A,D):
    """
    Information:
    ------------
    Normalize Adjacency/Laplacian Matrix

    Parameters
    ----------    
    A::[2darray<float>]
        Adjacency matrix
    D::[2darray<float>]
        Degree matrix

    Returns
    -------
    norm_A::[2darray<float>]
        Normalized adjacency matrix
    """

    inv_D = np.diag(1/np.sqrt(D)) # D^(-0.5)
    norm_A = (inv_D @ A @ inv_D)
    return norm_A

def laplacian(D,A):
    """
    Information:
    ------------
    Compute Laplacian

    Parameters
    ----------    
    D::[2darray<float>]
        Degree matrix
    A::[2darray<float>]
        Adjacency matrix

    Returns
    -------
    L::[2darray<float>]
        Laplacian
    """

    L = np.diag(D)-A
    return L