def loadModule():
	component = Module.CreateComponent("sys_input", "Input System Service", "/Input/Service", "sys_input.py")
	component.setDisplayType("System Service")
	component.addCapability("sys_input", "Input System Service", True)
	