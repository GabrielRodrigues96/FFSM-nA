def roullete_build_GAfile(cost_matrix,dim_populat):
    
    import numpy as np
    
    sum_cost = sum(cost_matrix); 
    probab_ind = cost_matrix/sum_cost;
    
    acumulat_probab = 0; roulette_vec = np.zeros(dim_populat)
    for i in range(dim_populat):
        
        acumulat_probab = acumulat_probab + probab_ind[i] 
        
        roulette_vec[i] = acumulat_probab;
    
    return roulette_vec
