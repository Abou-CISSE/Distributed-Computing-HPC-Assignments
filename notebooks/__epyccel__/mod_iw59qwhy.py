@types('float[:,:]', 'float[:,:]','float[:,:]','float[:,:]' , 'int','float', 'float','float', 'float')
def solve_2d_linearconv_pyccel(u, un, nt, dt, dx, dy, c):
   
    row, col = u.shape

    kx=c*dt/dx
    ky=c*dt/dy
        
    for k in range(nt):
        un=u.copy()
        for i in range(1, row-1):
            for j in range(1, col-1):
                                                          
                u[i,j]=(un[i,j] -
                        kx*(un[i,j] - un[i-1,j]) -
                        ky*(un[i,j] - un[i,j-1]))
                
                                
        u[0, :] = 1
        u[:, 0] = 1
        u[row-1, :] = 1
        u[:, col-1] = 1
               
    return 0
