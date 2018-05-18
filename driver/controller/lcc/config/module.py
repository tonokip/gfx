def loadModule():
	if Variables.get("__PROCESSOR") != "PIC32CZ2038CA70144":
		return
	
	cntlComponent = Module.CreateComponent("gfx_ca70_lcc", "LCC ", "/Graphics/Driver", "config/lcc_controller.py")
	cntlComponent.setDisplayType("CA70 LCC Display Driver")
	cntlComponent.addDependency("sys_dma", "sys_dma", True)
	cntlComponent.addCapability("gfx_lcc_driver", "Display Driver", False)