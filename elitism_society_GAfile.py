def elitism_society_GAfile(bit_matrix_mut,n_bits,n_leafs,bit_matrix,ind_best_local,ind_worst): 
    
    import numpy as np
    ## Extraction of society's fittest
    best_solution_local = np.zeros(n_bits.max(),n_leafs)
    for k in range(n_leafs): 
        best_solution_local[0:n_bits[k],k] = bit_matrix_mut[ind_best_local,:,k]; 
    
    ## input over worst individual
    bit_matrix_evolved = bit_matrix; # initial population overwriting 
    
    for k in range(n_leafs): 
        bit_matrix_evolved[ind_worst,:,k] = best_solution_local[0:n_bits[k],k] 
    
    return bit_matrix_evolved