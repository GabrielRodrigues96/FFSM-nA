def crossover_execution_GAfile(bit_matrix_selected,n_bits,n_leafs,reprodMates_ind):
    
    from crossover_leaf_GAfile import crossover_leaf_GAfile
        
    # permutation overwriting
    bit_matrix_reprod = bit_matrix_selected.copy();
    
    for k in range(n_leafs):
        
        bit_matrix_leaf = bit_matrix_selected[:,0:n_bits(k),k]; # leaf sampling
        
        bit_matrix_reprod_leaf = crossover_leaf_GAfile(reprodMates_ind,bit_matrix_leaf,n_bits(k));
        
        bit_matrix_reprod[:,0:n_bits(k),k] = bit_matrix_reprod_leaf # leaf building
        
    return bit_matrix_reprod
    
    
