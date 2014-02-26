########################################################################################################################
# File name: __init__.py
# Copyright(C) 2007-2013, A10 Networks Inc. All rights reserved.
# Software for all A10 products contain trade secrets and confidential
# information of A10 Networks and its subsidiaries and may not be
# disclosed, copied, reproduced or distributed to anyone outside of
# A10 Networks without prior written consent of A10 Networks, Inc.
########################################################################################################################
import sys
import os
from os import path
import imp


__all__ = []
__pkg_path = path.abspath(__path__[0]) #parent directory

def load_modules(path):
    for (path, _, files) in os.walk(os.path.abspath(path)):
        if (path.__eq__(__pkg_path)):
            continue
        if ( os.path.isdir(path) and os.path.exists(path + os.sep + "__init__.py")):
            for file in files:
                if not file.endswith(".py"):
                    continue
                if file.__eq__("__init__.py"):
                    continue
                modname = file.replace(".py","")
                f, filename, desc = imp.find_module(modname, [path])
                module = imp.load_module(modname, f, filename, desc)
                #append all toplevel modules and packages to __all__
                if not "." in modname:
                    __all__.append(modname)
                    globals()[modname] = module
                #set everything else as an attribute of their parent package
                else:
                    #get the toplevel package from globals()
                    pkg_name, rest = modname.split(".", 1)
                    pkg = globals()[pkg_name]
                    if not pkg :
                       print "package reference %s  was null" % pkg_name
                    #recursively get the modules parent package via getattr
                    while "." in rest:
                        subpkg, rest = rest.split(".", 1)
                        pkg = getattr(pkg, subpkg)
                    #set the module (or package) as an attribute of its parent package
                    setattr(pkg, rest, module)
load_modules(__pkg_path + "/common")
load_modules(__pkg_path)

