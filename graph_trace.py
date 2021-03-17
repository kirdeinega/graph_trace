from graphviz import Digraph
from dataclasses import dataclass
from typing import Any, Dict
import copy
import time

actions = []

@dataclass
class ActionProperties:
    status: str
    label: str
    args: tuple
    kwargs: Dict[str, Any]
    result: Any = None
    result_time: Any = None

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
            start_time = time.time()
            actions.append(action_properties)
            result = func(*args, **kwargs)
            action_properties.result = result
            action_properties_2.status = "<<<"
            actions.append(action_properties_2)
            timetime = time.time() - start_time
            action_properties.result_time(timetime)
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
            tree.edge(f"label = {open_close[-1].label}, resalt = {open_close[-1].result}, time = {open_close[-1].result_time}", f"label = {actions[i].label}, resalt = {actions[i].result}, time = {actions[i].result_time}", f"args = {actions[i].args}, kwargs = {actions[i].kwargs}")
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