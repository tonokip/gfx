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

componentsIDTable = ["HarmonyCore", "gfx_hal", "aria_gfx_library", "gfx_disp_atmxt-xpro_320x480", "gfx_driver_ili9488"]
autoConnectTable = [["gfx_hal", "gfx_display", "gfx_disp_atmxt-xpro_320x480", "gfx_display"],
					["aria_gfx_library", "gfx_hal", "gfx_hal", "gfx_hal"],
					["gfx_hal", "gfx_display_driver", "gfx_driver_ili9488", "gfx_driver_ili9488"]]
deactivateIDTable = ["FreeRTOS"]

execfile(Module.getPath() + "../common/pin_config.py")
execfile(Module.getPath() + "../common/bsp_utils.py")

#Add BSP support
execfile(Module.getPath() + "Support_BSP_SAM_E70_Xplained_Ultra.py")
execfile(Module.getPath() + "Support_BSP_SAM_C21_Xplained_Pro.py")

def enableILI9488SPIPins(bspID, enable):
	ili9488SPI4PinConfigs = getBSPSupportNode(bspID, "SPI 4-line").getPinConfig()
	if (ili9488SPI4PinConfigs != None):
		resetPins(ili9488SPI4PinConfigs)
		if (enable == True):
			configurePins(ili9488SPI4PinConfigs)

def enableILI9488ParallelPins(bspID, enable):
	ili9488ParallelPinConfigs = getBSPSupportNode(bspID, "Parallel").getPinConfig()
	if (ili9488ParallelPinConfigs != None):
		resetPins(ili9488ParallelPinConfigs)
		if (enable == True):
			configurePins(ili9488ParallelPinConfigs)

def enableSPIInterface(bspID, enable):
	componentIDTable = getBSPSupportNode(bspID, "SPI 4-line").getComponentActivateList()
	autoConnectTable = getBSPSupportNode(bspID, "SPI 4-line").getComponentAutoConnectList()
	if (enable == True):
		if (componentIDTable != None):
			res = Database.activateComponents(componentIDTable)
		if (autoConnectTable != None):
			res = Database.connectDependencies(autoConnectTable)
	elif (enable == False):
		if (componentIDTable != None):
			res = Database.deactivateComponents(componentIDTable)
	enableILI9488SPIPins(bspID, enable)
	if (getBSPSupportNode(bspID, "SPI 4-line").getEventCallbackFxn() != None):
		getBSPSupportNode(bspID, "SPI 4-line").getEventCallbackFxn()("configure")
	
def enableParallelInterface(bspID, enable):
	componentIDTable = getBSPSupportNode(bspID, "Parallel").getComponentActivateList()
	autoConnectTable = getBSPSupportNode(bspID, "Parallel").getComponentAutoConnectList()
	if (enable == True):
		if (componentIDTable != None):
			res = Database.activateComponents(componentIDTable)
		if (autoConnectTable != None):
			res = Database.connectDependencies(autoConnectTable)
	elif (enable == False):
		if (componentIDTable != None):
			res = Database.deactivateComponents(componentIDTable)
	enableILI9488ParallelPins(bspID, enable)
	if (getBSPSupportNode(bspID, "Parallel").getEventCallbackFxn() != None):
		getBSPSupportNode(bspID, "Parallel").getEventCallbackFxn()("configure")

def configureDisplayInterface(bspID, interface):
	print("Configuring for " + str(interface) + " Interface.")
	if (bspID == None):
		print("No BSP used, will not configure")
	else:
		if (str(interface) == "SPI 4-line"):
			enableParallelInterface(bspID, False)
			enableSPIInterface(bspID, True)
		elif (str(interface) == "Parallel"):
			enableSPIInterface(bspID, False)
			enableParallelInterface(bspID, True)

def onDisplayInterfaceSelected(interfaceSelected, event):
	bspID = getSupportedBSP()
	newDisplayInterface= interfaceSelected.getComponent().getSymbolByID("DisplayInterface").getValue()
	currDisplayInterface = interfaceSelected.getComponent().getSymbolByID("currDisplayInterface").getValue()
	interfaceSelected.getComponent().getSymbolByID("currDisplayInterface").setValue(event["value"], 1)
	configureDisplayInterface(bspID, str(newDisplayInterface))

def instantiateComponent(bspComponent):
	global componentsIDTable
	global autoConnectTable
	global supportedBSPsIDList
	
	#Check if a supported BSP is loaded
	bspID = getSupportedBSP()

	res = Database.activateComponents(componentsIDTable)
	res = Database.connectDependencies(autoConnectTable)
	res = Database.deactivateComponents(deactivateIDTable);
	
	#DisplayInterface = bspComponent.createComboSymbol("DisplayInterface", None, ["SPI 4-line", "Parallel"])
	DisplayInterface = bspComponent.createComboSymbol("DisplayInterface", None, ["SPI 4-line"])
	DisplayInterface.setLabel("Display Interface")
	DisplayInterface.setDescription("Configures the display interface to the maXTouch Xplained Pro display.")
	DisplayInterface.setDefaultValue("SPI 4-line")
	DisplayInterface.setDependencies(onDisplayInterfaceSelected, ["DisplayInterface"])
	DisplayInterface.setVisible(True)
	
	# Shadow display interface symbol
	currDisplayInterface = bspComponent.createComboSymbol("currDisplayInterface", None, ["SPI 4-line", "Parallel"])
	currDisplayInterface.setDefaultValue("SPI 4-line")
	currDisplayInterface.setVisible(False)
	
	if (bspID != None):
		configureDisplayInterface(bspID, str(currDisplayInterface.getValue()))
	else:
		print("No BSP used, only software components are configured. Please add board-specific components.")

