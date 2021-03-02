from graphviz import Digraph
from typing import Any, Dict


actions = []
functions = []

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


def render_trace():
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
