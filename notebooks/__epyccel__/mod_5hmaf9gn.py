@types('float[:]', 'float[:]', 'int', 'int', 'float','float', 'float')

def solve_1d_burger_pyccel(u, un, nt, nx, dt, dx, nu):
    k=nu*dt/(dx*dx)
    p=dt/dx
    for it in range(nt):
        for i in range(nx): un[i] = u[i]
        for i in range(1,nx-1):            
                u[i] = un[i]-p*un[i]*(un[i]-un[i-1])+k*(un[i+1]-2*un[i]+un[i-1]) 
        #périodique condition
        u[0]=un[0]-p*un[0]*(un[0]-un[nx-2])+k*(un[1]-2*un[0]+un[nx-2])
        u[nx-1]=u[0]
        
    return 0
