#!/usr/bin/env python

import sys, os
from distutils.core import setup, Extension

assert len(sys.argv) == 1
sys.argv.append("build")

setup(name="CModule",
	  version="0.9.0",
	  description="rdiff-backup's C component",
	  ext_modules=[Extension("C", ["cmodule.c"],
							 define_macros=[("_LARGEFILE_SOURCE", 1),
											("_FILE_OFFSET_BITS", 64),
											("_LARGE_FILES", 1)]),
				   Extension("_librsync",
							 ["_librsyncmodule.c"],
							 libraries=["rsync"])])

assert not os.system("mv build/lib.linux-i686-2.2/C.so .")
assert not os.system("mv build/lib.linux-i686-2.2/_librsync.so .")
assert not os.system("rm -rf build")