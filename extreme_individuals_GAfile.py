def extreme_individuals_GAfile(dim_populat,cost_mut,cost_matrix): 
    
    
    ## SEARCH FOR BEST SOLUTION (evolved population)
    ind_best_local = cost_mut.argmax()
    
    ## SEARCH FOR WORST SOLUTION (initial population)
    ind_worst = cost_matrix.argmin()
    
    return ind_best_local,ind_worst
    
