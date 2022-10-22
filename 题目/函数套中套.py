def func1():
    print(123)
    def fun2():
        print(456)
        def func3():
            print(789)
        print(1)
        func3()
        print(2)
    print(3)
    fun2()
    print(4)


func1()
123
3
456
1
789
2
4