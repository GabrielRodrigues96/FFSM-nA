def failCase_return_GAfile(phenot_data,bit_matrix,dim_populat,cost_matrix,p_search,n_bits): 

    from phenotype_computing_GAfile import phenotype_computing_GAfile

    phenotype_evolved = phenot_data.copy()
    bit_matrix_evolved = bit_matrix.copy() 
    
    best_cost = -1e6; 
    for i in range(dim_populat):
   
        if(cost_matrix[i] >= best_cost):
            ind_best_local = i
            best_cost = cost_matrix[i] 
        
    
    best_solution = bit_matrix[ind_best_local,:] 
    best_phenotype = phenotype_computing_GAfile(best_solution[0:n_bits(0),0],p_search[:,0])    
    
    return phenotype_evolved,bit_matrix_evolved,best_solution,best_phenotype,best_cost
