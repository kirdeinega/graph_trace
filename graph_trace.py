from graphviz import Digraph
from dataclasses import dataclass
from typing import Any, Dict


actions = []
@dataclass
class ActionProperties:
    status: str
    label: str
    args: tuple
    kwargs: Dict[str, Any]
    result: Any = None

def trace(label: str):
    def my_decorator(func):
        def wrapped(*args, **kwargs):
            action_properties = ActionProperties(
                status = ">>>",
                label = label,
                args = args,
                kwargs = kwargs
            )
            actions.append(action_properties)
            res = func(*args, **kwargs)
            action_properties.res = res
            actions.append(("<<<",label))
            return res
        return wrapped
    return my_decorator


def render_trace():
    tree = Digraph()
    open_close = [actions[0]]
    for i in range(1, len(actions) - 2):
        if actions.status == '>>>':
            tree.edge(str(open_close[-1][1]), str(actions[i][1]), str(actions[i][2]))
            open_close.append(actions[i])
        if actions[i][0] == '<<<':
            if len(open_close) > 1:
                del open_close[-1]
    tree.render('out/graph_trace.gv', view=True)