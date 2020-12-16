import numpy as np
from mpi4py import MPI
import time
COMM=MPI.COMM_WORLD
size=COMM.Get_size()
rank=COMM.Get_rank()
def compute_integrale_trapeze(x, y, nbi):
    integrale = 0.
    for i in range(nbi):
        trap = (x[i+1]-x[i])/2 * (y[i]+y[i+1])
        integrale = integrale + trap               
    return integrale


t=time.time()
xmax=3*np.pi/2
xmin=0
nbx = 1000
dx=(xmax-xmin)/(nbx-1)
nbi=int((nbx-1)/size)+(size==(rank+1))*((nbx-1)%size)

if rank==0:
	xmin = xmax-nbi*dx
if rank==1:
	xmin = rank*nbi*dx
	xmax = (rank+1)*nbi*dx

x = np.linspace(xmin, xmax, nbi+1)
y = np.cos(x)

integrale=COMM.reduce(compute_integrale_trapeze(x, y, nbi), MPI.SUM, root=0)

if rank==0:
	runtime=time.time()-t
	print("integrale = " ,integrale, "in ",runtime," s")
