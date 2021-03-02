from graphviz import Digraph
from dataclasses import dataclass
from typing import Any, Dict

actions = []
functions = []
#@dataclass
#class ActionProperties:
#    label: str
#    status: str
 #   args: tuple
  #  kwargs: Dict[str, Any]
   # result: Any = None

#actions.append(action_properties)
#res = 100500
#action_properties.result = res
#action_properties.status = 'close'
#print(actions.status)

def trace(label: str):
    def my_decorator(func):
        def wrapped(*args, **kwargs):
            actions.append((">>>",label, args, kwargs))  #(">>>",label, args, kwargs)
            res = func(*args, **kwargs)
            functions.append(res)
            actions.append(("<<<",label))
            return res
        return wrapped
    return my_decorator


def print_trace():
    print("trace:")
    print(*actions, sep='\n')
    print("end of trace")

#########################################################################
# from ... import trace

y = 2

@trace(label="f1")
def f1(x):
    return f2(x) + f3(y) + f4(x)

@trace(label="f2")
def f2(x):
    return x + 1

@trace(label="f3")
def f3(y):
    return f4(y) * 2

@trace(label="f4")
def f4(y):
    return y ** 3
#print_trace()

###########################################################################

print(f1(10))
tree = Digraph()
actions.append(functions)
print(functions)
open_close = [actions[0]]
for i in range(1, len(actions) - 2):
    if actions[i][0] == '>>>':
        tree.edge(str(open_close[-1][1]), str(actions[i][1]), str(actions[i][2]))
        open_close.append(actions[i])
    if actions[i][0] == '<<<':
        if len(open_close) > 1:
            del open_close[-1]
tree.render('out/graph_trace.gv', view=True)
#f2(x) = 11, f3(y) = 8, f4(x) = 4