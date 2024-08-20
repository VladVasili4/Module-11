import inspect
from optparse import OptionParser
from pprint import pprint
# from homework_6 import Figure
import homework_6

def introspection(obj):
    print(f'Имя = {obj.__name__}')
    print(f'Тип = {type(obj)}')
    print('Атрибуты :')
    for i in dir(obj):
        print(f'{i} = {type(i)}')
    print(f'Методы : {inspect.getmembers(obj, predicate=inspect.ismethod)}')
    print(f'Модуль объекта : {inspect.getmodule(obj)}')

    print(f'Модуль = {inspect.ismodule(obj)}')
    print(f'Класс = {inspect.isclass(obj)}')
    print(f'Метод = {inspect.ismethod(obj)}')
    print(f'Функция = {inspect.isfunction(obj)}')
    print(f'Фрейм = {inspect.isframe(obj)}')
    print(f'Код = {inspect.iscode(obj)}')
    print(f'Аттрибут Куб есть? {hasattr(obj, 'Cube')}')
    print(f'Аттрибут Призма есть? {hasattr(obj, 'Prism')}')
    if hasattr(obj, 'Cube'):
        print(f'Данные Аттрибута Куб :\n {getattr(obj, 'Cube')}')
    print(f'Документация :\n {inspect.getdoc(obj)}')
    print(f'Комментарии :\n {inspect.getcomments(obj)}')

    pprint(help(obj))

k = introspection(homework_6)
