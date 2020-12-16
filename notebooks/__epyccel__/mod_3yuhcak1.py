@types('float[:]', 'float[:]', 'int', 'int', 'float','float', 'float')

def solve_1d_diff_pyccel(u, un, nt, nx, dt, dx, nu):
    
    for it in range(nt):
        for i in range(nx): un[i] = u[i]
        for i in range(1,nx-1):            
                u[i] = un[i]+(nu*dt/(dx*dx))*(un[i+1]-2*un[i]+un[i-1]) 
        u[nx-1]=u[nx-2]    
    
    return 0
