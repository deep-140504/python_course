from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets
def func(x):
    return x ** 2

interact(func, x = 10)

interact(func, x = True)

@interact(x = True, y = 1.0)
def g(x, y):
  return (x, y ** 2)