def phenotype_computing_GAfile(bit_num,p_search_leaf):

    from bit2dec_GAfile import bit2dec_GAfile    

    dec_num = bit2dec_GAfile(bit_num) 
    
    sol_fen = p_search_leaf[0] + dec_num*((p_search_leaf[1] - p_search_leaf[0])/(2**(len(bit_num)) - 1))
    
    return sol_fen
    
    




