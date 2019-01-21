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

def instantiateComponent(comp):
	print("Instantiated GFX2D driver component")
	projectPath = "config/" + Variables.get("__CONFIGURATION_NAME") + "/gfx/driver/gfx2d"

	# generated code files
	GFX_GFX2D_C = comp.createFileSymbol("GFX_GFX2D_C", None)
	GFX_GFX2D_C.setDestPath("gfx/driver/processor/gfx2d/")
	GFX_GFX2D_C.setOutputName("drv_gfx_gfx2d.c")
	GFX_GFX2D_C.setProjectPath(projectPath)
	GFX_GFX2D_C.setType("SOURCE")
	GFX_GFX2D_C.setMarkup(True)
	
	GFX_GFX2D_H = comp.createFileSymbol("GFX_GFX2D_H", None)
	GFX_GFX2D_H.setDestPath("gfx/driver/processor/gfx2d/")
	GFX_GFX2D_H.setOutputName("drv_gfx_gfx2d.h")
	GFX_GFX2D_H.setProjectPath(projectPath)
	GFX_GFX2D_H.setType("HEADER")
	GFX_GFX2D_H.setMarkup(True)

	GFX_GFX2D_C.setSourcePath("templates/drv_gfx_gfx2d.c.ftl")
	GFX_GFX2D_H.setSourcePath("templates/drv_gfx_gfx2d.h.ftl")
	