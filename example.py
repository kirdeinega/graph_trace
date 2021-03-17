from graph_trace import trace, render_trace

y = 'Hello World'
x = 1

@trace(label="f1")
def f1(x):
    return f2(x) + f3(y) + f4(y)

@trace(label="f2")
def f2(x):
    return f3(y) + str(x)

@trace(label="f3")
def f3(x):
    return str(5 * x)

@trace(label="f4")
def f4(y):
    return y * 2

f1(10)
render_trace()
