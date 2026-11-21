# Ganesha
# import printing_functions

# printing_functions.greeting()
# printing_functions.sayHari()

def fun1():
    print("In fun1")

    import printing_functions

    printing_functions.greeting()
    printing_functions.sayHari()


def fun2():
    print("In fun2")

    from printing_functions import greeting, sayHari

    greeting()
    sayHari()


def fun3():
    print("In fun3")

    from printing_functions import greeting as g, sayHari as h

    g()
    h()


def fun4():
    print("In fun4")

    import printing_functions as pf

    pf.greeting()
    pf.sayHari()


def fun5():
    print("In fun5")

    try:
        # from printing_functions import *
        from printing_functions import greeting, sayHari
    except SyntaxError as e:
        print(f"Exception {e} while importing * inside a function")
    else:
        greeting()
        sayHari()
    finally:
        print("finally")


def main():
    fun1()
    fun2()
    fun3()
    fun4()
    fun5()


if __name__ == '__main__':
    main()