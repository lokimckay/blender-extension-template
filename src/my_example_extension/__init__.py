from . import (ui, ops)
modules = [ui, ops]

bl_info = {
    "name": "Example Extension",
    "blender": (4, 3, 0),
    "category": "3D View",
}


def register():
    hot_reload()
    for module in modules:
        if hasattr(module, "register"):
            module.register()
    print("[Example Extension] registered")


def unregister():
    for module in modules:
        if hasattr(module, "unregister"):
            module
    print("[Example Extension] unregistered")


def hot_reload():
    # Refresh submodules during development
    from .env import ENV
    print("RELOADING@")
    if ENV == "DEV":
        import importlib
        for module in modules:
            print("Reloading module", module)
            importlib.reload(module)
