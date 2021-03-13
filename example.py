from graph_trace import trace, render_trace

y = 10
x = 10

@trace(label="f1")
def f1(x):
    return f2(x) + f3(y) + f4(x, y)

@trace(label="f2")
def f2(x):
    return x + 1

@trace(label="f3")
def f3(y):
    return f4(y, x) * 2

@trace(label="f4")
def f4(y, x):
    return y ** x

f1(10)
render_trace()
