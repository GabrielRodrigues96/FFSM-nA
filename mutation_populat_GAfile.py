def mutation_populat_GAfile(n_leafs,dim_populat,n_bits,bit_matrix_reprod,mut_prob): 
    
    import random; import numpy as np
    # mutation overwriting
    bit_matrix_mut = bit_matrix_reprod;
    
    mut_matrix = np.zeros((dim_populat,n_bits.max(),n_leafs))
    # mutation weighing
    for k in range(n_leafs):
        for i_pop in range(dim_populat): 
            for i_bits in range(n_bits[k]):
                mut_matrix[i_pop,i_bits,k] = random.random(i_pop,i_bits) 
    
    
    for k in range(n_leafs):
        for i in range(dim_populat):
            for j in range(n_bits):
                    
                # individuals for mutation
                if(mut_matrix[i,j,k] <= (mut_prob/100)): 
               
                    if(bit_matrix_mut[i,j,k] == 0):
                        bit_matrix_mut[i,j,k] = 1
                    else:
                        bit_matrix_mut[i,j,k] = 0
                    
                
    return bit_matrix_mut
            
        
    
    
    
