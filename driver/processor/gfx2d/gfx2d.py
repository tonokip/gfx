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

    if rtos_mode != None:
        if rtos_mode == "BareMetal":
            symbol.setValue("Asynchronous", 1)
        else:
            symbol.setValue("Synchronous", 1)

def instantiateComponent(comp):
	print("Instantiated GFX2D driver component")
	projectPath = "config/" + Variables.get("__CONFIGURATION_NAME") + "/gfx/driver/gfx2d"

	gfx2d_default_mode = "Synchronous"

    	gfx2dSymPLIB = comp.createStringSymbol("DRV_GFX2D_PLIB", None)
    	gfx2dSymPLIB.setLabel("PLIB Used")
    	gfx2dSymPLIB.setReadOnly(True)
    	gfx2dSymPLIB.setDefaultValue("")

    	gfx2dMode = comp.createComboSymbol("DRV_GFX2D_MODE", None, ["Asynchronous", "Synchronous"])
    	gfx2dMode.setLabel("Driver Mode")
    	gfx2dMode.setDefaultValue(gfx2d_default_mode)
    	gfx2dMode.setDependencies(setCommonMode, ["HarmonyCore.SELECT_RTOS"])

    	gfx2dSymQueueSize = comp.createIntegerSymbol("DRV_GFX2D_QUEUE_SIZE", None)
    	gfx2dSymQueueSize.setLabel("Transfer Queue Size")
    	gfx2dSymQueueSize.setMax(64)
    	gfx2dSymQueueSize.setVisible((Database.getSymbolValue("drv_gfx2d", "DRV_GFX2D_MODE") == "Asynchronous"))
    	gfx2dSymQueueSize.setDefaultValue(2)
    	gfx2dSymQueueSize.setDependencies(asyncModeOptions, ["drv_gfx2d.DRV_GFX2D_MODE"])

	# generated code files
	GFX_GFX2D_C = comp.createFileSymbol("GFX_GFX2D_C", None)
	GFX_GFX2D_C.setDestPath("gfx/driver/processor/gfx2d/")
	GFX_GFX2D_C.setOutputName("drv_gfx2d.c")
	GFX_GFX2D_C.setProjectPath(projectPath)
	GFX_GFX2D_C.setType("SOURCE")
	GFX_GFX2D_C.setMarkup(True)
	GFX_GFX2D_C.setSourcePath("templates/drv_gfx2d.c.ftl")
	
	GFX_GFX2D_H = comp.createFileSymbol("GFX_GFX2D_H", None)
	GFX_GFX2D_H.setDestPath("gfx/driver/processor/gfx2d/")
	GFX_GFX2D_H.setOutputName("drv_gfx2d.h")
	GFX_GFX2D_H.setProjectPath(projectPath)
	GFX_GFX2D_H.setType("HEADER")
	GFX_GFX2D_H.setMarkup(True)
	GFX_GFX2D_H.setSourcePath("templates/drv_gfx2d.h.ftl")


    	# System Template Files
    	gfx2dSymSystemDefObjFile = comp.createFileSymbol("DRV_GFX2D_FILE_SYS_DEF_OBJ", None)
    	gfx2dSymSystemDefObjFile.setType("STRING")
    	gfx2dSymSystemDefObjFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_OBJECTS")
    	gfx2dSymSystemDefObjFile.setSourcePath("templates/system/system_definitions_objects.h.ftl")
    	gfx2dSymSystemDefObjFile.setMarkup(True)

    	gfx2dSymSystemConfigFile = comp.createFileSymbol("DRV_GFX2D_FILE_SYS_CONFIG", None)
    	gfx2dSymSystemConfigFile.setType("STRING")
    	gfx2dSymSystemConfigFile.setOutputName("core.LIST_SYSTEM_CONFIG_H_DRIVER_CONFIGURATION")
    	gfx2dSymSystemConfigFile.setSourcePath("templates/system/system_config.h.ftl")
    	gfx2dSymSystemConfigFile.setMarkup(True)

    	gfx2dSymSystemInitDataFile = comp.createFileSymbol("DRV_GFX2D_FILE_SYS_INIT_DATA", None)
    	gfx2dSymSystemInitDataFile.setType("STRING")
    	gfx2dSymSystemInitDataFile.setOutputName("core.LIST_SYSTEM_INIT_C_DRIVER_INITIALIZATION_DATA")
    	gfx2dSymSystemInitDataFile.setSourcePath("templates/system/system_initialize_data.c.ftl")
    	gfx2dSymSystemInitDataFile.setMarkup(True)

    	gfx2dSymSystemInitFile = comp.createFileSymbol("DRV_GFX2D_FILE_SYS_INIT", None)
    	gfx2dSymSystemInitFile.setType("STRING")
    	gfx2dSymSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_DRIVERS")
    	gfx2dSymSystemInitFile.setSourcePath("templates/system/system_initialize.c.ftl")
    	gfx2dSymSystemInitFile.setMarkup(True)

        gfx2dSymSystemDefFile = comp.createFileSymbol("DRV_GFX2D_FILE_SYS_DEF", None)
        gfx2dSymSystemDefFile.setType("STRING")
        gfx2dSymSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
        gfx2dSymSystemDefFile.setSourcePath("templates/system/system_definitions.h.ftl")
        gfx2dSymSystemDefFile.setMarkup(True)

    	# Global Header Files
    	gfx2dSymHeaderDefFile = comp.createFileSymbol("DRV_GFX2D_FILE_DEF_HEADER", None)
    	gfx2dSymHeaderDefFile.setSourcePath("templates/drv_gfx2d_definitions.h.ftl")
    	gfx2dSymHeaderDefFile.setOutputName("drv_gfx2d_definitions.h")
    	gfx2dSymHeaderDefFile.setDestPath("gfx/driver/processor/gfx2d/")
    	gfx2dSymHeaderDefFile.setProjectPath(projectPath)
    	gfx2dSymHeaderDefFile.setType("HEADER")
    	gfx2dSymHeaderDefFile.setMarkup(True)
    	gfx2dSymHeaderDefFile.setOverwrite(True)


def asyncModeOptions(symbol, event):
    if (event["value"] == "Asynchronous"):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def configureGFX2DComponent(gpuComponent, comp):
	print("GFX2D Driver: Connecting GFX2D")
	
def resetGFX2DComponent(gpuComponent, comp):
	print("GFX2D Driver: Disconnecting GFX2D")

def onAttachmentConnected(source, target):
	print("dependency Connected = " + str(target['id']))
	#### test for GFX2D dependency

def onAttachmentDisconnected(source, target):
	print("dependency Disconnected = " + str(target['id']))

