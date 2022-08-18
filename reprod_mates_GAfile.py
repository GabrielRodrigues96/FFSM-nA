def reprod_mates_GAfile(ind_cross):
        
    import numpy as np
    
    # parity analysis
    if(np.mod(len(ind_cross),2) == 0): 
       indCross_even = ind_cross
    else:
        indCross_even = ind_cross[1:len(ind_cross)-1] 
    
    
    # mates indices
    count_mat = -1; reprodMates_ind = np.zeros((2,len(indCross_even)))
    for i in range(0,len(indCross_even),2):
        count_mat = count_mat + 1;
        
        reprodMates_ind[0,count_mat] = indCross_even[i] 
        reprodMates_ind[1,count_mat] = indCross_even[i+1]
       
        
    reprodMates_ind = reprodMates_ind[0:count_mat+1]
    
    return reprodMates_ind
