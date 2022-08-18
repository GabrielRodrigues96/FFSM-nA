def search_def_GAfile(): 
           
    import numpy as np
    
    ## PARAMETRIC DOMAIN
    n_prmt = 2
    p_search = np.zeros((2,n_prmt))
    
    p_search[:,0] = [0,0.1] 
    p_search[:,1] = [-3,3] 
    
    ## DATA COMPACTING
    
    n_leafs = len(p_search[0,:])
    
    return p_search,n_leafs
