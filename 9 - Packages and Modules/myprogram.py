# this is import from a module
from module import my_func

my_func()
print("\n"*5)
#this is import from package
from MyMainPackage import some_main_script
from MyMainPackage.SubPackage import mysubscript

some_main_script.report_main()
mysubscript.sub_report()