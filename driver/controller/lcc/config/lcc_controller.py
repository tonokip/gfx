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

import re

def instantiateComponent(comp):
	projectPath = "config/" + Variables.get("__CONFIGURATION_NAME") + "/gfx/driver/lcc"
	
	comp.setHelpFile("../../../docs/help_harmony_gfx_html_alias.h")
	#comp.setHelp("IDH_HTML_GFX_CMP__3__Display_Driver_Component")
	
	HALConnected = comp.createBooleanSymbol("HALConnected", None)
	HALConnected.setVisible(False)
	HALConnected.setDependencies(onHALConnected, ["HALConnected"])
	
	# these two symbols are read by the HAL for initialization purposes
	# they must match the function names in the actual driver code
	DriverInfoFunction = comp.createStringSymbol("DriverInfoFunction", None)
	DriverInfoFunction.setLabel("Driver Info Function Name")
	DriverInfoFunction.setReadOnly(True)
	DriverInfoFunction.setDefaultValue("driverLCCInfoGet")
	DriverInfoFunction.setVisible(False)
	
	DriverInitFunction = comp.createStringSymbol("DriverInitFunction", None)
	DriverInitFunction.setLabel("Driver Init Function Name")
	DriverInitFunction.setReadOnly(True)
	DriverInitFunction.setDefaultValue("driverLCCContextInitialize")
	DriverInitFunction.setVisible(False)
	
	# configuration options
	HALComment = comp.createCommentSymbol("HALComment", None)
	HALComment.setLabel("Some settings are being managed by the GFX Core and have been hidden.")
	HALComment.setVisible(False)
	
	DisplayWidth = comp.createIntegerSymbol("DisplayWidth", None)
	DisplayWidth.setLabel("Width")
	DisplayWidth.setDescription("The width of the frame buffer in pixels.")
	DisplayWidth.setDefaultValue(480)

	DisplayHeight = comp.createIntegerSymbol("DisplayHeight", None)
	DisplayHeight.setLabel("Height")
	DisplayHeight.setDescription("The height of the frame buffer in pixels.")
	DisplayHeight.setDefaultValue(272)
	
	PixelClock = comp.createIntegerSymbol("PixelClock", None)
	PixelClock.setLabel("Pixel Clock (Hz)")
	PixelClock.setReadOnly(True)
	PixelClock.setDescription("The approximate pixel clock frequency generated by the LCC. Fixed value, no configuration options available.")
	PixelClock.setDefaultValue(6250000)
	
	DisplayTimingOptionsEnabled = comp.createBooleanSymbol("DisplayTimingOptionsEnabled", None)
	DisplayTimingOptionsEnabled.setLabel("Display Timing Options Enabled")
	DisplayTimingOptionsEnabled.setDescription("Hints to the HAL if display timing is configurable for this display.")
	DisplayTimingOptionsEnabled.setDefaultValue(True)
	DisplayTimingOptionsEnabled.setVisible(False)
	
	#PixelSupportLevel = comp.createStringSymbol("PixelSupportLevel")
	#PixelSupportLevel.setLabel("WQVGA or lower")
	#PixelSupportLevel.setReadOnly(True)
	#PixelSupportLevel.setDescription("The total number of pixels expected to be supportable.")
	
	LCCRefresh = comp.createBooleanSymbol("LCCRefresh", None)
	LCCRefresh.setLabel("Use Aggressive Refresh Strategy?")
	LCCRefresh.setDescription("<html>Indicates that the LCC refresh loop should attempt<br>to aggresively refresh the display.  May cause<br>display artifacts but is needed for some larger displays.</html>")
	
	DisplaySettingsMenu = comp.createMenuSymbol("DisplaySettingsMenu", None)
	DisplaySettingsMenu.setLabel("Display Settings")
	
	DisplayBacklightEnable = comp.createIntegerSymbol("DisplayBacklightEnable", DisplaySettingsMenu)
	DisplayBacklightEnable.setLabel("Back Light Enable Value")
	DisplayBacklightEnable.setDescription("The value used to enable the display back light.")
	DisplayBacklightEnable.setDefaultValue(1)

	DisplayVSYNCNegative = comp.createBooleanSymbol("DisplayVSYNCNegative", DisplaySettingsMenu)
	DisplayVSYNCNegative.setLabel("VSYNC Polarity Positive?")
	DisplayVSYNCNegative.setDescription("Indicates if this display requries negative VSYNC polarity.")
	DisplayVSYNCNegative.setDefaultValue(True)

	DisplayHSYNCNegative = comp.createBooleanSymbol("DisplayHSYNCNegative", DisplaySettingsMenu)
	DisplayHSYNCNegative.setLabel("HSYNC Polarity Positive?")
	DisplayHSYNCNegative.setDescription("Indicates if this display requries negative HSYNC polarity.")
	DisplayHSYNCNegative.setDefaultValue(True)

	DisplayDataEnable = comp.createBooleanSymbol("DisplayDataEnable", DisplaySettingsMenu)
	DisplayDataEnable.setLabel("Use Data Enable?")
	DisplayDataEnable.setDescription("Indicates if this display requries the use of the Data Enable line.")
	DisplayDataEnable.setDefaultValue(True)

	DisplayDataEnablePolarity = comp.createBooleanSymbol("DisplayDataEnablePolarity", DisplaySettingsMenu)
	DisplayDataEnablePolarity.setLabel("Data Enable Polarity Positive?")
	DisplayDataEnablePolarity.setDescription("Indicates if this display Data Enable polarity is positive.")
	DisplayDataEnablePolarity.setDefaultValue(True)

	DisplayUseReset = comp.createBooleanSymbol("DisplayUseReset", DisplaySettingsMenu)
	DisplayUseReset.setLabel("Use Reset?")
	DisplayUseReset.setDescription("Indicates if this display reset line should be used.")
	DisplayUseReset.setDefaultValue(True)

	DisplayResetPolarity = comp.createBooleanSymbol("DisplayResetPolarity", DisplaySettingsMenu)
	DisplayResetPolarity.setLabel("Reset Polarity Positive?")
	DisplayResetPolarity.setDescription("Indicates if this display reset line should be reset positive.")
	DisplayResetPolarity.setDefaultValue(True)
	
	DisplayUseChipSelect = comp.createBooleanSymbol("DisplayUseChipSelect", DisplaySettingsMenu)
	DisplayUseChipSelect.setLabel("Use Chip Select?")
	DisplayUseChipSelect.setDescription("Indicates if this display uses the chip select line.")
	DisplayUseChipSelect.setDefaultValue(True)

	DisplayChipSelectPolarity = comp.createBooleanSymbol("DisplayChipSelectPolarity", DisplaySettingsMenu)
	DisplayChipSelectPolarity.setLabel("Chip Select Polarity Positive?")
	DisplayChipSelectPolarity.setDescription("Indicates if this display chip select line should be positive.")
	DisplayChipSelectPolarity.setDefaultValue(True)
	
	FrameBufferSettingsMenu = comp.createMenuSymbol("FrameBufferSettingsMenu", None)
	FrameBufferSettingsMenu.setLabel("Frame Buffer Settings")

	DoubleBuffer = comp.createBooleanSymbol("DoubleBuffer", FrameBufferSettingsMenu)
	DoubleBuffer.setLabel("Use Double Buffering?")
	DoubleBuffer.setDescription("<html>Uses an additional buffer for off-screen drawing.<br>Eliminates screen tearing but doubles the required memory.</html>")

	PaletteMode = comp.createBooleanSymbol("PaletteMode", FrameBufferSettingsMenu)
	PaletteMode.setLabel("Use 8-bit Palette?")
	PaletteMode.setDescription("<html>Enables frame buffer compression.<br>Uses an 8-bit color lookup table to reduce the required<br>frame buffer memory size.  This also reduces the<br>maximum avilable color count to 256 and significantly<br>slows down display refresh speed.</html>")

	UseCachedFrameBuffer = comp.createBooleanSymbol("UseCachedFrameBuffer", FrameBufferSettingsMenu)
	UseCachedFrameBuffer.setLabel("Uses Cache?")
	UseCachedFrameBuffer.setDescription("Specifies if frame buffer is cached and needs to be managed by the LCC driver.")
	UseCachedFrameBuffer.setDefaultValue(True)
	UseCachedFrameBuffer.setDependencies(OnCacheEnabled, ["core.DATA_CACHE_ENABLE"])

	#FrameBufferMemory = comp.createComboSymbol("FrameBufferMemory", FrameBufferSettingsMenu, ["Internal SRAM", "External SDRAM"])
	FrameBufferMemory = comp.createComboSymbol("FrameBufferMemory", FrameBufferSettingsMenu, ["Internal SRAM"])
	FrameBufferMemory.setLabel("Memory Interface")
	FrameBufferMemory.setDescription("Memory used for Frame Buffer")
	FrameBufferMemory.setDefaultValue("Internal SRAM")
	
	DMAMenu = comp.createMenuSymbol("DMAMenu", None)
	DMAMenu.setLabel("DMA Settings")
	
	DMAChannel = comp.createIntegerSymbol("DMAChannel", DMAMenu)
	DMAChannel.setLabel("DMA Channel")
	DMAChannel.setDefaultValue(0)
	DMAChannel.setMin(0)
	DMAChannel.setMax(23)
	DMAChannel.setDependencies(onDMAChannelSet, ["DMAChannel"])

	OldDMAChannel = comp.createIntegerSymbol("OldDMAChannel", DMAMenu)
	OldDMAChannel.setLabel("Old DMA Channel")
	OldDMAChannel.setVisible(False)
	
	DMAChannelSelected = comp.createBooleanSymbol("DMAChannelSelected", DMAMenu)
	DMAChannelSelected.setDefaultValue(False)
	DMAChannelSelected.setVisible(False)
	
	# IntPriority = comp.createIntegerSymbol("IntPriority", DMAMenu)
	# IntPriority.setLabel("Interrupt Priority Level")
	# IntPriority.setMin(0)
	# IntPriority.setMax(7)
	
	### Start of Backlight config options
	BacklightSettings = comp.createMenuSymbol("BacklightSettings", None)
	BacklightSettings.setLabel("Backlight Settings")
	
	DefaultBrightness = comp.createIntegerSymbol("DefaultBrightness", BacklightSettings)
	DefaultBrightness.setLabel("Default Brightness (%)")
	DefaultBrightness.setDescription("The default brightness setting at driver startup")
	DefaultBrightness.setMin(0)
	DefaultBrightness.setMax(100)
	DefaultBrightness.setDefaultValue(100)

	PeripheralControl = comp.createComboSymbol("PeripheralControl", BacklightSettings, ["GPIO", "TC"])
	PeripheralControl.setLabel("Peripheral")
	PeripheralControl.setDescription("Peripheral used to control the backlight PWM")
	PeripheralControl.setDefaultValue("GPIO")
	PeripheralControl.setDependencies(onBacklightPeripheralSelected, ["PeripheralControl"])
	
	TCPeripheralSettings = comp.createMenuSymbol("TCPeripheralSettings", PeripheralControl)
	TCPeripheralSettings.setLabel("Timer Counter Settings")
	TCPeripheralSettings.setDescription("Settings for using the TC peripheral library")
	TCPeripheralSettings.setVisible(False)
	
	TCInstance = comp.createIntegerSymbol("TCInstance", TCPeripheralSettings)
	TCInstance.setLabel("TC Instance")
	TCInstance.setDescription("The TC peripheral IDx")
	TCInstance.setMin(0)
	TCInstance.setMax(64)
	TCInstance.setDefaultValue(0)

	TCChannel = comp.createIntegerSymbol("TCChannel", TCPeripheralSettings)
	TCChannel.setLabel("TC Channel")
	TCChannel.setDescription("The TC channel that controls the PWM signal")
	TCChannel.setMin(0)
	TCChannel.setMax(64)
	TCChannel.setDefaultValue(0)

	TCChannelCompare = comp.createComboSymbol("TCChannelCompare", TCPeripheralSettings, ["A", "B"])
	TCChannelCompare.setLabel("Compare Register")
	TCChannelCompare.setDescription("Compare Register for PWM")
	TCChannelCompare.setDefaultValue("A")
	### End of Backlight config options

	# generated code files
	GFX_LCC_C = comp.createFileSymbol("GFX_LCC_C", None)
	GFX_LCC_C.setDestPath("gfx/driver/controller/lcc/")
	GFX_LCC_C.setOutputName("drv_gfx_lcc.c")
	GFX_LCC_C.setProjectPath(projectPath)
	GFX_LCC_C.setType("SOURCE")
	GFX_LCC_C.setMarkup(True)
	
	GFX_LCC_H = comp.createFileSymbol("GFX_LCC_H", None)
	GFX_LCC_H.setDestPath("gfx/driver/controller/lcc/")
	GFX_LCC_H.setOutputName("drv_gfx_lcc.h")
	GFX_LCC_H.setProjectPath(projectPath)
	GFX_LCC_H.setType("HEADER")
	GFX_LCC_H.setMarkup(True)

	EBIChipSelectIndex = comp.createIntegerSymbol("EBIChipSelectIndex", None)
	EBIChipSelectIndex.setLabel("EBI Chip Select Index")
	EBIChipSelectIndex.setDescription("The chip select index")
	EBIChipSelectIndex.setMin(0)
	EBIChipSelectIndex.setMax(4)
	EBIChipSelectIndex.setDefaultValue(0)
	EBIChipSelectIndex.setVisible(False)

	GFX_LCC_C.setSourcePath("templates/drv_gfx_lcc_generic.c.ftl")
	GFX_LCC_H.setSourcePath("templates/drv_gfx_lcc_generic.h.ftl")

	autoSelectDMAChannel(DMAChannelSelected, DMAChannel, OldDMAChannel)

