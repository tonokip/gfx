def loadModule():
	halComponent = Module.CreateGeneratorComponent("gfx_hal", "GFX HAL", "/Graphics/", "config/hal_common.py", "config/hal.py")
	halComponent.setDisplayType("Hardware Abstraction Layer")
	#halComponent.addCapability("gfx_hal", "GFX HAL", True)
	halComponent.addDependency("gfx_display_controller", "Display Controller", False)
	halComponent.addDependency("gfx_graphics_processor", "Graphics Processor", False)
	halComponent.addCapability("gfx_hal", "GFX HAL", False)
	halComponent.setInstanceHeaderText("Display List")
	halComponent.setInstanceText("Display ${INDEX}")
	#halComponent.addDependency("test dep", "Test Generic Dependency", True)
	
	#halComponent.addDependency("gfx_display_controller_1", "gfx_display_controller", False)
	#halComponent.setDependencyEnabled("gfx_display_controller_1", False)
	
	#halComponent.addDependency("gfx_display_controller_2", "gfx_display_controller", False)
	#halComponent.setDependencyEnabled("gfx_display_controller_2", False)
	
	#, "config/hal_common.py", 
