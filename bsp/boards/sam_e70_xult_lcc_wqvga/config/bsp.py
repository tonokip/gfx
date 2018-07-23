def activateDefaultComponents(bspComponent):
	print("activating default components")
	componentIDTable = ["smc0", "gfx_hal", "gfx_driver_lcc", "gfx_disp_pdatm4301b_480x272", "aria_gfx_library"]
	autoConnectTable = [["gfx_driver_lcc", "SMC_CS", "smc0", "smc_cs0"],
					["gfx_hal", "gfx_display_driver", "gfx_driver_lcc", "gfx_driver_lcc"],
					["gfx_hal", "gfx_display", "gfx_disp_pdatm4301b_480x272", "gfx_display"],
					["aria_gfx_library", "gfx_hal", "gfx_hal", "gfx_hal"]]

	touchComponentsIDTable = ["twihs0", "drv_i2c", "drv_i2c0", "gfx_maxtouch_controller", "sys_input"]
	touchComponentConnectionTable = [["drv_i2c_0", "drv_i2c_I2C_dependency", "twihs0", "TWIHS_0"],
									["gfx_maxtouch_controller", "i2c", "drv_i2c_0", "drv_i2c"],
									["gfx_maxtouch_controller", "touch_panel", "gfx_disp_pdatm4301b_480x272", "touch_panel"]]

	res = Database.activateComponents(componentIDTable)
	res = Database.connectDependencies(autoConnectTable)
	
	res = Database.activateComponents(touchComponentsIDTable)
	res = Database.connectDependencies(touchComponentConnectionTable)

def activateSDRAMComponent(bspComponent):
	componentIDTable = ["SDRAMC_0"]
	
	res = Database.activateComponents(componentIDTable)

def configurePins(pinConfigs):
	for pinConfig in pinConfigs:
		print("Configuring " + pinConfig["name"])
		Database.clearSymbolValue("core", "PIN_" + str(pinConfig["pin"]) + "_FUNCTION_NAME")
		Database.clearSymbolValue("core", "PIN_" + str(pinConfig["pin"]) + "_FUNCTION_TYPE")
		Database.clearSymbolValue("core", "PIN_" + str(pinConfig["pin"]) + "_DIR")
		Database.clearSymbolValue("core", "PIN_" + str(pinConfig["pin"]) + "_LAT")
		
		Database.setSymbolValue("core", "PIN_" + str(pinConfig["pin"]) + "_FUNCTION_NAME", pinConfig["name"])
		Database.setSymbolValue("core", "PIN_" + str(pinConfig["pin"]) + "_FUNCTION_TYPE", pinConfig["type"])
		Database.setSymbolValue("core", "PIN_" + str(pinConfig["pin"]) + "_DIR", pinConfig["direction"])
		Database.setSymbolValue("core", "PIN_" + str(pinConfig["pin"]) + "_LAT", pinConfig["latch"])

