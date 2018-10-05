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

execfile(Module.getPath() + "../common/pin_config.py")
execfile(Module.getPath() + "../common/bsp_utils.py")

execfile(Module.getPath() + "Support_BSP_SAM_E70_Xplained_Ultra.py")

def instantiateComponent(templateComponent):
	componentsIDTable = ["HarmonyCore", "sys_input", "gfx_hal", "aria_gfx_library", "gfx_disp_pdatm4301b_480x272", "gfx_maxtouch_controller"]
	autoConnectTable = [["gfx_hal", "gfx_display", "gfx_disp_pdatm4301b_480x272", "gfx_display"],
						["aria_gfx_library", "gfx_hal", "gfx_hal", "gfx_hal"],
						["gfx_maxtouch_controller", "touch_panel", "gfx_disp_pdatm4301b_480x272", "touch_panel"]]
	deactivateIDTable = ["FreeRTOS"]

	#Check if a supported BSP is loaded
	bspUsedKeyID = getSupportedBSP()

	if (bspUsedKeyID != None):
		print("Configuring for BSP : " + bspUsedKeyID)
		if (getBSPSupportNode(bspUsedKeyID, None).getComponentActivateList() != None):
			componentsIDTable += getBSPSupportNode(bspUsedKeyID, None).getComponentActivateList()
		if (getBSPSupportNode(bspUsedKeyID, None).getComponentAutoConnectList() != None):
			autoConnectTable += getBSPSupportNode(bspUsedKeyID, None).getComponentAutoConnectList()
		if (getBSPSupportNode(bspUsedKeyID, None).getPinConfig() != None):
			resetPins(getBSPSupportNode(bspUsedKeyID, None).getPinConfig())
			configurePins(getBSPSupportNode(bspUsedKeyID, None).getPinConfig())

	res = Database.activateComponents(componentsIDTable)
	res = Database.connectDependencies(autoConnectTable)
	res = Database.deactivateComponents(deactivateIDTable);

	Database.setSymbolValue("aria_gfx_library", "enableInput", True, 1)

	if (bspUsedKeyID == None):
		print("No BSP used, only software components are configured. Please add board-specific components")
