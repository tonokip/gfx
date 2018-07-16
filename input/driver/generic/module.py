def loadModule():
	component = Module.CreateComponent("gfx_touch_controller", "Generic Touch Controller", "/Input/Touch/", "generic_controller.py")
	component.setDisplayType("Touch Controller")
	component.addDependency("touch_panel", "Touch Panel")
	component.addDependency("sys_input", "Input System Service", True)