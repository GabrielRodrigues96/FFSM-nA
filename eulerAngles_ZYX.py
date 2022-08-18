def eulerAngles_ZYX(phi,theta,psi):
    
    import numpy as np
    
    z_rot = np.array[[np.cos(psi), -np.sin(psi), 0],[np.sin(psi), np.cos(psi), 0],[ 0, 0, 1]]
    y_rot = np.array[[np.cos(theta), 0,  np.sin(theta)],[ 0, 1, 0],[ -np.sin(theta), 0, np.cos(theta)]] 
    x_rot = np.array[[1, 0, 0],[0, np.cos(phi), -np.sin(phi)],[0, np.sin(phi), np.cos(phi)]]
    
    eulerAngle_transf = np.matmul(np.matmul(z_rot,y_rot),x_rot)
    
    return eulerAngle_transf