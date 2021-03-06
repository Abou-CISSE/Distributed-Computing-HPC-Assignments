from setuptools import Extension, setup
import numpy

extension_mod = Extension("mod_rm3vra2m",
		[ r'mod_rm3vra2m_wrapper.c' ],
		extra_objects = [r'/home/cisse/github/Distributed-Computing-HPC-Assignments/notebooks/__epyccel__/__pyccel__/bind_c_mod_rm3vra2m.o',
				r'/home/cisse/github/Distributed-Computing-HPC-Assignments/notebooks/__epyccel__/__pyccel__/mod_rm3vra2m.o'],
		include_dirs = [r'/home/cisse/github/Distributed-Computing-HPC-Assignments/notebooks/__epyccel__/__pyccel__', numpy.get_include()],
		libraries = [r'gfortran'],
		library_dirs = [r'/usr/lib/gcc/x86_64-linux-gnu/9'],
		extra_link_args = [r'-O3',
				r'-fPIC',
				r'-I"/home/cisse/github/Distributed-Computing-HPC-Assignments/notebooks/__epyccel__/__pyccel__"'])

setup(name = "mod_rm3vra2m", ext_modules=[extension_mod])