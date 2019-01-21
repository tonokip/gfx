# coding: utf-8
"""*****************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
*
* Subject to your compliance with these terms, you may use Microchip software
* and any derivatives exclusively with Microchip products. It is your
* responsibility to comply with third party license terms applicable to your
* use of third party software (including open source software) that may
* accompany Microchip software.
*
* THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
* EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
* WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
* PARTICULAR PURPOSE.
*
* IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
* INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
* WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
* BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
* FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
* ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
* THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
*****************************************************************************"""

###################################################################################################
########################### Global variables   #################################
###################################################################################################
global gfx2dInstanceName

###################################################################################################
########################### Callback Functions   #################################
###################################################################################################


###################################################################################################
########################### Component   #################################
###################################################################################################
def instantiateComponent(gfx2dComponent):
    global gfx2dInstanceName
    gfx2dInstanceName = gfx2dComponent.createStringSymbol("GFX2D_INSTANCE_NAME", None)
    gfx2dInstanceName.setVisible(False)
    gfx2dInstanceName.setDefaultValue(gfx2dComponent.getID().upper())

    Log.writeInfoMessage("Running " + gfx2dInstanceName.getValue())

    configName = Variables.get("__CONFIGURATION_NAME")

###################################################################################################
########################### Code Generation   #################################
###################################################################################################
    gfx2d = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"GFX2D\"]")
    #gfx2DID = gfx2d.getAttribute("id")

    gfx2dHeaderFile = gfx2dComponent.createFileSymbol("GFX2D_HEADER", None)
    gfx2dHeaderFile.setSourcePath("peripheral/gfx2d_44061/templates/plib_gfx2d.h.ftl")
    gfx2dHeaderFile.setOutputName("plib_"+gfx2dInstanceName.getValue().lower() + ".h")
    gfx2dHeaderFile.setDestPath("peripheral/gfx2d/")
    gfx2dHeaderFile.setProjectPath("config/" + configName +"/peripheral/gfx2d/")
    gfx2dHeaderFile.setType("HEADER")
    gfx2dHeaderFile.setMarkup(True)

    gfx2dGlobalHeaderFile = gfx2dComponent.createFileSymbol("GFX2D_GLOBALHEADER", None)
    gfx2dGlobalHeaderFile.setSourcePath("peripheral/gfx2d_44061/templates/plib_gfx2d_common.h")
    gfx2dGlobalHeaderFile.setOutputName("plib_gfx2d_common.h")
    gfx2dGlobalHeaderFile.setDestPath("peripheral/gfx2d/")
    gfx2dGlobalHeaderFile.setProjectPath("config/" + configName +"/peripheral/gfx2d/")
    gfx2dGlobalHeaderFile.setType("HEADER")

    gfx2dSource1File = gfx2dComponent.createFileSymbol("GFX2D_SOURCE", None)
    gfx2dSource1File.setSourcePath("peripheral/gfx2d_44061/templates/plib_gfx2d.c.ftl")
    gfx2dSource1File.setOutputName("plib_"+gfx2dInstanceName.getValue().lower()+".c")
    gfx2dSource1File.setDestPath("peripheral/gfx2d/")
    gfx2dSource1File.setProjectPath("config/" + configName +"/peripheral/gfx2d/")
    gfx2dSource1File.setType("SOURCE")
    gfx2dSource1File.setMarkup(True)

    gfx2dSystemInitFile = gfx2dComponent.createFileSymbol("GFX2D_INIT", None)
    gfx2dSystemInitFile.setType("STRING")
    gfx2dSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    gfx2dSystemInitFile.setSourcePath("peripheral/gfx2d_44061/templates/system/system_initialize.c.ftl")
    gfx2dSystemInitFile.setMarkup(True)

    gfx2dSystemDefFile = gfx2dComponent.createFileSymbol("GFX2D_DEF", None)
    gfx2dSystemDefFile.setType("STRING")
    gfx2dSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    gfx2dSystemDefFile.setSourcePath("peripheral/gfx2d_44061/templates/system/system_definitions.h.ftl")
    gfx2dSystemDefFile.setMarkup(True)
  