def autoSelectDMAChannel(DMAChannelSelected, DMAChannel, OldDMAChannel):
	if DMAChannelSelected.getValue() == False:
		for channel in range(0, 23):
			enabled = Database.getComponentByID("core").getSymbolByID("XDMAC_CH" + str(channel) + "_ENABLE").getValue();
			if enabled == False:
				configureDMAChannel(channel)
				DMAChannelSelected.setValue(True, 1)
				DMAChannel.setValue(channel, 1)
				OldDMAChannel.setValue(channel, 1)
				break

def configureDMAChannel(channel):
	Database.getComponentByID("core").getSymbolByID("XDMAC_CH" + str(channel) + "_ENABLE").setValue(True, 1)
	Database.getComponentByID("core").getSymbolByID("XDMAC_CC" + str(channel) + "_DAM").setSelectedKey("FIXED_AM", 1)
	Database.getComponentByID("core").getSymbolByID("XDMAC_CC" + str(channel) + "_DWIDTH").setSelectedKey("HALFWORD", 1)
	Database.getComponentByID("core").getSymbolByID("XDMAC_CC" + str(channel) + "_SIF").setSelectedKey("AHB_IF0", 1)
	Database.getComponentByID("core").getSymbolByID("XDMAC_CC" + str(channel) + "_MBSIZE").setSelectedKey("SIXTEEN", 1)

