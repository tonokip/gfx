def loadModule():
	component = Module.CreateComponent("gfx_maxtouch_controller", "MaxTouch Controller", "/Input/Touch", "maxtouch_controller.py")
	component.setDisplayType("Touch Controller")
	component.addDependency("touch_panel", "Touch Panel", False)
	component.addDependency("i2c", "DRV_I2C", False)
	component.addDependency("sys_input", "Input System Service", True)