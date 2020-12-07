from importlib import import_module
from .settings import MODULES

routes = []
for module in MODULES:
    try:
        module = 'modules.{}.urls'.format(module)
        module = import_module(module)
        routes += module.routes
    except Exception as e:
        print(e)
        print("HEREEEEEEEEEEEEEEE", module)
        pass