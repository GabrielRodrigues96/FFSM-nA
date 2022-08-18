def PSO_optimization_redundancy(flg_optType,tol_stop,n_red,n_prmt,p_search,w_inert,c1,c2,dim_populat): 
    
    import numpy as np
    from PSO_optimization import PSO_optimization; from get_signCost import get_signCost

    sign_cost = get_signCost(flg_optType)    

    cost_strg = np.zeros((tol_stop,n_red)); bestSolut_strg = np.zeros((tol_stop,n_prmt,n_red))
    cost_red_strg = np.zeros(n_red); bestSolut_red_strg = np.zeros((n_prmt,n_red))

    for i_red in range(n_red): 
        cost_strg_loc,bestSolut_strg_loc = PSO_optimization(dim_populat,n_prmt,tol_stop,flg_optType,p_search,w_inert,c1,c2)

        # DATA STORAGE
        cost_strg[:,i_red] = cost_strg_loc.copy()
        bestSolut_strg[:,:,i_red] = bestSolut_strg_loc.copy()

        ind_opt_loc = (sign_cost*cost_strg_loc).argmin()
        cost_red_strg[i_red] = cost_strg_loc[ind_opt_loc]
        bestSolut_red_strg[:,i_red] = bestSolut_strg_loc[ind_opt_loc,:]


    ind_opt_red = (sign_cost * cost_red_strg).argmin()
    cost_opt_red = cost_red_strg[ind_opt_red]; bestSolut_opt_red = bestSolut_red_strg[:,ind_opt_red]


    return bestSolut_opt_red,cost_opt_red,ind_opt_red,bestSolut_red_strg,cost_red_strg,cost_strg,bestSolut_strg