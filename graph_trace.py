from graphviz import Digraph
from dataclasses import dataclass
from typing import Any, Dict
import copy

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
            action_properties_2 = copy.copy(action_properties)
            actions.append(action_properties)
            result = func(*args, **kwargs)
            action_properties.result = result
            action_properties_2.status = "<<<"
            actions.append(action_properties_2)
            return result
        return wrapped
    return my_decorator

def render_trace():
    tree = Digraph()
    open_close = [actions[0]]
    for i in range(1, len(actions) - 2):
        if actions[i].status == ">>>":
            tree.edge(f"label = {open_close[-1].label}, resalt = {open_close[-1].result}", f"label = {actions[i].label}, resalt = {actions[i].result}", f"args = {actions[i].args}")
            #print(f"label = {open_close[-1].label}, resalt = {open_close[-1].result}", actions[i].label, f"args = {actions[i].args}")
            open_close.append(actions[i])
        elif actions[i].status == "<<<":
            if len(open_close) > 1:
                del open_close[-1]
    tree.render('out/graph_trace.gv', view=True)