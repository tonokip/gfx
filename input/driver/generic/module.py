def loadModule():
	component = Module.CreateComponent("gfx_touch_controller", "Generic Touch Controller", "/Input/Touch/", "generic_controller.py")
	component.setDisplayType("Touch Controller")
	component.addDependency("gfx_display", "Graphics Display")
	component.addDependency("sys_input", "Input System Service", True)