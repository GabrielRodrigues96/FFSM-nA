def population_init_GAfile(p_search,N_prec,dim_populat,n_leafs): 
    
    import numpy as np
    from localpopulat_gen_GAfile import localpopulat_gen_GAfile
        
    n_bits = np.zeros(n_leafs,dtype=int)
    for i in range(n_leafs):
        
        p_search_leaf = p_search[:,i] # leaf sample
        [bit_matrix_leaf,nBits_leaf] = localpopulat_gen_GAfile(N_prec,p_search_leaf,dim_populat) 
        
        if(i == 0): 
             bit_matrix = np.zeros((np.shape(bit_matrix_leaf),n_leafs))
             
        bit_matrix[:,0:len(bit_matrix_leaf[0,:]),i] = bit_matrix_leaf
        
        
        n_bits[i] = nBits_leaf
        