def unconfigureDMAChannel(channel):
	Database.clearSymbolValue("core", "XDMAC_CH" + str(channel) + "_ENABLE")
	Database.clearSymbolValue("core", "XDMAC_CC" + str(channel) + "_DAM")
	Database.clearSymbolValue("core", "XDMAC_CC" + str(channel) + "_DWIDTH")
	Database.clearSymbolValue("core", "XDMAC_CC" + str(channel) + "_SIF")
	Database.clearSymbolValue("core", "XDMAC_CC" + str(channel) + "_MBSIZE")
	
def onHALConnected(halConnected, event):
	halConnected.getComponent().getSymbolByID("HALComment").setVisible(event["value"] == True)
	halConnected.getComponent().getSymbolByID("DisplayWidth").setVisible(event["value"] == False)
	halConnected.getComponent().getSymbolByID("DisplayHeight").setVisible(event["value"] == False)
	halConnected.getComponent().getSymbolByID("DoubleBuffer").setVisible(event["value"] == False)
	halConnected.getComponent().getSymbolByID("PaletteMode").setVisible(event["value"] == False)
	halConnected.getComponent().getSymbolByID("LCCRefresh").setVisible(event["value"] == False)
	halConnected.getComponent().getSymbolByID("DisplaySettingsMenu").setVisible(event["value"] == False)
	
