def costEval_population_GAfile(phenot_data):

    import numpy as np
    from cost_function import cost_function    
    
    cost_matrix = np.zeros(len(phenot_data[:,0]))
    
    for k in range(len(phenot_data[:,0])):
   
        individ_sample = phenot_data[k,:]; 
        cost_eval = cost_function(individ_sample) 
        cost_matrix[k] = cost_eval; 
   
    return cost_matrix
    
    
    

