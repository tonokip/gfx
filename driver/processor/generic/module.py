def loadModule():
	cntlComponent = Module.CreateComponent("gfx_generic_gpu", "Generic GPU", "/Graphics/Processor", "generic.py")
	cntlComponent.setDisplayType("Graphics Processor")
	cntlComponent.addCapability("gfx_controller", "Graphics Processor", False)