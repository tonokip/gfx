def instantiateComponent(component):
	Width = component.createIntegerSymbol("Width", None)
	Width.setLabel("Width")
	Width.setDescription("The width of the touch panel in pixels.")
	Width.setDefaultValue(480)
	
	Height = component.createIntegerSymbol("Height", None)
	Height.setLabel("Height")
	Height.setDescription("The height of the touch panel in pixels.")
	Height.setDefaultValue(272)
	
	"""DisplayOrientation = halComponent.createComboSymbol("DisplayOrientation", DisplayMenu, ["0","90","180","270"])
	DisplayOrientation.setLabel("Display Orientation")
	DisplayOrientation.setDefaultValue("0")
	DisplayOrientation.setDescription("Configures the touch panel orientation at the hardware level.")"""
	
	projectPath = "config/" + Variables.get("__CONFIGURATION_NAME") + "/driver/input"
	
	DRV_MAXTOUCH_H = component.createFileSymbol("DRV_MAXTOUCH_H", None)
	DRV_MAXTOUCH_H.setSourcePath("drv_maxtouch.h")
	DRV_MAXTOUCH_H.setDestPath("driver/input/")
	DRV_MAXTOUCH_H.setProjectPath(projectPath)
	DRV_MAXTOUCH_H.setType("HEADER")
	
	DRV_MAXTOUCH_C = component.createFileSymbol("DRV_MAXTOUCH_C", None)
	DRV_MAXTOUCH_C.setSourcePath("drv_maxtouch.c")
	DRV_MAXTOUCH_C.setDestPath("driver/input/")
	DRV_MAXTOUCH_C.setProjectPath(projectPath)
	DRV_MAXTOUCH_C.setType("SOURCE")
	
	I2CIndex = component.createIntegerSymbol("I2CIndex", None)
	I2CIndex.setLabel("I2C Driver Index")
	I2CIndex.setDefaultValue(0)
	I2CIndex.setMin(0)
	
	SysDefines = component.createFileSymbol("SysDefines", None)
	SysDefines.setType("STRING")
	SysDefines.setOutputName("core.LIST_SYSTEM_CONFIG_H_DRIVER_CONFIGURATION")
	SysDefines.setSourcePath("drv_maxtouch_defines.ftl")
	SysDefines.setMarkup(True)
	
	SysInitData = component.createFileSymbol("SysInitData", None)
	SysInitData.setType("STRING")
	SysInitData.setOutputName("core.LIST_SYSTEM_INIT_C_DRIVER_INITIALIZATION_DATA")
	SysInitData.setSourcePath("drv_maxtouch_init.ftl")
	SysInitData.setMarkup(True)
	
	SysObjString = component.createListEntrySymbol("SysObjString", None)
	SysObjString.addValue('    SYS_MODULE_OBJ  drvMAXTOUCH;')
	SysObjString.setTarget("core.LIST_SYSTEM_DEFINITIONS_H_OBJECTS")
	
	SysTasksString = component.createListEntrySymbol("SYSTasksString", None)
	SysTasksString.addValue("DRV_MAXTOUCH_Tasks(sysObj.drvMAXTOUCH);")
	SysTasksString.setTarget("core.LIST_SYSTEM_TASKS_C_CALL_DRIVER_TASKS")
	
	SysInitString = component.createListEntrySymbol("SysInitString", None)
	SysInitString.addValue("    sysObj.drvMAXTOUCH = DRV_MAXTOUCH_Initialize(0, (SYS_MODULE_INIT *)&drvMAXTOUCHInitData);")
	SysInitString.setTarget("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_DRIVERS")

	SysInitIncludeString = component.createListEntrySymbol("SysInitIncludeString", None)
	SysInitIncludeString.addValue('#include "driver/input/drv_maxtouch.h"')
	SysInitIncludeString.setTarget("core.LIST_SYSTEM_CONFIG_H_GLOBAL_INCLUDES")
	
def onDependentComponentAdded(component, dependencyID, dependencyComponent):
	print(component)
	
	if dependencyID == "touch_panel":
		component.setSymbolValue("Width", dependencyComponent.getSymbolValue("TouchWidth"), 1)
		component.setSymbolValue("Height", dependencyComponent.getSymbolValue("TouchHeight"), 1)
		
	if dependencyID == "i2c":
		I2CIndex = component.getSymbolByID("I2CIndex")
		I2CIndex.setValue(int(dependencyComponent.getID()[-1]), 1)
		I2CIndex.setReadOnly(True)
	
def onDependentComponentRemoved(component, dependencyID, dependencyComponent):
	if dependencyID == "touch_panel":
		component.clearSymbolValue("Width")
		component.clearSymbolValue("Height")
	
	if dependencyID == "i2c":
		I2CIndex = component.getSymbolByID("I2CIndex")
		I2CIndex.clearValue()
		I2CIndex.setReadOnly(False)
