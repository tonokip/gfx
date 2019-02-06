def instantiateComponent(comp):
	execfile(Module.getPath() + "/config/ssd1963_config.py")
	execfile(Module.getPath() + "/config/ssd1963_files.py")

def onHALConnected(halConnected, event):
	halConnected.getComponent().getSymbolByID("HALComment").setVisible(event["value"] == True)
	halConnected.getComponent().getSymbolByID("DisplaySettingsMenu").setVisible(event["value"] == False)
	halConnected.getComponent().getSymbolByID("PaletteMode").setVisible(event["value"] == False)

def configureSMCComponent(comp, smcComponent):
	print("Configuring SMC")
	smcChipSelNum = comp.getSymbolValue("EBIChipSelectIndex")
	smcComponent.setSymbolValue("SMC_CHIP_SELECT" + str(smcChipSelNum), True, 1)
	smcComponent.setSymbolValue("SMC_MEM_SCRAMBLING_CS" + str(smcChipSelNum), False, 1)
	# SMC Write Timings
	smcComponent.setSymbolValue("SMC_NWE_SETUP_CS" + str(smcChipSelNum), 4, 1)
	smcComponent.setSymbolValue("SMC_NCS_WR_SETUP_CS" + str(smcChipSelNum), 0, 1)
	smcComponent.setSymbolValue("SMC_NWE_PULSE_CS" + str(smcChipSelNum), 4, 1)
	smcComponent.setSymbolValue("SMC_NCS_WR_PULSE_CS" + str(smcChipSelNum), 10, 1)
	smcComponent.setSymbolValue("SMC_DATA_BUS_CS" + str(smcChipSelNum), 1, 1)
	smcComponent.setSymbolValue("SMC_NWE_CYCLE_CS" + str(smcChipSelNum), 3, 1)
	# SMC Read Timings
	smcComponent.setSymbolValue("SMC_NRD_SETUP_CS" + str(smcChipSelNum), 2, 1)
	smcComponent.setSymbolValue("SMC_NCS_RD_SETUP_CS" + str(smcChipSelNum), 0, 1)
	smcComponent.setSymbolValue("SMC_NRD_PULSE_CS" + str(smcChipSelNum), 63, 1)
	smcComponent.setSymbolValue("SMC_NCS_RD_PULSE_CS" + str(smcChipSelNum), 63, 1)
	smcComponent.setSymbolValue("SMC_NRD_CYCLE_CS" + str(smcChipSelNum), 110, 1)
	# SMC Mode Configuration
	smcComponent.setSymbolValue("SMC_DATA_BUS_CS" + str(smcChipSelNum), 1, 1)
	smcComponent.setSymbolValue("SMC_BAT_CS" + str(smcChipSelNum), 0, 1)
	smcComponent.setSymbolValue("SMC_READ_ENABLE_MODE_CS" + str(smcChipSelNum), True, 1)
	smcComponent.setSymbolValue("SMC_WRITE_ENABLE_MODE_CS" + str(smcChipSelNum), False, 1)
	
def onAttachmentConnected(source, target):
	print(source["component"].getID() + ": " + source["id"] + " dependent component added")
	if source["id"] == "SMC_CS":
		#Enable the SMC options
		source["component"].getSymbolByID("GFX_SSD1963_INTF_SMC").setEnabled(True)
		source["component"].getSymbolByID("InterfaceSettingsSMCMenu").setVisible(True)
		configureSMCComponent(source["component"], target["component"])

def onAttachmentDisconnected(source, target):
	print(source["component"].getID() + ": " + source["id"] + " dependent component removed")
	#Disable the SMC options
	source["component"].getSymbolByID("InterfaceSettingsSMCMenu").setVisible(False)
	source["component"].getSymbolByID("GFX_SSD1963_INTF_SMC").setEnabled(False)
	
def onDataCommandSelectSet(dataCommandSelected, event):
	if (dataCommandSelected.getComponent().getSymbolByID("DataCommandSelectControl").getValue() == "GPIO"):
		dataCommandSelected.getComponent().getSymbolByID("DCXAddressBit").setVisible(False)
	else:
		dataCommandSelected.getComponent().getSymbolByID("DCXAddressBit").setVisible(True)

def onPixelClockSet(pixelClockSet, event):
	MasterClock = pixelClockSet.getComponent().getSymbolValue("MasterClock")
	prescalerValue = float(MasterClock/float(event["value"]))
	strValue = str(float("{0:.4f}".format(prescalerValue)))
	pixelClockSet.getComponent().getSymbolByID("PixelClockPreScaler").setValue(strValue, 1)
	if (pixelClockSet.getComponent().getSymbolValue("HALConnected") == True):
		Database.setSymbolValue("gfx_hal", "PixelClock", event["value"], 1)
		
def onBacklightPWMFrequencySet(pixelClockSet, event):
	MasterClock = pixelClockSet.getComponent().getSymbolValue("MasterClock")
	prescalerValue = float(MasterClock/float(event["value"]))
	strValue = str(float("{0:.4f}".format(prescalerValue)))
	pixelClockSet.getComponent().getSymbolByID("PixelClockPreScaler").setValue(strValue, 1)
