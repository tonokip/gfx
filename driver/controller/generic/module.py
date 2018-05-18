def loadModule():
	cntlComponent = Module.CreateComponent("gfx_generic_controller", "Generic Controller", "/Graphics/Driver", "generic_controller.py")
	cntlComponent.setDisplayType("Graphics Display Driver")
	cntlComponent.addCapability("gfx_generic_driver", "Display Driver", False)