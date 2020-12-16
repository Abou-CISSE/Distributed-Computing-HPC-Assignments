@types('float[:,:]', 'float[:,:]','float[:,:]','float[:,:]' , 'int' , 'float', 'float','float', 'float')
def solve_2d_burger_pyccel(u, un, v, vn, nt, dt, dx, dy, nu):
    
    
    ###Assign initial conditions
    ##set hat function I.C. : u(.5<=x<=1 && .5<=y<=1 ) is 2
    u[int(.5 / dy):int(1 / dy + 1),int(.5 / dx):int(1 / dx + 1)] = 2 
    ##set hat function I.C. : u(.5<=x<=1 && .5<=y<=1 ) is 2
    v[int(.5 / dy):int(1 / dy + 1),int(.5 / dx):int(1 / dx + 1)] = 2
    row, col = u.shape
    kx=dt/dx
    ky=dt/dy
    k1=nu*dt/dx**2
    k2=nu*dt/dy**2
    
    for k in range(nt):
        un=u.copy()
        vn=v.copy()
        for i in range(2, row):
            for j in range(2, col):
                                                          
                u[i-1,j-1]=(un[i-1,j-1] -
                            kx*un[i-1,j-1]*(un[i-1,j-1] - un[i-2,j-1]) -
                            ky*vn[i-1,j-1]*(un[i-1,j-1] - un[i-1,j-2]) +
                            k1*(un[i,j-1] - 2*un[i-1,j-1] + un[i-2,j-1]) +
                            k2*(un[i-1,j] - 2*un[i-1,j-1] + un[i-1,j-2]))
                
                v[i-1,j-1]=(vn[i-1,j-1] -
                            kx*un[i-1,j-1]*(vn[i-1,j-1] - vn[i-2,j-1]) -
                            ky*vn[i-1,j-1]*(vn[i-1,j-1] - vn[i-1,j-2]) +
                            k1*(vn[i,j-1] - 2*vn[i-1,j-1] + vn[i-2,j-1]) +
                            k2*(vn[i-1,j] - 2*vn[i-1,j-1] + vn[i-1,j-2]))
                            
                                
        u[0, :] = 1
        u[row-1, :] = 1
        u[:, 1] = 1
        u[:, col-1] = 1
        
        v[0, :] = 1
        v[row-1, :] = 1
        v[:, 1] = 1
        v[:, col-1] = 1
    
        
    return 0
