# import library
import bpy
from bpy.types import Panel,Operator,PropertyGroup

# basic info
bl_info = {
   "name": "ymg_fbx_exporter",
   "author": "ymgmcmc",
   "version": (1, 0, 1),
   "blender": (3, 2, 0),
   "location": "3D View",
   "description": "ymgmcmc",
   "warning": "",
   "support": "TESTING",
   "wiki_url": "",
   "tracker_url": "",
   "category": "Object"
}

#init props
class MyInputs(PropertyGroup):
   filepath:bpy.props.StringProperty(
      name="Directory",
      subtype="FILE_PATH"
   )
   useselected:bpy.props.BoolProperty(
        name="only_selected",
        default=False
    )
#init panels
class MainPanel(Panel):
   bl_label = "ymg_fbx_exporter"
   bl_space_type = "VIEW_3D"
   bl_region_type = "UI"
   bl_category = "ymgaddon"
   
  
   def draw(self, context):
       layout = self.layout
       layout.prop(context.scene.myinputs,"filepath")
       layout.prop(context.scene.myinputs,"useselected")
       layout.operator(FBX_Export.bl_idname, text="export")
#export fbx
class FBX_Export(Operator):
   bl_idname = "ymg_fbx_exporter.operator" #use lower scale
   bl_label = "Export"
   filepath = "/"
   
   def execute(self, context):
       bpy.ops.export_scene.fbx(
          filepath = context.scene.myinputs.filepath,
          check_existing=False,
          use_selection = context.scene.myinputs.useselected,
          apply_scale_options='FBX_SCALE_ALL',
          bale_space_transform=True,
          )
       print("exported:",context.scene.myinputs.filepath)
       return {"FINISHED"}
   
#class list for register
classes = [MyInputs,MainPanel,FBX_Export]

#register to blender
def register():
   for cls in classes:
       bpy.utils.register_class(cls)
   bpy.types.Scene.myinputs = bpy.props.PointerProperty(type=MyInputs)


#unregister from blender
def unregister():
   for cls in classes:
       bpy.utils.unregister_class(cls)
       del bpy.types.Scene.myinputs

#entry point
if __name__ == "__main__":
   register()