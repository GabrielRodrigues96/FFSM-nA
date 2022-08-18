def bestIndiv_evolvedSociety_GAfile(n_bits,n_leafs,dim_populat,cost_evolved,bit_matrix_evolved,p_search):
    
    import numpy as np
    from phenotype_computing_GAfile import phenotype_computing_GAfile
    
    ## BEST INDIVIDUAL INDEX
    ind_best = cost_evolved.argmax(); best_cost = cost_evolved.max()
    
    ## BUILDING OF BEST SOLUTION
    
    best_solution = np.zeros((n_bits.max(),n_leafs))
    best_phenotype = np.zeros(n_leafs)
    for k in range(n_leafs):
        best_solution[0:n_bits[k],k] = bit_matrix_evolved[ind_best,:,k]
        best_phenotype[k] = phenotype_computing_GAfile(best_solution[0:n_bits[k],k],p_search[:,k])  
    
    
    return best_solution,best_phenotype,best_cost