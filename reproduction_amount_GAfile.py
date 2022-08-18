def reproduction_amount_GAfile(dim_populat,cross_prob): 
    
    import numpy as np; import random
    
    cross_numbers = np.zeros(dim_populat)
    for k in range(dim_populat):     
        cross_numbers[k] = random.random() 
    
        
    count_cross = 0; ind_cross = np.zeros(dim_populat,dtype=int)
    for i in range(dim_populat):
       
        if(cross_numbers[i] <= (cross_prob / 100)): 
           count_cross = count_cross + 1;
            
           ind_cross[count_cross] = i
            
    if(count_cross == 0):
        ind_cross = 0;
    
    
    return ind_cross,count_cross
