def PSO_optimization(dim_populat,n_prmt,tol_stop,flg_optType,p_search,w_inert,c1,c2): 
    
    import numpy as np; import random
    from costPopulation_comput import costPopulation_comput; from telemetry_updating_PSOfile import telemetry_updating_PSOfile
    from get_signCost import get_signCost

    v_swarm = np.zeros((dim_populat,n_prmt,tol_stop + 1))
    x_swarm = np.zeros((dim_populat,n_prmt,tol_stop + 1))  
    
    cost_strg = np.zeros(tol_stop); 
    bestSolut_strg = np.zeros((tol_stop,n_prmt)); 
    r1_coef = np.zeros(n_prmt); 
    r2_coef = np.zeros(n_prmt); 
    
    sign_cost = get_signCost(flg_optType)    
    
    # initialize population
    
    populat_init = np.zeros((dim_populat,n_prmt))
    for i_prmt in range(n_prmt): 
        
        for i_pop in range(dim_populat): 
            populat_init[i_pop,i_prmt] = p_search[0,i_prmt] + (p_search[1,i_prmt] - p_search[0,i_prmt])*random.random()
        
    x_swarm[:,:,0] = populat_init.copy(); x_init = populat_init.copy()
    cost_ant = 1e6 * np.ones(dim_populat)
    
    # RUN SWARM
    
    
    for n_pso in range(tol_stop): 
    
          for i_r in range(n_prmt): 
                   
                r1_coef[i_r] = random.random()
                r2_coef[i_r] = random.random()      
            
          r1_m = np.diag(r1_coef)
          r2_m = np.diag(r2_coef) 
            
          # cost computing
          bestCost_local,bestCost_global,cost_ant,costOpt_global,x_init = costPopulation_comput(sign_cost,x_init,cost_ant,x_swarm[:,:,n_pso],dim_populat,n_prmt)
          
          # telemetry update
          x_swarm,v_swarm = telemetry_updating_PSOfile(x_swarm,v_swarm,bestCost_local,bestCost_global,r1_m,r2_m,w_inert,c1,c2,dim_populat,n_pso,n_prmt,p_search) 
              
          
          cost_strg[n_pso] = costOpt_global
          bestSolut_strg[n_pso,:] = bestCost_global.copy()
     
        
    return cost_strg,bestSolut_strg