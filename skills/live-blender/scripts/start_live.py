# GUI Blender on the pod: install and enable the MCP for Blender add-on, start its server on 127.0.0.1:9876.
import os, shutil, addon_utils, bpy
here = os.path.dirname(os.path.abspath(__file__))
dst = bpy.utils.user_resource("SCRIPTS", path="addons", create=True)
shutil.copy(os.path.join(here, "blender_mcp.py"), os.path.join(dst, "blender_mcp.py"))
import sys
if dst not in sys.path:
    sys.path.append(dst)                      # the folder was created after start-up, so Blender is not scanning it yet
addon_utils.modules_refresh()
print("MCP add-on enabled:", bool(addon_utils.enable("blender_mcp", default_set=True, persistent=True)), flush=True)
bpy.context.preferences.view.smooth_view = 0

# Nick, 15 Nov 2026: "after 10 idle minutes please shut the pod down". The pod guard on the 3D System box stops the pod
# when ~/.wb_last_use is 10 min old and the pod is not busy, so every connector command writes it: a live Blender
# somebody talks to stays up, one nobody talks to goes. (The keepalive of `workbench run` no longer counts as use.)
import pathlib
import blender_mcp
LAST_USE = pathlib.Path.home() / ".wb_last_use"
if not getattr(blender_mcp.BlenderMCPServer.execute_command, "_marks_use", False):
    _execute = blender_mcp.BlenderMCPServer.execute_command

    def execute_command(self, command):
        try:
            LAST_USE.touch()
        except OSError:
            pass
        return _execute(self, command)
    execute_command._marks_use = True
    blender_mcp.BlenderMCPServer.execute_command = execute_command
print("connector commands mark the pod in use:", blender_mcp.BlenderMCPServer.execute_command._marks_use, flush=True)

def start():
    sc = bpy.context.scene
    if sc is None:
        return 0.5
    sc.blendermcp_auto_start_server = True
    try:
        bpy.ops.blendermcp.start_server()
    except Exception as exc:
        print("start_server:", exc, flush=True)
    print("MCP server running:", getattr(sc, "blendermcp_server_running", None), flush=True)
    return None
bpy.app.timers.register(start, first_interval=2.0)


def watchdog():
    """Restart the MCP server if it stopped (it did once after a failed long call)."""
    sc = bpy.context.scene
    server = getattr(bpy.types, "blendermcp_server", None)
    if sc is not None and (server is None or not server.running):
        try:
            import blender_mcp
            if server is None:
                server = blender_mcp.BlenderMCPServer(host="127.0.0.1", port=9876)
                bpy.types.blendermcp_server = server
            server.start()
            print("watchdog: MCP server restarted", server.running, flush=True)
        except Exception as exc:
            print("watchdog:", exc, flush=True)
    return 5.0
bpy.app.timers.register(watchdog, first_interval=10.0, persistent=True)
