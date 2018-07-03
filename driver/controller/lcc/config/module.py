def loadModule():	
	cntlComponent = Module.CreateComponent("gfx_driver_lcc", "LCC ", "/Graphics/Driver", "config/lcc_controller.py")
	cntlComponent.setDisplayType("LCC Display Driver")
	cntlComponent.addDependency("sys_dma", "sys_dma", True)
	cntlComponent.addDependency("sys_int", "sys_int", True)
	cntlComponent.addCapability("gfx_driver_lcc", "Display Driver", False)
	cntlComponent.addDependency("SMC", "SMC", False)
