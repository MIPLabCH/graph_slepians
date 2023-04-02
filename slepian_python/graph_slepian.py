import numpy as np
from scipy.linalg import eig
from scipy.sparse.linalg import eigsh



def compute_slepians(L, selection, NW, const_scale, maxiter=2500):
    """
    Information:
    ------------
    Compute slepians (laplacian/regular slepian/ modif distance slepian) 
    Information included are:
        - slepian vector
        - eigenvalue
        - concentration
        - cut

    Parameters
    ----------    
    L          ::[2darray<float>]
        Laplacian
    selection  ::[1darray<bool>]
        True if in selected nodes False otherwise
    NW         ::[int]
        Number of eigenvectors used bandlimit
    const_scale::[bool]
        Flag to sum up to 1 the spectrum limited laplacian eigenvalues
    maxiter    ::[int]
        Number of iteration for spectre approximation

    Returns
    -------
    basis     ::[list<2darray>]
        slepian vectors / energy distribution
    basis_eig0::[list<1darray>]
    basis_conc::[list<1darray>]
    basis_cut ::[list<1darray>]
    """

    # Lapalacian Spectrum
    S1, Utr = eigsh(L, NW, which='SA', maxiter=maxiter)
    S1 = np.abs(S1)
    if const_scale:
        tmp_scale = np.sum(S1)
    else:
        tmp_scale = 1
    S1 = S1/tmp_scale

    # selcting index (e.g bear head)
    basis_contr = Utr[selection]
    C = (basis_contr.T @ basis_contr)

    basis_contr2 = Utr[selection] @ np.diag(np.sqrt(S1))
    C2 = (basis_contr2.T @ basis_contr2)

    # regular slepian
    slepval, slepvect = eig(C)
    slepval, slepvect = np.real(slepval), np.real(slepvect)
    SLR = Utr @ slepvect
    seigr = (SLR.T @ (L) @ SLR) / tmp_scale
    concr = np.diagonal(slepvect.T @ C @ slepvect)
    cutr  = np.diagonal(slepvect.T @ C2 @ slepvect)

    # graph embedding distance slepian
    emb_slepval, emb_slepvect = eig(C2)
    emb_slepval, emb_slepvect = np.real(emb_slepval), np.real(emb_slepvect)
    SLE = Utr @ emb_slepvect
    seige = (SLE.T @ (L) @ SLE) / tmp_scale
    conce = np.diagonal(emb_slepvect.T @ C @ emb_slepvect)
    cute  = np.diagonal(emb_slepvect.T @ C2 @ emb_slepvect)

    # Laplacian | Regular Slepian | Embedded distance Slepian
    basis = [Utr, SLR, SLE]
    basis_eig0 = [S1, np.diagonal(seigr), np.diagonal(seige)]
    basis_conc = [np.diagonal(C), concr, conce]
    basis_cut = [np.diagonal(C2), cutr, cute]

    return basis, basis_eig0, basis_conc, basis_cut
