def test2():
    print(x)

def test1():
    global x
    x=10
    print(x)
x=20
test1()
test2()