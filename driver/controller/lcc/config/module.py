def loadModule():
	cntlComponent = Module.CreateComponent("gfx_lcc_controller", "LCC Controller", "/Graphics/Controllers", "config/lcc_controller.py")
	cntlComponent.setDisplayType("Graphics Display Controller")
	cntlComponent.addCapability("gfx_lcc_controller", "Display Controller", False)