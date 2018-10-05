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

def instantiateComponent(comp):
	Width = comp.createIntegerSymbol("Width", None)
	Width.setLabel("Width")
	Width.setDescription("The width of the touch panel in pixels.")
	Width.setDefaultValue(480)
	
	Height = comp.createIntegerSymbol("Height", None)
	Height.setLabel("Height")
	Height.setDescription("The height of the touch panel in pixels.")
	Height.setDefaultValue(272)
	
def onDependentComponentAdded(component, dependencyID, dependencyComponent):
	if dependencyID == "touch_panel":
		component.setSymbolValue("Width", dependencyComponent.getSymbolValue("TouchWidth"), 1)
		component.setSymbolValue("Height", dependencyComponent.getSymbolValue("TouchHeight"), 1)
	
def onDependentComponentRemoved(component, dependencyID, dependencyComponent):
	if dependencyID == "touch_panel":
		component.clearSymbolValue("Width")
		component.clearSymbolValue("Height")