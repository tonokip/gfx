# coding: utf-8
##############################################################################
# Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
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

def setCommonMode(symbol, event):
    rtos_mode = event["value"]


def instantiateComponent(comp):
	print("Instantiated 2DGPU driver component")
	projectPath = "config/" + Variables.get("__CONFIGURATION_NAME") + "/gfx/driver/2dgpu"

        gfx2DGPU_default_mode = "Synchronous"

    	gfx2DGPUSymLIB = comp.createStringSymbol("DRV_2DGPU_LIB", None)
    	gfx2DGPUSymLIB.setLabel("LIB Used")
    	gfx2DGPUSymLIB.setReadOnly(True)
    	gfx2DGPUSymLIB.setDefaultValue("")

    	gfx2DGPUMode = comp.createComboSymbol("DRV_2DGPU_MODE", None, ["Asynchronous", "Synchronous"])
    	gfx2DGPUMode.setLabel("Driver Mode")
    	gfx2DGPUMode.setDefaultValue(gfx2DGPU_default_mode)
    	gfx2DGPUMode.setDependencies(setCommonMode, ["HarmonyCore.SELECT_RTOS"])

    	gfx2DGPUSymQueueSize = comp.createIntegerSymbol("DRV_2DGPU_QUEUE_SIZE", None)
    	gfx2DGPUSymQueueSize.setLabel("Transfer Queue Size")
    	gfx2DGPUSymQueueSize.setMax(64)
    	gfx2DGPUSymQueueSize.setVisible((Database.getSymbolValue("drv_2dgpu", "DRV_2DGPU_MODE") == "Asynchronous"))
    	gfx2DGPUSymQueueSize.setDefaultValue(2)
    	gfx2DGPUSymQueueSize.setDependencies(asyncModeOptions, ["drv_2dgpu.DRV_2DGPU_MODE"])

	# generated code files
	GFX_2DGPU_A = comp.createFileSymbol("DRV_LIB_2DGPU", None)
	GFX_2DGPU_A.setDestPath("gfx/driver/processor/2dgpu/lib")
	GFX_2DGPU_A.setOutputName("lib2dgpu.a")
	GFX_2DGPU_A.setProjectPath(projectPath)
	GFX_2DGPU_A.setType("LIBRARY")
	#GFX_2DGPU_A.setMarkup(True)
	GFX_2DGPU_A.setSourcePath("lib/lib2dgpu.a")

    	# System Template Files
    	gfx2DGPUSymSystemDefObjFile = comp.createFileSymbol("DRV_2DGPU_FILE_SYS_DEF_OBJ", None)
    	gfx2DGPUSymSystemDefObjFile.setType("STRING")
    	gfx2DGPUSymSystemDefObjFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_OBJECTS")
    	gfx2DGPUSymSystemDefObjFile.setSourcePath("templates/system/system_definitions_objects.h.ftl")
    	gfx2DGPUSymSystemDefObjFile.setMarkup(True)

    	gfx2DGPUSymSystemConfigFile = comp.createFileSymbol("DRV_2DGPU_FILE_SYS_CONFIG", None)
    	gfx2DGPUSymSystemConfigFile.setType("STRING")
    	gfx2DGPUSymSystemConfigFile.setOutputName("core.LIST_SYSTEM_CONFIG_H_DRIVER_CONFIGURATION")
    	gfx2DGPUSymSystemConfigFile.setSourcePath("templates/system/system_config.h.ftl")
    	gfx2DGPUSymSystemConfigFile.setMarkup(True)

    	gfx2DSymSystemInitDataFile = comp.createFileSymbol("DRV_2DGPU_FILE_SYS_INIT_DATA", None)
    	gfx2DSymSystemInitDataFile.setType("STRING")
    	gfx2DSymSystemInitDataFile.setOutputName("core.LIST_SYSTEM_INIT_C_DRIVER_INITIALIZATION_DATA")
    	gfx2DSymSystemInitDataFile.setSourcePath("templates/system/system_initialize_data.c.ftl")
    	gfx2DSymSystemInitDataFile.setMarkup(True)

    	gfx2DSymSystemInitFile = comp.createFileSymbol("DRV_2DGPU_FILE_SYS_INIT", None)
    	gfx2DSymSystemInitFile.setType("STRING")
    	gfx2DSymSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_DRIVERS")
    	gfx2DSymSystemInitFile.setSourcePath("templates/system/system_initialize.c.ftl")
    	gfx2DSymSystemInitFile.setMarkup(True)

        gfx2DSymSystemDefFile = comp.createFileSymbol("DRV_2DGPU_FILE_SYS_DEF", None)
        gfx2DSymSystemDefFile.setType("STRING")
        gfx2DSymSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
        gfx2DSymSystemDefFile.setSourcePath("templates/system/system_definitions.h.ftl")
        gfx2DSymSystemDefFile.setMarkup(True)

    	# Global Header Files
    	gfx2DSymHeaderDefFile = comp.createFileSymbol("DRV_2DGPU_FILE_DEF_HEADER", None)
    	gfx2DSymHeaderDefFile.setSourcePath("templates/drv_2dgpu_definitions.h.ftl")
    	gfx2DSymHeaderDefFile.setOutputName("drv_2dgpu_definitions.h")
    	gfx2DSymHeaderDefFile.setDestPath("gfx/driver/processor/2dgpu/")
    	gfx2DSymHeaderDefFile.setProjectPath(projectPath)
    	gfx2DSymHeaderDefFile.setType("HEADER")
    	gfx2DSymHeaderDefFile.setMarkup(True)
    	gfx2DSymHeaderDefFile.setOverwrite(True)

    	gfx2DSymHeaderFile = comp.createFileSymbol("DRV_2DGPU_FILE_MAIN_HEADER", None)
    	gfx2DSymHeaderFile.setSourcePath("templates/drv_2dgpu.h.ftl")
    	gfx2DSymHeaderFile.setOutputName("drv_2dgpu.h")
    	gfx2DSymHeaderFile.setDestPath("driver/2dgpu/")
    	gfx2DSymHeaderFile.setProjectPath(projectPath)
    	gfx2DSymHeaderFile.setType("HEADER")
        gfx2DSymHeaderFile.setMarkup(True)
    	gfx2DSymHeaderFile.setOverwrite(True)

    	gfx2DHalFile = comp.createFileSymbol("DRV_2DGPU_FILE_HAL", None)
    	gfx2DHalFile.setSourcePath("templates/drv_2dgpu_hal.c.ftl")
    	gfx2DHalFile.setOutputName("drv_2dgpu.h")
    	gfx2DHalFile.setDestPath("driver/2dgpu/")
    	gfx2DHalFile.setProjectPath(projectPath)
    	gfx2DHalFile.setType("HEADER")
        gfx2DHalFile.setMarkup(True)
    	gfx2DHalFile.setOverwrite(True)


def asyncModeOptions(symbol, event):
    if (event["value"] == "Asynchronous"):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def configure2DGPUComponent(gpuComponent, comp):
	print("2DGPU Driver: Connecting 2DGPU")
	
def reset2DGPUComponent(gpuComponent, comp):
	print("2DGPU Driver: Disconnecting 2DGPU")

def onAttachmentConnected(source, target):
	print("dependency Connected = " + str(target['id']))
	#### test for 2DGPU dependency

def onAttachmentDisconnected(source, target):
	print("dependency Disconnected = " + str(target['id']))