def configureSDRAMPins(bspComponent):
	sdramPinConfigs = [{"pin": 120, "name": "EBI_A2/SDA0", "type": "EBI_A2/SDA0", "direction": "", "latch": ""},
				{"pin": 122, "name": "EBI_A3/SDA1", "type": "EBI_A3/SDA1", "direction": "", "latch": ""},
				{"pin": 124, "name": "EBI_A4/SDA2", "type": "EBI_A4/SDA2", "direction": "", "latch": ""},
				{"pin": 127, "name": "EBI_A5/SDA3", "type": "EBI_A5/SDA3", "direction": "", "latch": ""},
				{"pin": 130, "name": "EBI_A6/SDA4", "type": "EBI_A6/SDA4", "direction": "", "latch": ""},
				{"pin": 133, "name": "EBI_A7/SDA5", "type": "EBI_A7/SDA5", "direction": "", "latch": ""},
				{"pin": 13, "name": "EBI_A8/SDA6", "type": "EBI_A8/SDA6", "direction": "", "latch": ""},
				{"pin": 12, "name": "EBI_A9/SDA7", "type": "EBI_A9/SDA7", "direction": "", "latch": ""},
				{"pin": 76, "name": "EBI_A10/SDA8", "type": "EBI_A10/SDA8", "direction": "", "latch": ""},
				{"pin": 16, "name": "EBI_A11/SDA9", "type": "EBI_A11/SDA9", "direction": "", "latch": ""},
				{"pin": 88, "name": "EBI_SDA10", "type": "EBI_SDA10", "direction": "", "latch": ""},
				{"pin": 22, "name": "EBI_A16/BA0", "type": "EBI_A16/BA0", "direction": "", "latch": ""},
				{"pin": 57, "name": "EBI_SDCK", "type": "EBI_SDCK", "direction": "", "latch": ""},
				{"pin": 84, "name": "EBI_SDCKE", "type": "EBI_SDCKE", "direction": "", "latch": ""},
				{"pin": 18, "name": "EBI_NCS1/SDCS", "type": "EBI_NCS1/SDCS", "direction": "", "latch": ""},
				{"pin": 74, "name": "EBI_CAS", "type": "EBI_CAS", "direction": "", "latch": ""},
				{"pin": 78, "name": "EBI_RAS", "type": "EBI_RAS", "direction": "", "latch": ""},
				{"pin": 108, "name": "EBI_SDWE", "type": "EBI_SDWE", "direction": "", "latch": ""},
				{"pin": 111, "name": "EBI_A0/NBS0/DQM0", "type": "EBI_A0/NBS0/DQM0", "direction": "", "latch": ""},
				{"pin": 106, "name": "EBI_NWR1/NBS1/DQM1", "type": "EBI_NWR1/NBS1/DQM1", "direction": "", "latch": ""},
				]
	configurePins(sdramPinConfigs)

def configureLCCPins(bspComponent):
	lccPinConfigs = [{"pin": 11, "name": "EBI_D0", "type": "EBI_D0", "direction": "", "latch": ""},
				{"pin": 38, "name": "EBI_D1", "type": "EBI_D1", "direction": "", "latch": ""},
				{"pin": 39, "name": "EBI_D2", "type": "EBI_D2", "direction": "", "latch": ""},
				{"pin": 40, "name": "EBI_D3", "type": "EBI_D3", "direction": "", "latch": ""},
				{"pin": 41, "name": "EBI_D4", "type": "EBI_D4", "direction": "", "latch": ""},
				{"pin": 58, "name": "EBI_D5", "type": "EBI_D5", "direction": "", "latch": ""},
				{"pin": 54, "name": "EBI_D6", "type": "EBI_D6", "direction": "", "latch": ""},
				{"pin": 48, "name": "EBI_D7", "type": "EBI_D7", "direction": "", "latch": ""},
				{"pin": 4, "name": "EBI_D8", "type": "EBI_D8", "direction": "", "latch": ""},
				{"pin": 6, "name": "EBI_D9", "type": "EBI_D9", "direction": "", "latch": ""},
				{"pin": 7, "name": "EBI_D10", "type": "EBI_D10", "direction": "", "latch": ""},
				{"pin": 10, "name": "EBI_D11", "type": "EBI_D11", "direction": "", "latch": ""},
				{"pin": 27, "name": "EBI_D12", "type": "EBI_D12", "direction": "", "latch": ""},
				{"pin": 28, "name": "EBI_D13", "type": "EBI_D13", "direction": "", "latch": ""},
				{"pin": 49, "name": "EBI_D14", "type": "EBI_D14", "direction": "", "latch": ""},
				{"pin": 45, "name": "EBI_D15", "type": "EBI_D15", "direction": "", "latch": ""},
				{"pin": 82, "name": "EBI_NWR0/NWE", "type": "EBI_NWR0/NWE", "direction": "", "latch": ""},
				{"pin": 15, "name": "BSP_LCD_HSYNC", "type": "GPIO", "direction": "Out", "latch": "High"},
				{"pin": 19, "name": "BSP_LCD_RESET", "type": "GPIO", "direction": "Out", "latch": "High"},
				{"pin": 67, "name": "BSP_LCD_VSYNC", "type": "GPIO", "direction": "Out", "latch": "High"},
				{"pin": 86, "name": "BSP_LCD_BACKLIGHT", "type": "GPIO", "direction": "Out", "latch": "High"},
				{"pin": 94, "name": "BSP_LCD_DE", "type": "GPIO", "direction": "Out", "latch": "High"},
				]
	configurePins(lccPinConfigs)

