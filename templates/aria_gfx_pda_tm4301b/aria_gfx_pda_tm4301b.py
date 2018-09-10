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
			configurePins(getBSPSupportNode(bspUsedKeyID, None).getPinConfig())

	res = Database.activateComponents(componentsIDTable)
	res = Database.connectDependencies(autoConnectTable)
	res = Database.deactivateComponents(deactivateIDTable);

	Database.setSymbolValue("aria_gfx_library", "enableInput", True, 1)

	if (bspUsedKeyID == None):
		print("No BSP used, only software components are configured. Please add board-specific components")
