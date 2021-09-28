from . import _main

@_main.route('/')
def index():
    return '<h1>hello word</h1>'