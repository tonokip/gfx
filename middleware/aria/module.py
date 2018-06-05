def loadModule():
	component = Module.CreateComponent("aria_gfx_library", "Aria", "/Graphics/Middleware/", "config/aria.py")
	component.setDisplayType("Graphics Library")
	component.addDependency("gfx_hal", "GFX HAL", False, True)
	component.addDependency("sys_input", "Input System Service", True, True)
	component.setDependencyEnabled("sys_input", False)
	component.addPlugin("plugins/mhgc.jar")
	component.addPlugin("plugins/libaria.jar")