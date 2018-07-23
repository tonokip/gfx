def instantiateComponent(component):
	projectPath = "config/" + Variables.get("__CONFIGURATION_NAME") + "/gfx/libaria"
	
	execfile(Module.getPath() + "/config/aria_config.py")
	execfile(Module.getPath() + "/utils/config/aria_utils.py")
	execfile(Module.getPath() + "/third_party/config/aria_thirdparty.py")
	execfile(Module.getPath() + "/config/aria_demomode.py")
	execfile(Module.getPath() + "/config/aria_rtos.py")
	execfile(Module.getPath() + "/config/aria_files.py")

	SysInitIncludeString = component.createListEntrySymbol("SysInitIncludeString", None)
	SysInitIncludeString.addValue('#include "gfx/libaria/libaria_harmony.h"')
	SysInitIncludeString.setTarget("core.LIST_SYSTEM_CONFIG_H_GLOBAL_INCLUDES")
	
	SysInitString = component.createListEntrySymbol("SysInitString", None)
	SysInitString.addValue("    LibAria_Initialize(); // initialize UI library")
	SysInitString.setTarget("core.LIST_SYSTEM_INIT_C_INITIALIZE_MIDDLEWARE")
	
	SysTasksString = component.createListEntrySymbol("SYSTasksString", None)
	SysTasksString.addValue("    LibAria_Tasks(); // update the UI library")
	SysTasksString.setTarget("core.LIST_SYSTEM_TASKS_C_CALL_LIB_TASKS")
	
	setProjectHeap = component.createBooleanSymbol("setProjectHeap", None)
	setProjectHeap.setLabel("Set Project Heap?")
	setProjectHeap.setDefaultValue(False)
	setProjectHeap.setDescription("Set the heap for the MPLAB project. This overrides the default heap setting.")

	ariaProjectHeap = component.createIntegerSymbol("ariaProjectHeap", setProjectHeap)
	ariaProjectHeap.setLabel("Heap")
	ariaProjectHeap.setVisible(False)
	ariaProjectHeap.setDefaultValue(32768)
	ariaProjectHeap.setDescription("Heap for the MPLAB project. This overrides the default heap setting.")
	ariaProjectHeap.setDependencies(onSetProjectHeapEnabled, ["setProjectHeap"])

	xc32AriaProjectHeap = component.createSettingSymbol("XC32_ARIA_PROJECT_HEAP", setProjectHeap)
	xc32AriaProjectHeap.setCategory("C32-LD")
	xc32AriaProjectHeap.setKey("heap-size")
	xc32AriaProjectHeap.setEnabled(False)
	xc32AriaProjectHeap.setDependencies(onSetProjectHeap, ["ariaProjectHeap"])

def onSetProjectHeapEnabled(enableSetProjectHeap, event):
	enableSetProjectHeap.getComponent().getSymbolByID("ariaProjectHeap").setVisible(event["value"])
	
	projectHeap = enableSetProjectHeap.getComponent().getSymbolByID("ariaProjectHeap").getValue()
	enableSetProjectHeap.getComponent().getSymbolByID("XC32_ARIA_PROJECT_HEAP").setEnabled(event["value"])
	enableSetProjectHeap.getComponent().getSymbolByID("XC32_ARIA_PROJECT_HEAP").setValue(str(projectHeap))

def onSetProjectHeap(setProjectHeap, event):
	projectHeap = setProjectHeap.getComponent().getSymbolByID("ariaProjectHeap").getValue()
	setProjectHeap.getComponent().getSymbolByID("XC32_ARIA_PROJECT_HEAP").setValue(str(projectHeap))

def onDependentComponentAdded(aria, dependencyID, hal):
	hal.setSymbolValue("GlobalPaletteModeHint", aria.getSymbolValue("useGlobalPalette"), 1)
	hal.setSymbolValue("DisableGlobalPaletteModeHint", True, 1)

def onDependentComponentRemoved(aria, dependencyID, hal):
	hal.clearSymbolValue("GlobalPaletteModeHint")
	hal.clearSymbolValue("DisableGlobalPaletteModeHint")
	
def onDemoModeEnable(enableDemoMode, event):
	enableDemoMode.getComponent().getSymbolByID("demoModeRecordInput").setVisible(event["value"])
	enableDemoMode.getComponent().getSymbolByID("demoModeRecordTickPeriod").setVisible(event["value"])
	enableDemoMode.getComponent().getSymbolByID("demoModeMaxEvents").setVisible(event["value"])
	enableDemoMode.getComponent().getSymbolByID("demoModeIdleTimeout").setVisible(event["value"])
	enableDemoMode.getComponent().getSymbolByID("demoModeReplayDelay").setVisible(event["value"])
	event["source"].getSymbolByID("LIBARIA_DEMO_MODE_H").setEnabled(event["value"])
	event["source"].getSymbolByID("LIBARIA_DEMO_MODE_C").setEnabled(event["value"])
	
def onRTOSEnable(useRTOS, event):
	useRTOS.getComponent().getSymbolByID("useRTOSExtensions").setVisible(event["value"])
	useRTOS.getComponent().getSymbolByID("rtosfullBlockingMode").setVisible(event["value"])
	useRTOS.getComponent().getSymbolByID("rtosTaskSize").setVisible(event["value"])
	useRTOS.getComponent().getSymbolByID("rtosTaskPriority").setVisible(event["value"])
	useRTOS.getComponent().getSymbolByID("rtosEnableTaskDelay").setVisible(event["value"])
	useRTOS.getComponent().getSymbolByID("rtosTaskDelay").setVisible(event["value"])
	
def onEnableInputChanged(enableInput, event):
	enableInput.getComponent().setDependencyEnabled("sys_input", event["value"])
	
def onGenAriaDesignChanged(genAriaDesign, event):
	genAriaEvents = genAriaDesign.getComponent().getSymbolByID("genAriaDesign")
	genAriaEvents.setVisible(event["value"])
	genAriaEvents.setEnabled(event["value"])
	
	genAriaMacros = genAriaDesign.getComponent().getSymbolByID("genAriaMacros")
	genAriaMacros.setVisible(event["value"])
	genAriaMacros.setEnabled(event["value"])
	
def onJPEGEnableChanged(JPEGEnable, event):
	event["source"].getSymbolByID("GFXU_IMAGE_JPG_COMMON_H").setEnabled(event["value"])
	event["source"].getSymbolByID("GFXU_IMAGE_JPG_COMMON_C").setEnabled(event["value"])
	event["source"].getSymbolByID("JIDCTINT_C").setEnabled(event["value"])
	event["source"].getSymbolByID("GFXU_IMAGE_JPG_INTERNAL_C").setEnabled(event["value"])
	event["source"].getSymbolByID("GFXU_IMAGE_JPG_EXTERNAL_C").setEnabled(event["value"])
	
def onPNGEnableChanged(JPEGEnable, event):
	event["source"].getSymbolByID("GFXU_IMAGE_PNG_EXTERNAL_C").setEnabled(event["value"])
	event["source"].getSymbolByID("GFXU_IMAGE_PNG_INTERNAL_C").setEnabled(event["value"])
	event["source"].getSymbolByID("LODE_PNG_DECODER_H").setEnabled(event["value"])
	event["source"].getSymbolByID("LODE_PNG_DECODER_C").setEnabled(event["value"])
	
def onUseGlobalPaletteChanged(useGlobalPalette, event):
	# connected to HAL, update the global palette hint
	if event["source"].getDependencyComponent("gfx_hal") != None:
		Database.setSymbolValue("gfx_hal", "GlobalPaletteModeHint", event["value"], 1)
