def natural_selection_GAfile(mut_prob,n_bits,bit_matrix,dim_populat,p_search,n_leafs,cross_prob): 
    
    from phenot_matrix_GAfile import phenot_matrix_GAfile; from costEval_population_GAfile import costEval_population_GAfile
    from selection_func_GAfile import selection_func_GAfile; from reproduction_amount_GAfile import reproduction_amount_GAfile
    from failCase_return_GAfile import failCase_return_GAfile; from reprod_mates_GAfile import reprod_mates_GAfile
    from crossover_execution_GAfile import crossover_execution_GAfile
    from mutation_populat_GAfile import mutation_populat_GAfile
    from evolution_function_GAfile import evolution_function_GAfile
    
    phenot_data = phenot_matrix_GAfile(n_bits,bit_matrix,dim_populat,p_search,n_leafs)

    # COST EVALUATION (toward minimization)
    cost_matrix = -costEval_population_GAfile(phenot_data); 

    # SELECTION
    bit_matrix_selected = selection_func_GAfile(cost_matrix,dim_populat,n_bits,n_leafs,bit_matrix,phenot_data); 

    # REPRODUCTION
    
    # # MATES FOR REPRODUCTION
    # fittest individuals
    ind_cross,count_cross = reproduction_amount_GAfile(dim_populat,cross_prob) 


    if(count_cross < 1): # reprodution failed
       [phenotype_evolved,bit_matrix_evolved,best_solution,best_phenotype,best_cost] = failCase_return_GAfile(phenot_data,bit_matrix,dim_populat,cost_matrix,p_search); 
   
    
    else: # reprodution mates existent
    
    # combination of individuals
        reprodMates_ind = reprod_mates_GAfile(ind_cross) 

    # # CROSSOVER
        bit_matrix_reprod = crossover_execution_GAfile(bit_matrix_selected,n_bits,n_leafs,reprodMates_ind); 


        bit_matrix_mut = mutation_populat_GAfile(n_leafs,dim_populat,n_bits,bit_matrix_reprod,mut_prob) 

    # EVALUATION AND ELITISM
    
    phenotype_evolved,best_solution,best_phenotype,best_cost,bit_matrix_evolved = evolution_function_GAfile(n_bits,bit_matrix_mut,dim_populat,p_search,n_leafs,cost_matrix,bit_matrix);


    return phenotype_evolved,bit_matrix_evolved,best_solution,best_phenotype,best_cost