from distutils.core import setup
import py2exe
setup(console=['crypt.py'])
windows = [{
    'script': "crypt.py",
    'uac_info': "requireAdministrator",
},]