def onDMAChannelSet(dmaChannelSet, event):
	newDMAChannel = dmaChannelSet.getComponent().getSymbolByID("DMAChannel").getValue()
	oldDMAChannel = dmaChannelSet.getComponent().getSymbolByID("OldDMAChannel").getValue()
	unconfigureDMAChannel(str(oldDMAChannel))
	configureDMAChannel(str(newDMAChannel))
	dmaChannelSet.getComponent().getSymbolByID("OldDMAChannel").setValue(newDMAChannel, 1)

def configureSMCComponent(lccComponent, smcComponent, smcChipSelNum):
	print("LCC: Connecting SMC_CS" + str(smcChipSelNum))
	smcComponent.setSymbolValue("SMC_CHIP_SELECT" + str(smcChipSelNum), True, 1)
	smcComponent.setSymbolValue("SMC_MEM_SCRAMBLING_CS" + str(smcChipSelNum), False, 1)
	smcComponent.setSymbolValue("SMC_NWE_SETUP_CS" + str(smcChipSelNum), 5, 1)
	smcComponent.setSymbolValue("SMC_NCS_WR_SETUP_CS" + str(smcChipSelNum), 0, 1)
	smcComponent.setSymbolValue("SMC_NWE_PULSE_CS" + str(smcChipSelNum), 2, 1)
	smcComponent.setSymbolValue("SMC_NWE_CYCLE_CS" + str(smcChipSelNum), 6, 1)
	smcComponent.setSymbolValue("SMC_NCS_WR_PULSE_CS" + str(smcChipSelNum), 6, 1)
	smcComponent.setSymbolValue("SMC_DATA_BUS_CS" + str(smcChipSelNum), 1, 1)
	smcComponent.setSymbolValue("SMC_WRITE_ENABLE_MODE_CS" + str(smcChipSelNum), False, 1)
	lccComponent.setSymbolValue("EBIChipSelectIndex", smcChipSelNum, 1)
	
