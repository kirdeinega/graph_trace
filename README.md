Graph trace is a Python function visualizer. This program visualizes the work of functions in your python program.

How to work with this library

First you need to download this file. Next, in your code, we do an import (from graph_trace import trace, render_trace). Next, above each function that you want to render, you write @trace(label="the name of the function that you will see next in the output"). Also write render_trace() at the end of the program. And you can see the result.

Now let's see what this program outputs:

In an oval:

label is the same name you gave the function.
result is what the function returned.
time - how long the function worked.
Next to the arrows:

arguments
keyword arguments
Also, if the arrow goes from one oval to another, then the function from which the arrow goes has called the function to which the arrow goes.

There is currently no library for this code.
