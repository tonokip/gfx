def instantiateComponent(comp):
	projectPath = "config/" + Variables.get("__CONFIGURATION_NAME") + "/gfx/driver/lcc"
	
	HALConnected = comp.createBooleanSymbol("HALConnected", None)
	HALConnected.setVisible(False)
	HALConnected.setDependencies(onHALConnected, ["HALConnected"])
	
	# these two symbols are read by the HAL for initialization purposes
	# they must match the function names in the actual driver code
	DriverInfoFunction = comp.createStringSymbol("DriverInfoFunction", None)
	DriverInfoFunction.setLabel("Driver Info Function Name")
	DriverInfoFunction.setReadOnly(True)
	DriverInfoFunction.setDefaultValue("driverLCCInfoGet")
	DriverInfoFunction.setVisible(False)
	
	DriverInitFunction = comp.createStringSymbol("DriverInitFunction", None)
	DriverInitFunction.setLabel("Driver Init Function Name")
	DriverInitFunction.setReadOnly(True)
	DriverInitFunction.setDefaultValue("driverLCCContextInitialize")
	DriverInitFunction.setVisible(False)
	
	# configuration options
	HALComment = comp.createCommentSymbol("HALComment", None)
	HALComment.setLabel("Some settings are being managed by the GFX HAL and have been hidden.")
	HALComment.setVisible(False)
	
	DisplayWidth = comp.createIntegerSymbol("DisplayWidth", None)
	DisplayWidth.setLabel("Width")
	DisplayWidth.setDescription("The width of the frame buffer in pixels.")
	DisplayWidth.setDefaultValue(480)

	DisplayHeight = comp.createIntegerSymbol("DisplayHeight", None)
	DisplayHeight.setLabel("Height")
	DisplayHeight.setDescription("The height of the frame buffer in pixels.")
	DisplayHeight.setDefaultValue(272)
	
	#PixelCount = comp.createIntegerSymbol("PixelCount", None)
	#PixelCount.setLabel("Total Pixels (pixels)")
	#PixelCount.setReadOnly(True)
	#PixelCount.setDescription("The total number of pixels expected to exist.")
	
	#PixelSupportLevel = comp.createStringSymbol("PixelSupportLevel")
	#PixelSupportLevel.setLabel("WQVGA or lower")
	#PixelSupportLevel.setReadOnly(True)
	#PixelSupportLevel.setDescription("The total number of pixels expected to be supportable.")
	
	LCCRefresh = comp.createBooleanSymbol("LCCRefresh", None)
	LCCRefresh.setLabel("Use Aggressive Refresh Strategy?")
	LCCRefresh.setDescription("<html>Indicates that the LCC refresh loop should attempt<br>to aggresively refresh the display.  May cause<br>display artifacts but is needed for some larger displays.</html>")
	
	DisplaySettingsMenu = comp.createMenuSymbol("DisplaySettingsMenu", None)
	DisplaySettingsMenu.setLabel("Display Settings")
	
	DisplayBacklightEnable = comp.createIntegerSymbol("DisplayBacklightEnable", DisplaySettingsMenu)
	DisplayBacklightEnable.setLabel("Back Light Enable Value")
	DisplayBacklightEnable.setDescription("The value used to enable the display back light.")
	DisplayBacklightEnable.setDefaultValue(1)

	DisplayVSYNCNegative = comp.createBooleanSymbol("DisplayVSYNCNegative", DisplaySettingsMenu)
	DisplayVSYNCNegative.setLabel("VSYNC Negative?")
	DisplayVSYNCNegative.setDescription("Indicates if this display requries negative VSYNC polarity.")
	DisplayVSYNCNegative.setDefaultValue(False)

	DisplayHSYNCNegative = comp.createBooleanSymbol("DisplayHSYNCNegative", DisplaySettingsMenu)
	DisplayHSYNCNegative.setLabel("HSYNC Negative?")
	DisplayHSYNCNegative.setDescription("Indicates if this display requries negative HSYNC polarity.")
	DisplayHSYNCNegative.setDefaultValue(False)

	DisplayDataEnable = comp.createBooleanSymbol("DisplayDataEnable", DisplaySettingsMenu)
	DisplayDataEnable.setLabel("Use Data Enable?")
	DisplayDataEnable.setDescription("Indicates if this display requries the use of the Data Enable line.")
	DisplayDataEnable.setDefaultValue(True)

	DisplayDataEnablePolarity = comp.createBooleanSymbol("DisplayDataEnablePolarity", DisplaySettingsMenu)
	DisplayDataEnablePolarity.setLabel("Data Enable Polarity Positive?")
	DisplayDataEnablePolarity.setDescription("Indicates if this display Data Enable polarity is positive.")
	DisplayDataEnablePolarity.setDefaultValue(True)

	DisplayUseReset = comp.createBooleanSymbol("DisplayUseReset", DisplaySettingsMenu)
	DisplayUseReset.setLabel("Use Reset?")
	DisplayUseReset.setDescription("Indicates if this display reset line should be used.")
	DisplayUseReset.setDefaultValue(True)

	DisplayResetPolarity = comp.createBooleanSymbol("DisplayResetPolarity", DisplaySettingsMenu)
	DisplayResetPolarity.setLabel("Reset Polarity Positive?")
	DisplayResetPolarity.setDescription("Indicates if this display reset line should be reset positive.")
	DisplayResetPolarity.setDefaultValue(True)
	
	DisplayUseChipSelect = comp.createBooleanSymbol("DisplayUseChipSelect", DisplaySettingsMenu)
	DisplayUseChipSelect.setLabel("Use Chip Select?")
	DisplayUseChipSelect.setDescription("Indicates if this display uses the chip select line.")
	DisplayUseChipSelect.setDefaultValue(True)

	DisplayChipSelectPolarity = comp.createBooleanSymbol("DisplayChipSelectPolarity", DisplaySettingsMenu)
	DisplayChipSelectPolarity.setLabel("Chip Select Polarity Positive?")
	DisplayChipSelectPolarity.setDescription("Indicates if this display chip select line should be positive.")
	DisplayChipSelectPolarity.setDefaultValue(True)
	
	FrameBufferSettingsMenu = comp.createMenuSymbol("FrameBufferSettingsMenu", None)
	FrameBufferSettingsMenu.setLabel("Frame Buffer Settings")

	DoubleBuffer = comp.createBooleanSymbol("DoubleBuffer", FrameBufferSettingsMenu)
	DoubleBuffer.setLabel("Use Double Buffering?")
	DoubleBuffer.setDescription("<html>Uses an additional buffer for off-screen drawing.<br>Eliminates screen tearing but doubles the required memory.</html>")

	PaletteMode = comp.createBooleanSymbol("PaletteMode", FrameBufferSettingsMenu)
	PaletteMode.setLabel("Use 8-bit Palette?")
	PaletteMode.setDescription("<html>Enables frame buffer compression.<br>Uses an 8-bit color lookup table to reduce the required<br>frame buffer memory size.  This also reduces the<br>maximum avilable color count to 256 and significantly<br>slows down display refresh speed.</html>")

	UseCachedFrameBuffer = comp.createBooleanSymbol("UseCachedFrameBuffer", FrameBufferSettingsMenu)
	UseCachedFrameBuffer.setLabel("Uses Cache?")
	UseCachedFrameBuffer.setDescription("Specifies if frame buffer is cached and needs to be managed by the LCC driver.")
	UseCachedFrameBuffer.setDefaultValue(True)
	UseCachedFrameBuffer.setDependencies(OnCacheEnabled, ["core.DATA_CACHE_ENABLE"])

	FrameBufferMemory = comp.createComboSymbol("FrameBufferMemory", FrameBufferSettingsMenu, ["Internal SRAM", "External SDRAM"])
	FrameBufferMemory.setLabel("Memory Interface")
	FrameBufferMemory.setDescription("Memory used for Frame Buffer")
	FrameBufferMemory.setDefaultValue("Internal SRAM")
	
	DMAMenu = comp.createMenuSymbol("DMAMenu", None)
	DMAMenu.setLabel("DMA Settings")
	
	# temporary config symbol
	# need to use the graph to draw a line to the DMA provider
	# to claim a DMA channel or some other intuitive method
	# this current method is only guessing at the max
	# and could allow the user to assign duplicate channels
	DMAChannel = comp.createIntegerSymbol("DMAChannel", DMAMenu)
	DMAChannel.setLabel("DMA Instance")
	DMAChannel.setMin(0)
	DMAChannel.setMax(5) # HARD HACK
	
	IntPriority = comp.createIntegerSymbol("IntPriority", DMAMenu)
	IntPriority.setLabel("Interrupt Priority Level")
	IntPriority.setMin(0)
	IntPriority.setMax(7)

	# generated code files
	GFX_LCC_C = comp.createFileSymbol("GFX_LCC_C", None)
	GFX_LCC_C.setDestPath("gfx/driver/controller/lcc/")
	GFX_LCC_C.setOutputName("drv_gfx_lcc.c")
	GFX_LCC_C.setProjectPath(projectPath)
	GFX_LCC_C.setType("SOURCE")
	GFX_LCC_C.setMarkup(True)
	
	GFX_LCC_H = comp.createFileSymbol("GFX_LCC_H", None)
	GFX_LCC_H.setDestPath("gfx/driver/controller/lcc/")
	GFX_LCC_H.setOutputName("drv_gfx_lcc.h")
	GFX_LCC_H.setProjectPath(projectPath)
	GFX_LCC_H.setType("HEADER")
	GFX_LCC_H.setMarkup(True)

	EBIChipSelectIndex = comp.createIntegerSymbol("EBIChipSelectIndex", None)
	EBIChipSelectIndex.setLabel("EBI Chip Select Index")
	EBIChipSelectIndex.setDescription("The chip select index")
	EBIChipSelectIndex.setMin(0)
	EBIChipSelectIndex.setMax(4)
	EBIChipSelectIndex.setDefaultValue(0)
	EBIChipSelectIndex.setVisible(False)


	GFX_LCC_C.setSourcePath("templates/drv_gfx_lcc_generic.c.ftl")
	GFX_LCC_H.setSourcePath("templates/drv_gfx_lcc_generic.h.ftl")

	# Use and configure XDMAC channel 0 for now
	DMA_CHANNEL = 0
	Database.getComponentByID("core").getSymbolByID("XDMAC_CH" + str(DMA_CHANNEL) + "_ENABLE").setValue(True, 1)
	Database.getComponentByID("core").getSymbolByID("XDMAC_CC" + str(DMA_CHANNEL) + "_DAM").setSelectedKey("FIXED_AM", 1)
	Database.getComponentByID("core").getSymbolByID("XDMAC_CC" + str(DMA_CHANNEL) + "_DWIDTH").setSelectedKey("HALFWORD", 1)
	Database.getComponentByID("core").getSymbolByID("XDMAC_CC" + str(DMA_CHANNEL) + "_SIF").setSelectedKey("AHB_IF0", 1)
	Database.getComponentByID("core").getSymbolByID("XDMAC_CC" + str(DMA_CHANNEL) + "_MBSIZE").setSelectedKey("SIXTEEN", 1)

