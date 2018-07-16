def loadModule():
	halComponent = Module.CreateComponent("gfx_hal", "GFX Core", "/Graphics/", "config/hal.py")
	halComponent.setDisplayType("Hardware Abstraction Layer")
	halComponent.addDependency("gfx_display", "Graphics Display", False, False)
	halComponent.addDependency("gfx_display_driver", "Display Driver", False, True)
	halComponent.addDependency("gfx_graphics_processor", "Graphics Processor", False, False)
	halComponent.addCapability("gfx_hal", "GFX HAL", False)
	halComponent.addPlugin("plugins/displaymanager.jar")

