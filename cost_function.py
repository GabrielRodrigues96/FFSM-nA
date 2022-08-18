def cost_function(pp_data): 
    
    x = pp_data[0]
    y = pp_data[1]
    
    cost_value = 5 - ( x**2 + y**2)
    
    return cost_value