def onHALConnected(halConnected, event):
	halConnected.getComponent().getSymbolByID("HALComment").setVisible(event["value"] == True)
	halConnected.getComponent().getSymbolByID("DisplayWidth").setVisible(event["value"] == False)
	halConnected.getComponent().getSymbolByID("DisplayHeight").setVisible(event["value"] == False)
	halConnected.getComponent().getSymbolByID("DoubleBuffer").setVisible(event["value"] == False)
	halConnected.getComponent().getSymbolByID("PaletteMode").setVisible(event["value"] == False)
	halConnected.getComponent().getSymbolByID("LCCRefresh").setVisible(event["value"] == False)
	halConnected.getComponent().getSymbolByID("DisplaySettingsMenu").setVisible(event["value"] == False)
	
def configureSMCComponent(lccComponent, smcComponent, smcChipSelNum):
	print("LCC: Connecting SMC_CS" + str(smcChipSelNum))
	smcComponent.setSymbolValue("SMC_CHIP_SELECT" + str(smcChipSelNum), True, 1)
	smcComponent.setSymbolValue("SMC_MEM_SCRAMBLING_CS" + str(smcChipSelNum), False, 1)
	smcComponent.setSymbolValue("SMC_NWE_SETUP_CS" + str(smcChipSelNum), 1, 1)
	smcComponent.setSymbolValue("SMC_NCS_WR_SETUP_CS" + str(smcChipSelNum), 0, 1)
	smcComponent.setSymbolValue("SMC_NWE_PULSE_CS" + str(smcChipSelNum), 3, 1)
	smcComponent.setSymbolValue("SMC_NCS_WR_PULSE_CS" + str(smcChipSelNum), 3, 1)
	smcComponent.setSymbolValue("SMC_DATA_BUS_CS" + str(smcChipSelNum), 1, 1)
	smcComponent.setSymbolValue("SMC_WRITE_ENABLE_MODE_CS" + str(smcChipSelNum), False, 1)
	lccComponent.setSymbolValue("EBIChipSelectIndex", smcChipSelNum, 1)
	