def configureTouchControllerPins(bspComponent):
	touchCtrlrPinConfigs = [{"pin": 91, "name": "TWIHS0_TWD0", "type": "TWIHS0_TWD0", "direction": "", "latch": ""},
							{"pin": 77, "name": "TWIHS0_TWCK0", "type": "TWIHS0_TWCK0", "direction": "", "latch": ""},
							{"pin": 71, "name": "BSP_MAXTOUCH_CHG", "type": "GPIO", "direction": "In", "latch": ""},
							]
	configurePins(touchCtrlrPinConfigs)

def onSDRAMEnabled(SDRAMFrameBufferSelected, event):
	print("BSP Configure SDRAM")
	configureSDRAMPins(SDRAMFrameBufferSelected.getComponent())
	activateSDRAMComponent(SDRAMFrameBufferSelected.getComponent())

def instantiateComponent(bspComponent):
	BSP_NAME = "sam_e70_xult_lcc_wqvga"
	
	activateDefaultComponents(bspComponent)
	
	configureLCCPins(bspComponent)
	configureTouchControllerPins(bspComponent)

	#configureSDRAMPins(bspComponent)
	#activateSDRAMComponent(bspComponent)
	
	#enableSDRAM = bspComponent.createBooleanSymbol("EnableSDRAM", None)
	#enableSDRAM.setLabel("Enable SDRAM?")
	#enableSDRAM.setDependencies(onSDRAMEnabled, ["EnableSDRAM"])
	
	pinTypes = []
	pinAttributs = []

	# pinAttributes = [{"attrib":"type", "symbol":"BSP_CUSTOM_TYPE", "label":"Type Name"},
		# {"attrib":"mode", "symbol":"BSP_CUSTOM_MODE", "label":"Mode"},
		# {"attrib":"dir", "symbol":"BSP_CUSTOM_DIR", "label":"Direction"},
		# {"attrib":"lat", "symbol":"BSP_CUSTOM_LAT", "label":"Initial Latch Value"},
		# {"attrib":"od", "symbol":"BSP_CUSTOM_OD", "label":"Open Drain"},
		# {"attrib":"cn", "symbol":"BSP_CUSTOM_CN", "label":"Change Notice"},
		# {"attrib":"pu", "symbol":"BSP_CUSTOM_PU", "label":"Pull Up"},
		# {"attrib":"pd", "symbol":"BSP_CUSTOM_PD", "label":"Pull Down"},
		# {"attrib":"int", "symbol":"BSP_CUSTOM_PIO_INTERRUPT", "label":"PIO Interrupt"}]

	# pinTypes = [{"type":"LED_AH", "mode":"DIGITAL", "dir":"OUT"},
		# {"type":"LED_AL", "mode":"DIGITAL", "dir":"OUT"},
		# {"type":"SWITCH_AH", "mode":"DIGITAL"},
		# {"type":"SWITCH_AL", "mode":"DIGITAL"},
		# {"type":"VBUS_AH", "mode":"DIGITAL", "dir":"OUT"},
		# {"type":"VBUS_AL", "mode":"DIGITAL", "dir":"OUT"}]

	execfile(Variables.get("__BSP_DIR") + "/boards/config/bsp_common.py")
	
	#Enable input system service interface in GFX
	Database.setSymbolValue("aria_gfx_library", "enableInput", True) 
	#Enable default project heap setting
	Database.setSymbolValue("aria_gfx_library", "setProjectHeap", True) 

