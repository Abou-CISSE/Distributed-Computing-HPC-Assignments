@types('float[:]', 'float[:]', 'int', 'int', 'float','float', 'float')
def solve_1d_nonlinearconv_pyccel(u, un, nt, nx, dt, dx):

    p=dt/dx
    for k in range(nt):
        for i in range(nx): un[i] = u[i]
        for i in range(1,nx):            
                u[i] = un[i]-p*un[i]*(un[i]-un[i-1]) 
    
    return 0