def resetSMCComponent(lccComponent, smcComponent, smcChipSelNum):
	print("LCC: Disconnecting SMC_CS" + str(smcChipSelNum))
	smcComponent.clearSymbolValue("SMC_CHIP_SELECT" + str(smcChipSelNum))
	smcComponent.clearSymbolValue("SMC_MEM_SCRAMBLING_CS" + str(smcChipSelNum))
	smcComponent.clearSymbolValue("SMC_NWE_SETUP_CS" + str(smcChipSelNum))
	smcComponent.clearSymbolValue("SMC_NCS_WR_SETUP_CS" + str(smcChipSelNum))
	smcComponent.clearSymbolValue("SMC_NWE_PULSE_CS" + str(smcChipSelNum))
	smcComponent.clearSymbolValue("SMC_NWE_CYCLE_CS" + str(smcChipSelNum))
	smcComponent.clearSymbolValue("SMC_NCS_WR_PULSE_CS" + str(smcChipSelNum))
	smcComponent.clearSymbolValue("SMC_DATA_BUS_CS" + str(smcChipSelNum))
	smcComponent.clearSymbolValue("SMC_WRITE_ENABLE_MODE_CS" + str(smcChipSelNum))
	lccComponent.clearSymbolValue("EBIChipSelectIndex")

def onAttachmentConnected(source, target):
	print("dependency Connected = " + str(target['id']))
	#### test for SMC dependency
	if (source["id"] == "SMC_CS"):
		sub = re.search('smc_cs(.*)', str(target["id"]))
		if (sub and sub.group(1)):
			configureSMCComponent(source["component"], target["component"], int(sub.group(1)))
	#### test for TC dependency (backlight)
	elif (source["id"] == "TMR"):
		sub = re.search('TC(.*)', target["component"].getDisplayName())
		if (sub and sub.group(1)):
			source["component"].getSymbolByID("TCInstance").setValue(int(sub.group(1)), 1)
	
	
def onAttachmentDisconnected(source, target):
	if (source["id"] == "SMC_CS"):
		sub = re.search('smc_cs(.*)', str(target["id"]))
		if (sub and sub.group(1)):
			resetSMCComponent(source["component"], target["component"], int(sub.group(1)))

def OnCacheEnabled(cacheEnabled, event):
	print("LCC: cache enabled")
	cacheEnabled.getComponent().setSymbolValue("UseCachedFrameBuffer", event["value"] == True, 1)
	print("LCC: UseCachedFrameBuffer enabled")

def onBacklightPeripheralSelected(symbol, event):
	print("onBacklightPeripheralSelected = " + event["value"])
	if (event["value"] == "TC"):
		symbol.getComponent().setDependencyEnabled("TMR", True)
		symbol.getComponent().getSymbolByID("TCPeripheralSettings").setVisible(True)
	else:
		symbol.getComponent().getSymbolByID("TCPeripheralSettings").setVisible(False)
		symbol.getComponent().setDependencyEnabled("TMR", False)
