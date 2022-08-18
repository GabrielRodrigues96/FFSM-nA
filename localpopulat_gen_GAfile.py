def localpopulat_gen_GAfile(N_prec,p_search_leaf,dim_populat): 
    
    # POPULATION GENERATION

    n_lim = np.log2((p_search_leaf[1] - p_search_leaf[0])*10**(N_prec) +1 ) 
    n_bits = np.ceil(n_lim);


    for k = 1:dim_populat
   
        for j = 1:n_bits
       
            bit_matrix_leaf(k,j) = round(rand);
        
        end
    
    end


