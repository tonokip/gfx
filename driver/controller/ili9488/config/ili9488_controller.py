def instantiateComponent(comp):
	execfile(Module.getPath() + "/config/ili9488_config.py")
	execfile(Module.getPath() + "/config/ili9488_files.py")

def onHALConnected(halConnected, event):
	halConnected.getComponent().getSymbolByID("HALComment").setVisible(event["value"] == True)
	halConnected.getComponent().getSymbolByID("DisplayWidth").setVisible(event["value"] == False)
	halConnected.getComponent().getSymbolByID("DisplayHeight").setVisible(event["value"] == False)
	halConnected.getComponent().getSymbolByID("PaletteMode").setVisible(event["value"] == False)

def configureSMCComponent(comp, smcComponent):
	print("Configuring SMC")
	smcChipSelNum = comp.getSymbolValue("EBIChipSelectIndex")
	smcComponent.setSymbolValue("SMC_CHIP_SELECT" + str(smcChipSelNum), True, 1)
	smcComponent.setSymbolValue("SMC_MEM_SCRAMBLING_CS" + str(smcChipSelNum), False, 1)
	# SMC Write Timings
	smcComponent.setSymbolValue("SMC_NWE_SETUP_CS" + str(smcChipSelNum), 2, 1)
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
	smcComponent.setSymbolValue("SMC_WRITE_ENABLE_MODE_CS" + str(smcChipSelNum), True, 1)
	
def configureSPIComponent(comp, spiComponent):
	print("Configuring SPI")
	# TODO: Add SPI configuration here

def onDependentComponentAdded(comp, dependencyID, dependencyComponent):
	print(comp.getID() + ": " + dependencyID + " dependent component added ")
	if dependencyID == "SMC":
		#Disable the SPI symbols
		comp.setDependencyEnabled("DRV_SPI", False)
		comp.getSymbolByID("GFX_ILI9488_SPI").setEnabled(False)
		#Enable the SMC symbols
		comp.getSymbolByID("Interface").setValue("Parallel", 1)
		comp.getSymbolByID("ParallelInterfaceWidth").setVisible(True)
		comp.getSymbolByID("DCXAddressBit").setVisible(True)
		comp.getSymbolByID("UseSyncBarriers").setVisible(True)
		comp.getSymbolByID("EBIChipSelectIndex").setVisible(True)
		comp.getSymbolByID("GFX_ILI9488_DBIB_C").setEnabled(True)
		configureSMCComponent(comp, dependencyComponent)
	if dependencyID == "DRV_SPI":
		spiIndex = dependencyComponent.getSymbolByID("INDEX").getValue()
		print("Using SPI port " + str(spiIndex))
		#Disable the SMC symbols
		#comp.setDependencyEnabled("SMC", False)
		comp.getSymbolByID("GFX_ILI9488_DBIB_C").setEnabled(False)
		#Enable the SPI symbols
		comp.getSymbolByID("Interface").setValue("SPI 4-Line", 1)
		comp.getSymbolByID("SPIPortIndex").setValue(spiIndex, 1)
		comp.getSymbolByID("GFX_ILI9488_SPI").setEnabled(True)
		configureSPIComponent(comp, dependencyComponent)

def onDependentComponentRemoved(comp, dependencyID, dependencyComponent):
	print(comp.getID() + ": " + dependencyID + " dependent component removed ")
	comp.setDependencyEnabled("DRV_SPI", True)
	#comp.setDependencyEnabled("SMC", True)
	#Disable the SMC and SPI symbols
	comp.getSymbolByID("ParallelInterfaceWidth").setVisible(False)
	comp.getSymbolByID("DCXAddressBit").setVisible(False)
	comp.getSymbolByID("UseSyncBarriers").setVisible(False)
	comp.getSymbolByID("EBIChipSelectIndex").setVisible(False)
	comp.getSymbolByID("GFX_ILI9488_SPI").setEnabled(False)
	comp.getSymbolByID("GFX_ILI9488_DBIB_C").setEnabled(False)

def onInterfaceSetSPI(symbol, event):
	if event["value"] == "SPI 4-Line":
		symbol.setVisible(True)
	else:
		symbol.setVisible(False)

def onInterfaceSetParallel(symbol, event):
	if event["value"] == "16-bit" or event["value"] == "8-bit":
		symbol.setVisible(True)
	else:
		symbol.setVisible(False)
