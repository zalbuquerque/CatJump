from functools import wraps

def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'[LOG] Executando: {func.__name__}')
        return func(*args, **kwargs)
    return wrapper