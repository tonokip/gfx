def loadModule():	
	cntlComponent = Module.CreateComponent("gfx_driver_ili9488", "ILI9488", "/Graphics/Driver", "config/ili9488_controller.py")
	cntlComponent.setDisplayType("ILI9488 Display Driver")
	cntlComponent.addCapability("gfx_driver_ili9488", "Display Driver", False)
	cntlComponent.addDependency("DRV_SPI", "DRV_SPI", False, True)
	#if Variables.get("__PROCESSOR") == "ATSAME70Q21B":
		#cntlComponent.addDependency("SMC", "SMC", False)
