import inspect
import homework_6


def introspection_info(obj):
    info = {}
    info['type'] = type(obj)
    info['attributes'] = obj.__dir__
    info['methods'] = dir(obj)
    info['module'] = inspect.getmodule(obj)
    return info

number_info = introspection_info(homework_6.Figure)
print(number_info)




