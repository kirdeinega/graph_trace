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
            result = func(*args, **kwargs)
            action_properties.result = result
            action_properties.status = '<<<'
            actions.append(action_properties)
            return result
        return wrapped
    return my_decorator

def render_trace():
    tree = Digraph()
    open_close = [actions[0]]
    for i in range(1, len(actions) - 2):
        if actions[i].status == '>>>':
            tree.edge(f"label = {open_close[-1].label}, resalt = {open_close[-1].result}", actions[i].label, f"args = {actions[i].args}")
            print(f"label = {open_close[-1].label}, resalt = {open_close[-1].result}", actions[i].label, f"args = {actions[i].args}")
            open_close.append(actions[i])
        elif actions[i].status == '<<<':
            if len(open_close) > 1:
                del open_close[-1]
    tree.render('out/graph_trace.gv', view=True)