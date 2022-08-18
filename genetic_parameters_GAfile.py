def genetic_parameters_GAfile(): 
     
    from search_def_GAfile import search_def_GAfile
        
    generation_number = 100 # number of generations
    dim_populat = 100 # population dimension 
    
    cross_prob = 70 # crossover probability (%) 
    mut_prob = 1 # mutation probability (%)
    
    N_prec = 10 # number of precision decimal digits
    
    p_search,n_leafs = search_def_GAfile() # search domain
    
    return generation_number,dim_populat,cross_prob,mut_prob,N_prec,p_search,n_leafs