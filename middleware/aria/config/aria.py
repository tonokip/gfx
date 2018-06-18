def instantiateComponent(component):
	projectPath = "config/" + Variables.get("__CONFIGURATION_NAME") + "/gfx/libaria"
	
	execfile(Module.getPath() + "/config/aria_config.py")
	execfile(Module.getPath() + "/utils/config/aria_utils.py")
	execfile(Module.getPath() + "/third_party/config/aria_thirdparty.py")
	execfile(Module.getPath() + "/config/aria_demomode.py")
	execfile(Module.getPath() + "/config/aria_rtos.py")
	execfile(Module.getPath() + "/config/aria_files.py")

def onDependentComponentAdded(aria, dependencyID, hal):
	aria.setSymbolValue("displayWidth", hal.getSymbolValue("DisplayWidth"), 1)
	aria.setSymbolValue("displayHeight", hal.getSymbolValue("DisplayHeight"), 1)

def onDependentComponentRemoved(aria, dependencyID, hal):
	displayWidth.clearValue()
	displayHeight.clearValue()
	
def onDemoModeEnable(enableDemoMode, event):
	enableDemoMode.getComponent().getSymbolByID("demoModeRecordInput").setVisible(event["value"])
	enableDemoMode.getComponent().getSymbolByID("demoModeRecordTickPeriod").setVisible(event["value"])
	enableDemoMode.getComponent().getSymbolByID("demoModeMaxEvents").setVisible(event["value"])
	enableDemoMode.getComponent().getSymbolByID("demoModeIdleTimeout").setVisible(event["value"])
	enableDemoMode.getComponent().getSymbolByID("demoModeReplayDelay").setVisible(event["value"])
	
def onRTOSEnable(useRTOS, event):
	useRTOS.getComponent().getSymbolByID("useRTOSExtensions").setVisible(event["value"])
	useRTOS.getComponent().getSymbolByID("rtosfullBlockingMode").setVisible(event["value"])
	useRTOS.getComponent().getSymbolByID("rtosTaskSize").setVisible(event["value"])
	useRTOS.getComponent().getSymbolByID("rtosTaskPriority").setVisible(event["value"])
	useRTOS.getComponent().getSymbolByID("rtosEnableTaskDelay").setVisible(event["value"])
	useRTOS.getComponent().getSymbolByID("rtosTaskDelay").setVisible(event["value"])
	
def onDisplayWidthChanged(displayWidth, event):
	displayWidth.setValue(event["value"], 1)
	
def onDisplayHeightChanged(displayHeight, event):
	displayHeight.setValue(event["value"], 1)
	
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
	