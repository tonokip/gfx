def instantiateComponent(component):
	execfile(Module.getPath() + "/config/aria_config.py")
	execfile(Module.getPath() + "/config/aria_demomode.py")
	execfile(Module.getPath() + "/config/aria_rtos.py")
	execfile(Module.getPath() + "/config/aria_files.py")
	

def onDependentComponentAdded(aria, dependencyID, hal):
	print("lo here")
	aria.setSymbolValue("displayWidth", hal.getSymbolValue("DisplayWidth"), 1)
	aria.setSymbolValue("displayHeight", hal.getSymbolValue("DisplayHeight"), 1)

def onDependentComponentRemoved(aria, dependencyID, hal):
	print("lo there")
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
	print("here")
	displayWidth.setValue(event["value"], 1)
	
def onDisplayHeightChanged(displayHeight, event):
	print("there")
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