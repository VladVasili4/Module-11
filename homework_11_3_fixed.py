import inspect
import homework_6

def introspection_info(obj):
    info = {}
    info['type'] = type(obj)
    info['attributes'] = dir(obj)
    info['methods'] = []
    info['module'] = []
    info['name'] = obj.__name__
    for name in dir(obj):
        attr = getattr(obj, name)
        if callable(attr):
            info['methods'].append(attr)
        if inspect.ismodule(type(attr)):
            info['module'].append(attr)
    return info

x = introspection_info(homework_6.Figure)
print(f' introspection(homework_6.Figure) : {x}')




