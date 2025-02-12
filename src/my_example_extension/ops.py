import bpy


class ObjectMoveX(bpy.types.Operator):
    """My Object Moving Script"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "my_ops.move_x"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Move X by One"         # Display name in the interface.

    # execute() is called when running the operator.
    def execute(self, context):

        # The original script
        scene = context.scene
        for obj in scene.objects:
            obj.location.x += 1.0

        # Lets Blender know the operator finished successfully.
        return {'FINISHED'}


classes = (
    ObjectMoveX,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
