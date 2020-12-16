@types('float[:,:]', 'float[:,:]','float[:,:]','float[:,:]' , 'int','float', 'float','float', 'float')
def solve_2d_nonlinearconv_pyccel(u, un, v, vn, nt, dt, dx, dy, c):

    ###Assign initial conditions
    ##set hat function I.C. : u(.5<=x<=1 && .5<=y<=1 ) is 2
    u[int(.5 / dy):int(1 / dy + 1), int(.5 / dx):int(1 / dx + 1)] = 2
    ##set hat function I.C. : v(.5<=x<=1 && .5<=y<=1 ) is 2
    v[int(.5 / dy):int(1 / dy + 1), int(.5 / dx):int(1 / dx + 1)] = 2
    row, col = u.shape
    
    kx=dt/dx
    ky=dt/dy
    
    for k in range(nt):
        un=u.copy()
        vn=v.copy()
        for i in range(1, row-1):
            for j in range(1, col-1):
                                                          
                u[i,j]=(un[i,j] -
                        kx*un[i,j]*(un[i,j] - un[i-1,j]) -
                        ky*vn[i,j]*(un[i,j] - un[i,j-1]))
                
                u[i,j]=(vn[i,j] -
                        kx*un[i,j]*(vn[i,j] - vn[i-1,j]) -
                        ky*vn[i,j]*(vn[i,j] - vn[i,j-1]))
                
                                
        u[0, :] = 1
        u[:, 0] = 1
        u[row-1, :] = 1
        u[:, col-1] = 1
        
        v[0, :] = 1
        v[:, 0] = 1
        v[row-1, :] = 1
        v[:, col-1] = 1
        
        
    return 0
