def phenot_matrix_GAfile(n_bits,bit_matrix,dim_populat,p_search,n_leafs): 
    
    import numpy as np
    from phenotComput_leaf_GAfile import phenotComput_leaf_GAfile
        
    phenot_data = np.zeros((n_leafs))
    for i in range(n_leafs): 
        p_search_leaf = p_search[:,i] # leaf sampling
        bit_matrix_leaf = bit_matrix[:,1:n_bits[i],i] 
        
        dec_leaf = phenotComput_leaf_GAfile(bit_matrix_leaf,p_search_leaf,dim_populat) 
       
        phenot_data[:,i] = dec_leaf;
    
    return phenot_data

