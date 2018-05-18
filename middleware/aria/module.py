def loadModule():
	component = Module.CreateComponent("aria_gfx_library", "Aria", "/Graphics/Middleware/", "aria/aria.py")
	component.setDisplayType("Graphics Library")
	component.addDependency("gfx_hal", "GFX HAL")
	component.addDependency("sys_input", "Input System Service", True)