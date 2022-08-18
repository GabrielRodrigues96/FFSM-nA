def sat_particle_PSOfile(x_part,v_part,tLimit_sup,tLimit_inf): 
    
        
    if(x_part >= tLimit_sup):
        x_sat = tLimit_sup
        v_sat = 0
        
    else:
    
        if(x_part <= tLimit_inf):
            x_sat = tLimit_inf
            v_sat = 0
        else:
    
    
            if((x_part <= tLimit_sup) and (x_part >= tLimit_inf)):
                
                x_sat = x_part
                v_sat = v_part
                
    return x_sat,v_sat 
