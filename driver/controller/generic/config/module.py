def loadModule():
	cntlComponent = Module.CreateComponent("gfx_generic_controller", "Generic Controller", "/Graphics/Controllers", "config/generic_controller.py")
	cntlComponent.setDisplayType("Graphics Display Controller")
	cntlComponent.addCapability("gfx_generic_controller", "Display Controller", False)