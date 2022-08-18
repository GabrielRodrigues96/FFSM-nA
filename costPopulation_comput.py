def costPopulation_comput(sign_cost,x_init,cost_ant,x_current,dim_populat,n_prmt): 
    
    import numpy as np    
    from cost_function import cost_function    
    
    x_position = np.zeros((dim_populat,n_prmt)) 
    local_cost = np.zeros(dim_populat) 
    
    
    ## cost computing 
     
    for i in range(dim_populat): 
        
      cost_current = cost_function(x_current[i,:]); 
        
      if(cost_ant[i] <= sign_cost*cost_current):
         x_position[i,:] = x_init[i,:]
         local_cost[i] = cost_ant[i] 
      else:
         x_position[i,:] = x_current[i,:]
         local_cost[i] = cost_current 
      
    
    indOpt_glob = (sign_cost*local_cost).argmin()
    
    
    bestCost_local = x_position; 
    bestCost_global = x_position[indOpt_glob,:]; 
    cost_ant = local_cost; 
    costOpt_global = local_cost[indOpt_glob]
    x_init = x_position;  

    

    return bestCost_local,bestCost_global,cost_ant,costOpt_global,x_init
       
