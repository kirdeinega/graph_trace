from graph_trace import trace, render_trace

y = 5
x = 10

@trace(label="f1")
def f1(x):
    q = 0
    for i in range(99000000):
        q += i
    return f2(x) + f3(x) + f4(y) + q

@trace(label="f2")
def f2(x):
    return y + x

@trace(label="f3")
def f3(x):
    return 5 * x

@trace(label="f4")
def f4(y):
    return y * 2

f1(10)
render_trace()
