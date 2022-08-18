def bit2dec_GAfile(bit_num): 
    
        
    sum_dec = 0;
    for i in range(len(bit_num)): 
       
        sum_dec = sum_dec + 2**(i)*bit_num[len(bit_num) - (i+1)] 
    
    
    dec_num = sum_dec
    
    return dec_num