from graphviz import Digraph
from dataclasses import dataclass
from typing import Any, Dict
import copy
import time
import timeit

actions = []

@dataclass
class ActionProperties:
    status: str
    label: str
    args: tuple
    kwargs: Dict[str, Any]
    result: Any = None
    time: Any = None

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
            a = timeit.default_timer()
            actions.append(action_properties)
            result = func(*args, **kwargs)
            action_properties.result = result
            action_properties_2.status = "<<<"
            actions.append(action_properties_2)
            time = timeit.default_timer()-a
            action_properties.time = time
            return result
        return wrapped
    return my_decorator

x = []

def render_trace():
    tree = Digraph()
    open_close = [actions[0]]
    for i in range(1, len(actions) - 2):
        if actions[i].status == ">>>":
            wer = True
            tree.edge(f"label = {open_close[-1].label}, \n result = {open_close[-1].result[0]}, \n time = {open_close[-1].time}", 
            f"label = {actions[i].label}, \n result = {actions[i].result}, \n time = {actions[i].time}", 
            f"args = {actions[i].args}, \n kwargs = {actions[i].kwargs}"
            )
            #print(f"label = {open_close[-1].label}, resalt = {open_close[-1].result}", actions[i].label, f"args = {actions[i].args}")
            open_close.append(actions[i])
        elif actions[i].status == "<<<":
            wer = False
            if len(open_close) > 1:
                del open_close[-1]
        if wer:
            x.append(copy.deepcopy(tree))
    for w in range(len(x)):
        x[w].render(f'out/graph_trace{[w]}.gv', view = True)