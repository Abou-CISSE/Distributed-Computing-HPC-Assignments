@types('float[:,:]', 'float[:,:]' , 'int','float', 'float','float', 'float')
def solve_2d_diff_pyccel(u, un, nt, dt, dx, dy, nu):
    row, col = u.shape
    
    ##Assign initial conditions
    #set hat function I.C. : u(.5<=x<=1 && .5<=y<=1 ) is 2
    u[int(.5 / dy):int(1 / dy + 1),int(.5 / dx):int(1 / dx + 1)] = 2
    
    
    
    kx=nu*dt/dx**2
    ky=nu*dt/dy**2
    
    for k in range(nt):
        un=u.copy()
        
        for i in range(2, row):
            for j in range(2, col):
                                                          
                u[i-1,j-1]=(un[i-1,j-1] +
                            kx*(un[i,j-1] - 2*un[i-1,j-1] + un[i-2,j-1]) +
                            ky*(un[i-1,j] - 2*un[i-1,j-1] + un[i-1,j-2]))
             
            
                                
        u[0, :] = 1
        u[row-1, :] = 1
        u[:, 1] = 1
        u[:, col-1] = 1
        
        
        
        
    return 0
