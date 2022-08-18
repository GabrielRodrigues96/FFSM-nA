def evolution_function_GAfile(n_bits,bit_matrix_mut,dim_populat,p_search,n_leafs,cost_matrix,bit_matrix): 
    
    from phenot_matrix_GAfile import phenot_matrix_GAfile; from costEval_population_GAfile import costEval_population_GAfile
    from extreme_individuals_GAfile import extreme_individuals_GAfile; from elitism_society_GAfile import elitism_society_GAfile
    
    from bestIndiv_evolvedSociety_GAfile import bestIndiv_evolvedSociety_GAfile
    
    # evalutation of pre-evolved population
    phenotype_mut = phenot_matrix_GAfile(n_bits,bit_matrix_mut,dim_populat,p_search,n_leafs)
    cost_mut = -costEval_population_GAfile(phenotype_mut)
    
    # search for extreme individuals (best and worst)
    [ind_best_local,ind_worst] = extreme_individuals_GAfile(dim_populat,cost_mut,cost_matrix) 
    
    # evolved population construction
    bit_matrix_evolved = elitism_society_GAfile(bit_matrix_mut,n_bits,n_leafs,bit_matrix,ind_best_local,ind_worst)
    
    # # EVALUATION OF EVOLVED SOCIETY
    phenotype_evolved = phenot_matrix_GAfile(n_bits,bit_matrix_evolved,dim_populat,p_search,n_leafs)
    cost_evolved = -costEval_population_GAfile(phenotype_evolved)
    
    # best solution
    best_solution,best_phenotype,best_cost = bestIndiv_evolvedSociety_GAfile(n_bits,n_leafs,dim_populat,cost_evolved,bit_matrix_evolved,p_search)


    return phenotype_evolved,best_solution,best_phenotype,best_cost,bit_matrix_evolved