DriverHintMenu = halComponent.createMenuSymbol("DriverHintMenu", None)
DriverHintMenu.setLabel("Driver Configuration Hints")
DriverHintMenu.setDescription("Contains compile-time configuration hints for various graphics subsystems.")

ColorModes = [
		"GFX_COLOR_MODE_GS_8",
		"GFX_COLOR_MODE_RGB_332",
		"GFX_COLOR_MODE_RGB_565",
		"GFX_COLOR_MODE_RGB_5551",
		"GFX_COLOR_MODE_RGB_888",
		"GFX_COLOR_MODE_RGBA_8888",
		"GFX_COLOR_MODE_ARGB_8888"
	]
	
ColorModeHint = halComponent.createComboSymbol("ColorModeHint", DriverHintMenu, ColorModes)
ColorModeHint.setLabel("Display Color Mode")
ColorModeHint.setDescription("Indicates that the graphics display driver should use the indicated color mode if available.")
ColorModeHint.setDefaultValue("GFX_COLOR_MODE_RGB_565")

GlobalPaletteModeHint = halComponent.createBooleanSymbol("GlobalPaletteModeHint", DriverHintMenu)
GlobalPaletteModeHint.setLabel("Global Palette Mode")
GlobalPaletteModeHint.setDescription("Indicates that the graphics display driver should use global palette mode if available.")

DoubleBufferHint = halComponent.createBooleanSymbol("DoubleBufferHint", DriverHintMenu)
DoubleBufferHint.setLabel("Double Buffer Mode")
DoubleBufferHint.setDescription("Indicates that the graphics display driver should use double buffering if available.")

#DisplayOrientationHint = halComponent.createComboSymbol("DisplayOrientationHint", DriverHintMenu)


LCCRefreshHint = halComponent.createBooleanSymbol("LCCRefreshHint", DriverHintMenu)
LCCRefreshHint.setLabel("LCC Aggressive Refresh")
LCCRefreshHint.setDescription("Indicates that an LCC graphics display driver should use an aggressive refresh strategy for the given display device.")
