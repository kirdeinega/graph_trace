# graph_trace
Graph trace — визуализатор функций на Python. Данная программа визуализирует работу функций в Вашей программе на питон. 

***Как работать с данной библиотекой***

Для начала нужно скачать [этот файл](https://github.com/kirdeinega/graph_trace/blob/main/graph_trace.py). Далее в Вашем коде делаем импорт (*from graph_trace import trace, render_trace*). Далее над каждой функцией, которую Вы хотите визуализировать Вы пишите @trace(label="то название функции, которое Вы далее увидите в выводе"). Так же в конце программы напишите *render_trace()*. И всё можете увидеть результат.

***Теперь разберёмся что выводит эта программа:***

В овале:

* label - то самое название, которое Вы давали функции.
* result - то, что вернула функция.
* time - сколько времени проработала функция.

Рядом со стрелками:

* аргументы
* кейворд-аргументы

Так же если стрелка идёт от одного овала к другому, значит та функция от которой идёт стрелка вызвала функцию, к которой идёт стрелка.



***На данный момент для данного кода нет библиотеки.***


and in English
Graph trace is a Python function visualizer. This program visualizes the work of functions in your python program.

***How to work with this library***

First you need to download this file. Next, in your code, we do an import (from graph_trace import trace, render_trace). Next, above each function that you want to render, you write @trace(label="the name of the function that you will see next in the output"). Also write render_trace() at the end of the program. And you can see the result.

Now let's see what this program outputs:

In an oval:

* label is the same name you gave the function.
* result is what the function returned.
* time - how long the function worked.
* Next to the arrows:

arguments
* keyword arguments
* Also, if the arrow goes from one oval to another, then the function from which the arrow goes has called the function to which the arrow goes.

There is currently no library for this code.
