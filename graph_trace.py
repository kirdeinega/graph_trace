from graphviz import Digraph
from typing import Any, Dict


actions = []
@dataclass
class ActionProperties:
    status: str
    status_2: str
    label: str
    args: tuple
    kwargs: Dict[str, Any]
    result: Any = None

def trace(label: str):
    def my_decorator(func):
        def wrapped(*args, **kwargs):
            action_properties = ActionProperties(
                status = ">>>",
                lable = lable,
                args = args
                kwargs = kwargs
            )
            actions.append(action_properties)
            res = func(*args, **kwargs)
            action_properties.append(res=res)
            actions.append(("<<<",label))
            return res
        return wrapped
    return my_decorator


def render_trace():
    tree = Digraph()
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