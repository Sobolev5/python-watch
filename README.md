# python-watch

Simple and useful python decorator for real-time logging.

```no-highlight
https://github.com/Sobolev5/python-watch
```

# How to use it

To install run:
```no-highlight
pip install python-watch
```


Add the following line at the top of your file:
```python
from python_watch.functions import watch 
```


And simple wrap your function or class method:
```python
@watch
def print_text(text):
    print(text)

print_text('hello_world')    
```


Open your development console and see the result:
```python
""" /my_project/news/views.py => print_text: Line number 15 """
args: ('hello_world')
```

That's all.