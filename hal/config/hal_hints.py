DriverHintMenu = halComponent.createMenuSymbol("DriverHintMenu", None)
DriverHintMenu.setLabel("Driver Configuration Hints")
DriverHintMenu.setDescription("Contains compile-time configuration hints for various graphics subsystems.")

ColorModes = [
		"GFX_COLOR_MODE_GS_8",
		"GFX_COLOR_MODE_RGB_332",
		"GFX_COLOR_MODE_RGB_565",
		"GFX_COLOR_MODE_RGBA_5551",
		"GFX_COLOR_MODE_RGB_888",
		"GFX_COLOR_MODE_RGBA_8888",
		"GFX_COLOR_MODE_ARGB_8888"
	]
	
ColorModeHint = halComponent.createComboSymbol("ColorModeHint", DriverHintMenu, ColorModes)
ColorModeHint.setLabel("Display Color Mode")
ColorModeHint.setDescription("Indicates that the graphics display driver should use the indicated color mode if available.")
ColorModeHint.setDefaultValue("GFX_COLOR_MODE_RGB_565")

DisableColorModeHint = halComponent.createBooleanSymbol("DisableColorModeHint", DriverHintMenu)
DisableColorModeHint.setDefaultValue(False)
DisableColorModeHint.setVisible(False)
DisableColorModeHint.setDependencies(onDisableHint, ["DisableColorModeHint"])

GlobalPaletteModeHint = halComponent.createBooleanSymbol("GlobalPaletteModeHint", DriverHintMenu)
GlobalPaletteModeHint.setLabel("Global Palette Mode")
GlobalPaletteModeHint.setDescription("Indicates that the graphics display driver should use global palette mode if available.")

DisableGlobalPaletteModeHint = halComponent.createBooleanSymbol("DisableGlobalPaletteModeHint", DriverHintMenu)
DisableGlobalPaletteModeHint.setDefaultValue(False)
DisableGlobalPaletteModeHint.setVisible(False)
DisableGlobalPaletteModeHint.setDependencies(onDisableHint, ["DisableGlobalPaletteModeHint"])

DoubleBufferHint = halComponent.createBooleanSymbol("DoubleBufferHint", DriverHintMenu)
DoubleBufferHint.setLabel("Double Buffer Mode")
DoubleBufferHint.setDescription("Indicates that the graphics display driver should use double buffering if available.")

DisableDoubleBufferHint = halComponent.createBooleanSymbol("DisableDoubleBufferHint", DriverHintMenu)
DisableDoubleBufferHint.setDefaultValue(False)
DisableDoubleBufferHint.setVisible(False)
DisableDoubleBufferHint.setDependencies(onDisableHint, ["DisableDoubleBufferHint"])

LCCRefreshHint = halComponent.createBooleanSymbol("LCCRefreshHint", DriverHintMenu)
LCCRefreshHint.setLabel("Aggressive Refresh")
LCCRefreshHint.setDescription("Indicates that a graphics display driver should use an aggressive refresh strategy for the given display device.  This involves merging the front porch pulses into the back porch.")

DisableLCCRefreshHint = halComponent.createBooleanSymbol("DisableLCCRefreshHint", DriverHintMenu)
DisableLCCRefreshHint.setDefaultValue(False)
DisableLCCRefreshHint.setVisible(False)
DisableLCCRefreshHint.setDependencies(onDisableHint, ["DisableLCCRefreshHint"])

HardwareLayerCountHint = halComponent.createIntegerSymbol("HardwareLayerCountHint", DriverHintMenu)
HardwareLayerCountHint.setLabel("Hardware Layer Count")
HardwareLayerCountHint.setDefaultValue(1)
HardwareLayerCountHint.setDescription("Indicates the number of hardware layers provided by the display driver.")
#HardwareLayerCountHint.setReadOnly(True)

DisableHardwareLayerCountHint = halComponent.createBooleanSymbol("DisableHardwareLayerCountHint", DriverHintMenu)
DisableHardwareLayerCountHint.setDefaultValue(False)
DisableHardwareLayerCountHint.setVisible(False)
DisableHardwareLayerCountHint.setDependencies(onDisableHint, ["DisableHardwareLayerCountHint"])