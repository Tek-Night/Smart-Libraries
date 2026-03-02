import numpy as np

def cosine_similarity_matrix(X):
    dot_products = X@X.T
    norms = np.linalg(X, axis = 1)
    norm_matrix = np.outer(norms,norms)
    return dot_products/norm_matrix