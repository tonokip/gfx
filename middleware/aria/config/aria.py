# coding: utf-8
##############################################################################
# Copyright (C) 2018 Microchip Technology Inc. and its subsidiaries.
#
# Subject to your compliance with these terms, you may use Microchip software
# and any derivatives exclusively with Microchip products. It is your
# responsibility to comply with third party license terms applicable to your
# use of third party software (including open source software) that may
# accompany Microchip software.
#
# THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
# EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
# WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
# PARTICULAR PURPOSE.
#
# IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
# INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
# WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
# BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
# FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
# ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
# THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
##############################################################################

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

def onAttachmentConnected(source, target):
	if source["id"] == "gfx_hal":
		target["component"].setSymbolValue("GlobalPaletteModeHint", source["component"].getSymbolValue("useGlobalPalette"), 1)
		target["component"].setSymbolValue("DisableGlobalPaletteModeHint", True, 1)

def onAttachmentDisconnected(source, target):
	if source["id"] == "gfx_hal":
		target["component"].clearSymbolValue("GlobalPaletteModeHint")
		target["component"].clearSymbolValue("DisableGlobalPaletteModeHint")
	
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
