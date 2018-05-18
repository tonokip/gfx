def loadModule():
	component = Module.CreateComponent("gfx_mxt336_controller", "MaxTouch 336T Controller", "/Input/Touch", "mxt336t_controller.py")
	component.setDisplayType("Touch Controller")
	component.addDependency("gfx_display", "Graphics Display", False)
	component.addDependency("sys_input", "Input System Service", True)
	