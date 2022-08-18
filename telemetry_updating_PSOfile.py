def telemetry_updating_PSOfile(x_swarm,v_swarm,bestCost_local,bestCost_global,r1_m,r2_m,w_inert,c1,c2,dim_populat,n_pso,n_prmt,p_search): 
    
    import numpy as np
    from sat_particle_PSOfile import sat_particle_PSOfile
    
    for k in range(dim_populat): 

        v_swarm[k,:,n_pso+1] = w_inert*v_swarm[k,:,n_pso] + c1*(np.matmul(r1_m,(bestCost_local[k,:] - x_swarm[k,:,n_pso]))) + c2*(np.matmul(r2_m,(bestCost_global - x_swarm[k,:,n_pso])))
        x_swarm[k,:,n_pso+1] = x_swarm[k,:,n_pso] + v_swarm[k,:,n_pso+1]; 

        # particle saturation
        for i_sat in range(n_prmt): 
   
            x_swarm[k,i_sat,n_pso+1],v_swarm[k,i_sat,n_pso+1] = sat_particle_PSOfile(x_swarm[k,i_sat,n_pso+1],v_swarm[k,i_sat,n_pso+1],p_search[1,i_sat],p_search[0,i_sat]) 


    return x_swarm,v_swarm