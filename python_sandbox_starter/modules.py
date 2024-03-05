# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

#Built-in modules
from datetime import date
from camelcase import CamelCase

today = date.today()
print('Today is:', today)

#Install a module using pip3 - without being in a virtual env, the module is installed globally but can be uninstalled using pip3 uninstall. Example module install command, pip3 install camelcase
cc = CamelCase() #Initialize the method from the module
str = 'this string is originally all lowercase'
print(cc.hump(str))