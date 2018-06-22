def instantiateComponent(bspComponent):
	BSP_NAME = "sam_e70_xult_lcc_wqvga"
	
	pinConfigs = [{"pin": 11, "name": "EBI_D0", "type": "EBI_DO", "direction": "", "latch": ""},
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
				{"pin": 94, "name": "BSP_LCD_DE", "type": "GPIO", "direction": "Out", "latch": "High"},
				]
				
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

