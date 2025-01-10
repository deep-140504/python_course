def func():
    print("func in one.py")
print("top level in one.py")
def func1():
    pass
def func2():
    pass
if __name__ == "__main__":
    print("one.py is being run directly")
    func1()
    func2()
    # so the use of __name__ property is while executing larger python scripts, u can avoid the exection of certain snippet where the script is imported
    # like, here func1() and func2() will only be executed if the "python one.py" is called directly 
else:
    print("\n", __name__)
    #here the value of __name__ becomes one since it is imported in two
    print("one.py has been imported")

