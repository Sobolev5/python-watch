from termcolor import cprint
from functools import wraps


def unwrap(func):
    while hasattr(func, '__wrapped__'):
        func = func.__wrapped__
    return func


def watch(func):
    @wraps(func)
    def wrapper(*args, **kwargs): 
        process_stdout = f'\n""" {func.__code__.co_filename} => {func.__name__}: Line number {func.__code__.co_firstlineno} """'
        if args: 
            process_stdout += f"\nargs: {args}"
        if kwargs: 
            process_stdout += f"\nkwargs: {kwargs}"
        if args and isinstance(args, tuple) and hasattr(args[0], 'method') and args[0].method:
            # django part
            request = args[0]           
            if request.GET: 
                process_stdout += f"\nrequest.GET: {request.GET}"
            if request.POST: 
                process_stdout += f"\nrequest.POST: {request.POST}"     
        cprint(process_stdout, 'magenta', attrs=['bold'])   
        response = func(*args, **kwargs)                            
        return response 
    return wrapper
