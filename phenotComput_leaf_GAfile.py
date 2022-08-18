def phenotComput_leaf_GAfile(bit_matrix_leaf,p_search_leaf,dim_populat): 
    
    import numpy as np
    from phenotype_computing_GAfile import phenotype_computing_GAfile
    
    dec_leaf = np.zeros(dim_populat)
    for k in range(dim_populat): 
        
        dec_leaf[k] = phenotype_computing_GAfile(bit_matrix_leaf[k,:],p_search_leaf) 
    
    



