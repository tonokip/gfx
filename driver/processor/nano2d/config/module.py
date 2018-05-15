def loadModule():
	cntlComponent = Module.CreateComponent("gfx_nano2d_controller", "Nano2D GPU", "/Graphics/Processor", "config/nano2d.py")
	cntlComponent.setDisplayType("Graphics Processor")
	cntlComponent.addCapability("gfx_nano2d_controller", "Graphics Processor", False)