def crossover_leaf_GAfile(reprodMates_ind,bit_matrix_leaf,n_bits_leaf): 
    
    
    import random; import numpy as np
    
    bit_matrix_reprod_leaf = bit_matrix_leaf; 
    
    for i in range(len(reprodMates_ind[0,:])): 
   
        cut_point = np.ceil(random.random()*n_bits_leaf); 
   
        temp_sect = bit_matrix_leaf[reprodMates_ind[0,i],cut_point:]
    
        bit_matrix_reprod_leaf[reprodMates_ind[0,i],cut_point:] = bit_matrix_leaf[reprodMates_ind[1,i],cut_point:]; 
        bit_matrix_reprod_leaf[reprodMates_ind[1,i],cut_point:] = temp_sect; 

    return bit_matrix_reprod_leaf

