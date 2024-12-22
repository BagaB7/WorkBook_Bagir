def test_function():

    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()

test_function()


p = 'п'
def test_func_1():
    def f1():
        p1 = 'р'
        def f2():
            p2 = 'и'
            def f3():
                p3 = 'в'
                def f4():
                    p4 = 'е'
                    def f5():
                        p5 = 'т'
                        print(p+p1+p2+p3+p4+p5)
                    f5()
                f4()
            f3()
        f2()
    f1()

test_func_1()