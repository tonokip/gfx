def instantiateComponent(halComponent):
	projectPath = "config/" + Variables.get("__CONFIGURATION_NAME") + "/gfx/hal"
	
	execfile(Module.getPath() + "/config/hal_pipeline.py")
	execfile(Module.getPath() + "/config/hal_display.py")
	execfile(Module.getPath() + "/config/hal_driver.py")
	execfile(Module.getPath() + "/config/hal_gpu.py")
	execfile(Module.getPath() + "/config/hal_hints.py")
	execfile(Module.getPath() + "/config/hal_files.py")
	
	SysInitIncludeString = halComponent.createListEntrySymbol("SysInitIncludeString", None)
	SysInitIncludeString.addValue('#include "gfx/hal/gfx.h"')
	SysInitIncludeString.setTarget("core.LIST_SYSTEM_CONFIG_H_GLOBAL_INCLUDES")
	
	SysInitString = halComponent.createListEntrySymbol("SysInitString", None)
	SysInitString.addValue("    GFX_Initialize();")
	SysInitString.setTarget("core.LIST_SYSTEM_INIT_C_INITIALIZE_MIDDLEWARE")
	
	SysTasksString = halComponent.createListEntrySymbol("SYSTasksString", None)
	SysTasksString.addValue("    GFX_Update();")
	SysTasksString.setTarget("core.LIST_SYSTEM_TASKS_C_CALL_LIB_TASKS")
	
def onDependentComponentAdded(halComponent, dependencyID, dependencyComponent):
	if dependencyID == "gfx_display_driver":
		halComponent.setSymbolValue("DriverInfoFunction", dependencyComponent.getSymbolValue("DriverInfoFunction"), 1)
		halComponent.setSymbolValue("DriverInitFunction", dependencyComponent.getSymbolValue("DriverInitFunction"), 1)
		
		dependencyComponent.setSymbolValue("HALConnected", True, 1)
		
	if dependencyID == "gfx_display":
		updateDisplayValues(halComponent, dependencyComponent)
	
def onDependentComponentRemoved(halComponent, dependencyID, dependencyComponent):
	if dependencyID == "gfx_display_driver":
		halComponent.clearSymbolValue("DriverInfoFunction")
		halComponent.clearSymbolValue("DriverInitFunction")
	
		dependencyComponent.clearSymbolValue("HALConnected")
	
	if dependencyID == "gfx_display":
		clearDisplayValues(halComponent)

def onDrawPipelineEnableChanged(menu, event):
	menu.setVisible(event["value"])

def updateDisplayValues(halComponent, displayComponent):
	halComponent.setSymbolValue("DisplayName", displayComponent.getSymbolValue("Name"), 1)
	halComponent.setSymbolValue("DisplayWidth", displayComponent.getSymbolValue("DisplayWidth"), 1)
	halComponent.setSymbolValue("DisplayHeight", displayComponent.getSymbolValue("DisplayHeight"), 1)
	halComponent.setSymbolValue("DisplayDataWidth", displayComponent.getSymbolValue("DataWidth"), 1)
	halComponent.setSymbolValue("DisplayHorzPulseWidth", displayComponent.getSymbolValue("HorzPulseWidth"), 1)
	halComponent.setSymbolValue("DisplayHorzBackPorch", displayComponent.getSymbolValue("HorzBackPorch"), 1)
	halComponent.setSymbolValue("DisplayHorzFrontPorch", displayComponent.getSymbolValue("HorzFrontPorch"), 1)
	halComponent.setSymbolValue("DisplayVertPulseWidth", displayComponent.getSymbolValue("VertPulseWidth"), 1)
	halComponent.setSymbolValue("DisplayVertBackPorch", displayComponent.getSymbolValue("VertBackPorch"), 1)
	halComponent.setSymbolValue("DisplayVertFrontPorch", displayComponent.getSymbolValue("VertFrontPorch"), 1)
	halComponent.setSymbolValue("DisplayInvLeftShift", displayComponent.getSymbolValue("InvLeftShift"), 1)
	halComponent.setSymbolValue("DisplayBacklightDisable", displayComponent.getSymbolValue("BacklightDisable"), 1)
	halComponent.setSymbolValue("DisplayBacklightEnable", displayComponent.getSymbolValue("BacklightEnable"), 1)
	halComponent.setSymbolValue("DisplayVSYNCNegative", displayComponent.getSymbolValue("VSYNCNegative"), 1)
	halComponent.setSymbolValue("DisplayHSYNCNegative", displayComponent.getSymbolValue("HSYNCNegative"), 1)
	halComponent.setSymbolValue("DisplayDataEnable", displayComponent.getSymbolValue("DataEnable"), 1)
	halComponent.setSymbolValue("DisplayDataEnablePolarity", displayComponent.getSymbolValue("DataEnablePolarity"), 1)
	halComponent.setSymbolValue("DisplayUseReset", displayComponent.getSymbolValue("UseReset"), 1)
	halComponent.setSymbolValue("DisplayResetPolarity", displayComponent.getSymbolValue("ResetPolarity"), 1)
	halComponent.setSymbolValue("DisplayUseChipSelect", displayComponent.getSymbolValue("UseChipSelect"), 1)
	halComponent.setSymbolValue("DisplayChipSelectPolarity", displayComponent.getSymbolValue("ChipSelectPolarity"), 1)

