def get_signCost(flg_optType): 
    
    
    if(flg_optType == 1): # maximization
        sign_cost = -1
    else:
        if(flg_optType == 0): # minimization
            sign_cost = 1
    
    
    return sign_cost