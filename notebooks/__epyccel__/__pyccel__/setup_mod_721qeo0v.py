from setuptools import Extension, setup
import numpy

extension_mod = Extension("mod_721qeo0v",
		[ r'mod_721qeo0v_wrapper.c' ],
		extra_objects = [r'/home/cisse/github/Distributed-Computing-HPC-Assignments/notebooks/__epyccel__/__pyccel__/bind_c_mod_721qeo0v.o',
				r'/home/cisse/github/Distributed-Computing-HPC-Assignments/notebooks/__epyccel__/__pyccel__/mod_721qeo0v.o'],
		include_dirs = [r'/home/cisse/github/Distributed-Computing-HPC-Assignments/notebooks/__epyccel__/__pyccel__', numpy.get_include()],
		libraries = [r'gfortran'],
		library_dirs = [r'/usr/lib/gcc/x86_64-linux-gnu/9'],
		extra_link_args = [r'-O3',
				r'-fPIC',
				r'-I"/home/cisse/github/Distributed-Computing-HPC-Assignments/notebooks/__epyccel__/__pyccel__"'])

setup(name = "mod_721qeo0v", ext_modules=[extension_mod])