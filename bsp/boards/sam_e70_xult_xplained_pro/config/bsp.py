def resetPins(pinConfigs):
	for pinConfig in pinConfigs:
		print("Resetting " + pinConfig["name"])
		Database.clearSymbolValue("core", "PIN_" + str(pinConfig["pin"]) + "_FUNCTION_NAME")
		Database.setSymbolValue("core", "PIN_" + str(pinConfig["pin"]) + "_FUNCTION_TYPE", "Available")
		Database.clearSymbolValue("core", "PIN_" + str(pinConfig["pin"]) + "_DIR")
		Database.clearSymbolValue("core", "PIN_" + str(pinConfig["pin"]) + "_LAT")

def configurePins(pinConfigs):
	for pinConfig in pinConfigs:
		print("Configuring " + pinConfig["name"])
		Database.setSymbolValue("core", "PIN_" + str(pinConfig["pin"]) + "_FUNCTION_NAME", pinConfig["name"])
		Database.setSymbolValue("core", "PIN_" + str(pinConfig["pin"]) + "_FUNCTION_TYPE", pinConfig["type"])
		Database.setSymbolValue("core", "PIN_" + str(pinConfig["pin"]) + "_DIR", pinConfig["direction"])
		Database.setSymbolValue("core", "PIN_" + str(pinConfig["pin"]) + "_LAT", pinConfig["latch"])

def enableILI9488SPIPins(enable):
	ili9488SPI4PinConfigs = [{"pin": 31, "name": "BSP_ILI9488_SPI_DCX", "type": "GPIO", "direction": "Out", "latch": "High"},
				{"pin": 52, "name": "BSP_ILI9488_SPI_CSX", "type": "GPIO", "direction": "Out", "latch": "High"},
				{"pin": 60, "name": "SPI0_SPCK", "type": "SPI0_SPCK", "direction": "", "latch": ""},
				{"pin": 63, "name": "SPI0_MOSI", "type": "SPI0_MOSI", "direction": "", "latch": ""},
				{"pin": 65, "name": "SPI0_MISO", "type": "SPI0_MISO", "direction": "", "latch": ""},
				{"pin": 102, "name": "BSP_DisplayBacklight", "type": "GPIO", "direction": "Out", "latch": "High"},
				{"pin": 103, "name": "BSP_DisplayReset", "type": "GPIO", "direction": "Out", "latch": "High"}]
	resetPins(ili9488SPI4PinConfigs)
	if (enable == True):
		configurePins(ili9488SPI4PinConfigs)

def enableSPIInterface(enable):
	componentIDTable = ["spi0", "drv_spi", "drv_spi_0"]
	autoConnectTable = [["drv_spi_0", "drv_spi_SPI_dependency", "spi0", "SPI_0"],
						["gfx_driver_ili9488", "DRV_SPI", "drv_spi_0", "drv_spi"]]
	if (enable == True):
		res = Database.activateComponents(componentIDTable)
		res = Database.connectDependencies(autoConnectTable)
	elif (enable == False):
		res = Database.deactivateComponents(componentIDTable)
	enableILI9488SPIPins(enable)

def configureDisplayInterface(interface):
	print("Configuring for " + str(interface) + "Interface.")
	if (interface == "SPI 4-line"):
		enableSPIInterface(True)
	elif (interface == "Parallel 16-bit"):
		enableSPIInterface(False)
	elif (interface == "Parallel 8-bit"):
		enableSPIInterface(False)

def onDisplayInterfaceSelected(interfaceSelected, event):
	newDisplayInterface= interfaceSelected.getComponent().getSymbolByID("DisplayInterface").getValue()
	currDisplayInterface = interfaceSelected.getComponent().getSymbolByID("currDisplayInterface").getValue()
	interfaceSelected.getComponent().getSymbolByID("currDisplayInterface").setValue(event["value"], 1)
	configureDisplayInterface(str(newDisplayInterface))

def activateDefaultComponents(bspComponent):
	print("activating default components")
	orderedComponentIDTable = ["HarmonyCore", "gfx_driver_ili9488", "gfx_disp_atmxt-xpro_320x480", "gfx_hal", "aria_gfx_library"]
	res = Database.activateComponents(orderedComponentIDTable)
	
	autoConnectTable = [["gfx_hal", "gfx_display", "gfx_disp_atmxt-xpro_320x480", "gfx_display"],
					["gfx_hal", "gfx_display_driver", "gfx_driver_ili9488", "gfx_driver_ili9488"],
					["aria_gfx_library", "gfx_hal", "gfx_hal", "gfx_hal"]]

	deactivateIDTable = ["FreeRTOS"]

	res = Database.connectDependencies(autoConnectTable)
	res = Database.deactivateComponents(deactivateIDTable)
	
	#DisplayInterface = bspComponent.createComboSymbol("DisplayInterface", None, ["SPI 4-line", "Parallel 16-bit", "Parallel 8-bit"])
	DisplayInterface = bspComponent.createComboSymbol("DisplayInterface", None, ["SPI 4-line"]) #Only SPI is supported for now
	DisplayInterface.setLabel("Display Interface")
	DisplayInterface.setDescription("Configures the display interface to the maXTouch Xplained Pro display.")
	DisplayInterface.setDefaultValue("SPI 4-line")
	DisplayInterface.setDependencies(onDisplayInterfaceSelected, ["DisplayInterface"])
	
	# Shadow display interface symbol
	currDisplayInterface = bspComponent.createComboSymbol("currDisplayInterface", None, ["SPI 4-line", "Parallel 16-bit", "Parallel 8-bit"])
	currDisplayInterface.setDefaultValue("SPI 4-line")
	currDisplayInterface.setVisible(False)
	
	configureDisplayInterface(str(currDisplayInterface.getValue()))

def instantiateComponent(bspComponent):
	BSP_NAME = "sam_e70_xult_xplained_pro"
	
	activateDefaultComponents(bspComponent)

	pinTypes = []
	pinAttributs = []

	execfile(Variables.get("__BSP_DIR") + "/boards/config/bsp_common.py")