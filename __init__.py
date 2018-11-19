# 2018-11-19
# a plugin by ling

bl_info = {
    'name': 'ling tools',
    'category': 'All',
    'version': (1, 0, 0),
    'blender': (2, 79, 0)
}

modulesNames = [
    'pie_object_interaction',
    'pie_pivot_center',
    'pie_transform_orientation',
    'pie_shade',
]


# -------------------
# Don't touch below this: it's an auto-registering snippet code
# src: https://b3d.interplanety.org/en/creating-multifile-add-on-for-blender/
# -------------------

import sys
import importlib

modulesFullNames = {}
for currentModuleName in modulesNames:
    modulesFullNames[currentModuleName] = ('{}.{}'.format(__name__, currentModuleName))

for currentModuleFullName in modulesFullNames.values():
    if currentModuleFullName in sys.modules:
        importlib.reload(sys.modules[currentModuleFullName])
    else:
        globals()[currentModuleFullName] = importlib.import_module(currentModuleFullName)
        setattr(globals()[currentModuleFullName], 'modulesNames', modulesFullNames)


def register():
    for currentModuleName in modulesFullNames.values():
        if currentModuleName in sys.modules:
            if hasattr(sys.modules[currentModuleName], 'register'):
                sys.modules[currentModuleName].register()


def unregister():
    for currentModuleName in modulesFullNames.values():
        if currentModuleName in sys.modules:
            if hasattr(sys.modules[currentModuleName], 'unregister'):
                sys.modules[currentModuleName].unregister()


if __name__ == "__main__":
    register()