def clearDisplayValues(halComponent):
	halComponent.clearSymbolValue("DisplayName")
	halComponent.clearSymbolValue("DisplayWidth")
	halComponent.clearSymbolValue("DisplayHeight")
	halComponent.clearSymbolValue("DisplayDataWidth")
	halComponent.clearSymbolValue("DisplayHorzPulseWidth")
	halComponent.clearSymbolValue("DisplayHorzBackPorch")
	halComponent.clearSymbolValue("DisplayHorzFrontPorch")
	halComponent.clearSymbolValue("DisplayVertPulseWidth")
	halComponent.clearSymbolValue("DisplayVertBackPorch")
	halComponent.clearSymbolValue("DisplayVertFrontPorch")
	halComponent.clearSymbolValue("DisplayInvLeftShift")
	halComponent.clearSymbolValue("DisplayBacklightDisable")
	halComponent.clearSymbolValue("DisplayBacklightEnable")
	halComponent.clearSymbolValue("DisplayVSYNCNegative")
	halComponent.clearSymbolValue("DisplayHSYNCNegative")
	halComponent.clearSymbolValue("DisplayDataEnable")
	halComponent.clearSymbolValue("DisplayDataEnablePolarity")
	halComponent.clearSymbolValue("DisplayUseReset")
	halComponent.clearSymbolValue("DisplayResetPolarity")
	halComponent.clearSymbolValue("DisplayUseChipSelect")
	halComponent.clearSymbolValue("DisplayChipSelectPolarity")
	
def onDisableHint(symbol, event):
	halComponent = event["source"]
	
	ColorModeHint = halComponent.getSymbolByID("ColorModeHint")
	ColorModeHint.setReadOnly(halComponent.getSymbolValue("DisableColorModeHint"))
	
	GlobalPaletteModeHint = halComponent.getSymbolByID("GlobalPaletteModeHint")
	GlobalPaletteModeHint.setReadOnly(halComponent.getSymbolValue("DisableGlobalPaletteModeHint"))
	
	DoubleBufferHint = halComponent.getSymbolByID("DoubleBufferHint")
	DoubleBufferHint.setReadOnly(halComponent.getSymbolValue("DisableDoubleBufferHint"))
	
	LCCRefreshHint = halComponent.getSymbolByID("LCCRefreshHint")
	LCCRefreshHint.setReadOnly(halComponent.getSymbolValue("DisableLCCRefreshHint"))
	
	Orientation = halComponent.getSymbolByID("DisplayOrientation")
	Orientation.setReadOnly(halComponent.getSymbolValue("DisableDisplayOrientation"))