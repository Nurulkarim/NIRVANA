def first(func):
    def second():
        print("hello world")  #  decorator is changing a function from
        func()                #  outside without modifying it .
    return second()


@first
def third():
    print("i am new here")


