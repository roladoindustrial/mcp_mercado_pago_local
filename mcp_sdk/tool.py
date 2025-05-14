def tool(name: str, description: str = ""):
    def decorator(func):
        func.__tool__ = True
        func.__name__ = name
        func.__doc__ = description
        return func
    return decorator
