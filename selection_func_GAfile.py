def selection_func_GAfile(cost_matrix,dim_populat,n_bits,n_leafs,bit_matrix,phenot_data):
    
    from roullete_build_GAfile import roullete_build_GAfile
    from roullete_spin_GAfile import roullete_spin_GAfile
    
    # ROULETTE BUILDING
    roulette_vec = roullete_build_GAfile(cost_matrix,dim_populat)

    # ROULLETE SPINNING
    bit_matrix_selected = roullete_spin_GAfile(n_bits,n_leafs,dim_populat,roulette_vec,bit_matrix,phenot_data) 

