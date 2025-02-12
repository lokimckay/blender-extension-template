import bpy


class OBJMOVEX_PT_obj_properties_panel(bpy.types.Panel):
    bl_label = "Hello World"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "object"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.scale_y = 2.0
        row.operator("my_ops.move_x")


classes = (OBJMOVEX_PT_obj_properties_panel, )


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
