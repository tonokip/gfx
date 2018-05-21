def instantiateComponent(comp):
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
	
	DoubleBuffer = comp.createBooleanSymbol("DoubleBuffer", None)
	DoubleBuffer.setLabel("Use Double Buffering?")
	DoubleBuffer.setDescription("<html>Uses an additional buffer for off-screen drawing.<br>Eliminates screen tearing but doubles the required memory.</html>")
	
	PaletteMode = comp.createBooleanSymbol("PaletteMode", None)
	PaletteMode.setLabel("Use 8-bit Palette?")
	PaletteMode.setDescription("<html>Enables frame buffer compression.<br>Uses an 8-bit color lookup table to reduce the required<br>frame buffer memory size.  This also reduces the<br>maximum avilable color count to 256 and significantly<br>slows down display refresh speed.</html>")
	
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

	#temporary config symbol, need to find what replaced CONFIG_PROJECT_USES_CACHE in H3
	ProjectUsesCache = comp.createBooleanSymbol("ProjectUsesCache", None)
	
	
	# generated code files
	GFX_LCC_C = comp.createFileSymbol("GFX_LCC_C", None)
	GFX_LCC_C.setDestPath("gfx/driver")
	GFX_LCC_C.setOutputName("drv_gfx_lcc.c")
	GFX_LCC_C.setProjectPath("/gfx/driver/lcc/")
	GFX_LCC_C.setType("SOURCE")
	GFX_LCC_C.setMarkup(True)
	
	GFX_LCC_H = comp.createFileSymbol("GFX_LCC_H", None)
	GFX_LCC_H.setDestPath("gfx/driver")
	GFX_LCC_H.setOutputName("drv_gfx_lcc.h")
	GFX_LCC_H.setProjectPath("/gfx/driver/lcc/")
	GFX_LCC_H.setType("HEADER")
	GFX_LCC_H.setMarkup(True)
	
	if Variables.get("__PROCESSOR") == "PIC32CZ2038CA70144":
		GFX_LCC_C.setSourcePath("templates/drv_gfx_lcc_generic_pic32c.c.ftl")
		GFX_LCC_H.setSourcePath("templates/drv_gfx_lcc_generic_pic32c.h.ftl")
	else:
		GFX_LCC_C.setSourcePath("templates/drv_gfx_lcc_generic.c.ftl")
		GFX_LCC_H.setSourcePath("templates/drv_gfx_lcc_generic.h.ftl")
		
def onHALConnected(halConnected, event):
	halConnected.getComponent().getSymbolByID("HALComment").setVisible(event["value"] == True)
	halConnected.getComponent().getSymbolByID("DisplayWidth").setVisible(event["value"] == False)
	halConnected.getComponent().getSymbolByID("DisplayHeight").setVisible(event["value"] == False)
	halConnected.getComponent().getSymbolByID("DoubleBuffer").setVisible(event["value"] == False)
	halConnected.getComponent().getSymbolByID("PaletteMode").setVisible(event["value"] == False)
	halConnected.getComponent().getSymbolByID("LCCRefresh").setVisible(event["value"] == False)
	halConnected.getComponent().getSymbolByID("DisplaySettingsMenu").setVisible(event["value"] == False)