def resetSMCComponent(lccComponent, smcComponent, smcChipSelNum):
	print("LCC: Disconnecting SMC_CS" + str(smcChipSelNum))
	smcComponent.clearSymbolValue("SMC_CHIP_SELECT" + str(smcChipSelNum))
	smcComponent.clearSymbolValue("SMC_MEM_SCRAMBLING_CS" + str(smcChipSelNum))
	smcComponent.clearSymbolValue("SMC_NWE_SETUP_CS" + str(smcChipSelNum))
	smcComponent.clearSymbolValue("SMC_NCS_WR_SETUP_CS" + str(smcChipSelNum))
	smcComponent.clearSymbolValue("SMC_NWE_PULSE_CS" + str(smcChipSelNum))
	smcComponent.clearSymbolValue("SMC_NCS_WR_PULSE_CS" + str(smcChipSelNum))
	smcComponent.clearSymbolValue("SMC_DATA_BUS_CS" + str(smcChipSelNum))
	smcComponent.clearSymbolValue("SMC_WRITE_ENABLE_MODE_CS" + str(smcChipSelNum))
	lccComponent.clearSymbolValue("EBIChipSelectIndex")

def onDependencyConnected(info):
	if (info["capabilityID"] == "smc_cs0"):
		configureSMCComponent(info["localComponent"], info["remoteComponent"], 0)
	elif (info["capabilityID"] == "smc_cs1"):
		configureSMCComponent(info["localComponent"], info["remoteComponent"], 1)
	elif (info["capabilityID"] == "smc_cs2"):
		configureSMCComponent(info["localComponent"], info["remoteComponent"], 2)
	elif (info["capabilityID"] == "smc_cs3"):
		configureSMCComponent(info["localComponent"], info["remoteComponent"], 3)
	
def onDependencyDisconnected(info):
	if (info["capabilityID"] == "smc_cs0"):
		resetSMCComponent(info["localComponent"], info["remoteComponent"], 0)
	elif (info["capabilityID"] == "smc_cs1"):
		resetSMCComponent(info["localComponent"], info["remoteComponent"], 1)
	elif (info["capabilityID"] == "smc_cs2"):
		resetSMCComponent(info["localComponent"], info["remoteComponent"], 2)
	elif (info["capabilityID"] == "smc_cs3"):
		resetSMCComponent(info["localComponent"], info["remoteComponent"], 3)

def OnCacheEnabled(cacheEnabled, event):
	print("LCC: cache enabled")
	cacheEnabled.getComponent().setSymbolValue("UseCachedFrameBuffer", event["value"] == True, 1)
	print("LCC: UseCachedFrameBuffer enabled")
