def roullete_spin_GAfile(n_bits,n_leafs,dim_populat,roulette_vec,bit_matrix,phenot_data):
    
    
    import numpy as np; import random
    
    spin_numbers = np.zeros(dim_populat)
    for k in range(dim_populat):     
        spin_numbers[k] = random.random() 
    
    ind_vec = np.zeros(dim_populat,dtype=int)
    for i in range(dim_populat):
            
        dif_vec = roulette_vec - spin_numbers[i]; 
        index_numbers = np.argsort(abs(dif_vec));
        
        
        ind_vec[i] = index_numbers[0]
         
    bit_matrix_selected = np.zeros((dim_populat,n_bits.max(),n_leafs)); phenot_selected = np.zeros(dim_populat,n_leafs)  
    for i in range(dim_populat):
     for j in range(n_leafs):
         
        bit_matrix_selected[i,0:n_bits[j],j] = bit_matrix[ind_vec[i],0:n_bits[j],j] 
        phenot_selected[i,j] = phenot_data[ind_vec[i],j]
        
    return bit_matrix_selected
      
    