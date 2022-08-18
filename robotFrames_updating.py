def robotFrames_updating(joint_angle,base_pos,base_angle,J2CM_linkLength,CM2J_linkLength,fixedRB_jointRot_1,b_0,n_link,n_arm): 
    
    import numpy as np    
    from eulerAngles_ZYX import eulerAngles_ZYX; from frameBuild_rigidBody import frameBuild_rigidBody; from frameBuild_inertial import frameBuild_inertial
        
    # PRE-ALLOCATION AND INITIALIZATION
    inertialRB_joint = np.zeros((4,4,max(n_link),3)) 
    inertialRB_link = np.zeros((4,4,max(n_link),3)) 
    
    fixedRB_joint = np.zeros((4,4,max(n_link),3))
    fixedRB_link = np.zeros((4,4,max(n_link),3))
    
    
    
    # robotic base
    inertialBase_jointRot = eulerAngles_ZYX(base_angle(1),base_angle(2),base_angle(3)) 
    inertialBase_joint = np.array[[inertialBase_jointRot, base_pos],[np.zeros(1,3),1]] 
    inertialBase_link = inertialBase_joint.copy() 
    
    inertialRB_joint[:,:,0,0] = inertialBase_joint.copy() 
    inertialRB_link[:,:,0,0] = inertialBase_link.copy()
    
        
    ## 
    
    for i_arm in range(n_arm):
    
           
        # FIXED-BODY FRAMES
        
            fixedRB_joint_loc,fixedRB_link_loc = frameBuild_rigidBody(n_link[i_arm],joint_angle[:,i_arm],J2CM_linkLength[:,i_arm],CM2J_linkLength[:,i_arm],fixedRB_jointRot_1[:,:,i_arm],b_0[:,i_arm]) 
            
        # INERTIAL FRAMES
            inertialRB_joint_loc = np.zeros((4,4,max(n_link)))
            inertialRB_link_loc = np.zeros((4,4,max(n_link)))
            
            
        
            inertialRB_joint_loc[:,:,0] = inertialBase_joint * fixedRB_joint_loc[:,:,0]
            
            inertialRB_joint_loc,inertialRB_link_loc = frameBuild_inertial(n_link[i_arm],fixedRB_joint_loc,fixedRB_link_loc,inertialRB_joint_loc,inertialRB_link_loc)
            
            
            fixedRB_joint[:,:,0:n_link[i_arm]+1,i_arm+1] = fixedRB_joint_loc 
            fixedRB_link[:,:,0:n_link[i_arm],i_arm+1] = fixedRB_link_loc
        
            inertialRB_joint[:,:,0:n_link[i_arm]+1,i_arm+1] = inertialRB_joint_loc
            inertialRB_link[:,:,:,i_arm+1] = inertialRB_link_loc 
        
