
bl_info = {
    "name": "Transform orientation Menu: Key: ', key'",
    "description": "Transform orientation modes",
    "author": "lingtalfi",
    "version": (1, 0, 0),
    "blender": (2, 79, 0),
    "location": ", key", # azerty keyboard friendly
    "warning": "",
    "wiki_url": "",
    "category": "3d View"
    }

import bpy
from bpy.types import Menu


# Pie Pivot Mode
class VIEW3D_PIE_transform_orientation_of(Menu):
    bl_label = "Transform orientation"
    bl_idname = "view3d.transform_orientation_of"

    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()
        pie.prop(context.space_data, "transform_orientation", expand=True)


classes = (
    VIEW3D_PIE_transform_orientation_of,
    )

addon_keymaps = []


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    wm = bpy.context.window_manager

    if wm.keyconfigs.addon:
        # Align
        km = wm.keyconfigs.addon.keymaps.new(name='Object Non-modal')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'COMMA', 'PRESS')
        kmi.properties.name = "view3d.transform_orientation_of"
        addon_keymaps.append((km, kmi))


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        for km, kmi in addon_keymaps:
            km.keymap_items.remove(kmi)
    addon_keymaps.clear()


if __name__ == "__main__":
    register()
