from setuptools import Extension, setup
import numpy

extension_mod = Extension("mod_q60u7i98",
		[ r'mod_q60u7i98_wrapper.c' ],
		extra_objects = [r'/home/cisse/github/Distributed-Computing-HPC-Assignments/notebooks/__epyccel__/__pyccel__/bind_c_mod_q60u7i98.o',
				r'/home/cisse/github/Distributed-Computing-HPC-Assignments/notebooks/__epyccel__/__pyccel__/mod_q60u7i98.o'],
		include_dirs = [r'/home/cisse/github/Distributed-Computing-HPC-Assignments/notebooks/__epyccel__/__pyccel__', numpy.get_include()],
		libraries = [r'gfortran'],
		library_dirs = [r'/usr/lib/gcc/x86_64-linux-gnu/9'],
		extra_link_args = [r'-O3',
				r'-fPIC',
				r'-I"/home/cisse/github/Distributed-Computing-HPC-Assignments/notebooks/__epyccel__/__pyccel__"'])

setup(name = "mod_q60u7i98", ext_modules=[extension_mod])