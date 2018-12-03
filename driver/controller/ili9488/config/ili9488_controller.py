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
	execfile(Module.getPath() + "/config/ili9488_config.py")
	execfile(Module.getPath() + "/config/ili9488_files.py")

def onHALConnected(halConnected, event):
	halConnected.getComponent().getSymbolByID("HALComment").setVisible(event["value"] == True)
	halConnected.getComponent().getSymbolByID("DisplayWidth").setVisible(event["value"] == False)
	halConnected.getComponent().getSymbolByID("DisplayHeight").setVisible(event["value"] == False)
	halConnected.getComponent().getSymbolByID("PaletteMode").setVisible(event["value"] == False)

def configureSMCComponent(comp, smcComponent):
	print("Configuring SMC")
	smcChipSelNum = comp.getSymbolValue("EBIChipSelectIndex")
	smcComponent.setSymbolValue("SMC_CHIP_SELECT" + str(smcChipSelNum), True, 1)
	smcComponent.setSymbolValue("SMC_MEM_SCRAMBLING_CS" + str(smcChipSelNum), False, 1)
	# SMC Write Timings
	smcComponent.setSymbolValue("SMC_NWE_SETUP_CS" + str(smcChipSelNum), 2, 1)
	smcComponent.setSymbolValue("SMC_NCS_WR_SETUP_CS" + str(smcChipSelNum), 0, 1)
	smcComponent.setSymbolValue("SMC_NWE_PULSE_CS" + str(smcChipSelNum), 4, 1)
	smcComponent.setSymbolValue("SMC_NCS_WR_PULSE_CS" + str(smcChipSelNum), 10, 1)
	smcComponent.setSymbolValue("SMC_DATA_BUS_CS" + str(smcChipSelNum), 1, 1)
	smcComponent.setSymbolValue("SMC_NWE_CYCLE_CS" + str(smcChipSelNum), 3, 1)
	# SMC Read Timings
	smcComponent.setSymbolValue("SMC_NRD_SETUP_CS" + str(smcChipSelNum), 2, 1)
	smcComponent.setSymbolValue("SMC_NCS_RD_SETUP_CS" + str(smcChipSelNum), 0, 1)
	smcComponent.setSymbolValue("SMC_NRD_PULSE_CS" + str(smcChipSelNum), 63, 1)
	smcComponent.setSymbolValue("SMC_NCS_RD_PULSE_CS" + str(smcChipSelNum), 63, 1)
	smcComponent.setSymbolValue("SMC_NRD_CYCLE_CS" + str(smcChipSelNum), 110, 1)
	# SMC Mode Configuration
	smcComponent.setSymbolValue("SMC_DATA_BUS_CS" + str(smcChipSelNum), 1, 1)
	smcComponent.setSymbolValue("SMC_BAT_CS" + str(smcChipSelNum), 0, 1)
	smcComponent.setSymbolValue("SMC_READ_ENABLE_MODE_CS" + str(smcChipSelNum), True, 1)
	smcComponent.setSymbolValue("SMC_WRITE_ENABLE_MODE_CS" + str(smcChipSelNum), True, 1)
	
def configureSPIComponent(comp, spiComponent):
	print("Configuring SPI")
	# TODO: Add SPI configuration here

def onAttachmentConnected(source, target):
	#print(source["component"].getID() + ": " + dependencyID + " dependent component added ")
	
	if source["id"] == "SMC_CS":
		#Disable the SPI symbols
		source["component"].setDependencyEnabled("DRV_SPI", False)
		source["component"].getSymbolByID("GFX_ILI9488_SPI").setEnabled(False)
		source["component"].getSymbolByID("GFX_ILI9488_INTF_SPI").setEnabled(False)
		
		#Enable the SMC symbols
		source["component"].getSymbolByID("Interface").setValue("Parallel", 1)
		source["component"].getSymbolByID("ParallelInterfaceWidth").setVisible(True)
		source["component"].getSymbolByID("DCXAddressBit").setVisible(True)
		source["component"].getSymbolByID("UseSyncBarriers").setVisible(True)
		source["component"].getSymbolByID("EBIChipSelectIndex").setVisible(True)
		source["component"].getSymbolByID("GFX_ILI9488_DBIB_C").setEnabled(True)
		source["component"].getSymbolByID("GFX_ILI9488_INTF_SMC").setEnabled(True)
		
		configureSMCComponent(source["component"], target["component"])
		
	if source["id"] == "DRV_SPI":
		spiIndex = target["component"].getSymbolByID("INDEX").getValue()
		#print("Using SPI port " + str(spiIndex))
		
		#Disable the SMC symbols
		source["component"].setDependencyEnabled("SMC_CS", False)
		source["component"].getSymbolByID("GFX_ILI9488_DBIB_C").setEnabled(False)
		source["component"].getSymbolByID("GFX_ILI9488_INTF_SMC").setEnabled(False)
		
		#Enable the SPI symbols
		source["component"].getSymbolByID("Interface").setValue("SPI 4-Line", 1)
		source["component"].getSymbolByID("SPIPortIndex").setValue(spiIndex, 1)
		source["component"].getSymbolByID("GFX_ILI9488_SPI").setEnabled(True)
		source["component"].getSymbolByID("GFX_ILI9488_INTF_SPI").setEnabled(True)
		
		configureSPIComponent(source["component"], target["component"])

def onAttachmentDisconnected(source, target):
	#print(comp.getID() + ": " + dependencyID + " dependent component removed ")
	
	if source["id"] == "gfx_driver_ili9488":
		return
	
	source["component"].setDependencyEnabled("DRV_SPI", True)
	source["component"].setDependencyEnabled("SMC_CS", True)
	
	#Disable the SMC and SPI symbols
	source["component"].getSymbolByID("ParallelInterfaceWidth").setVisible(False)
	source["component"].getSymbolByID("DCXAddressBit").setVisible(False)
	source["component"].getSymbolByID("UseSyncBarriers").setVisible(False)
	source["component"].getSymbolByID("EBIChipSelectIndex").setVisible(False)
	source["component"].getSymbolByID("GFX_ILI9488_SPI").setEnabled(False)
	source["component"].getSymbolByID("GFX_ILI9488_DBIB_C").setEnabled(False)
	source["component"].getSymbolByID("GFX_ILI9488_INTF_SPI").setEnabled(False)

def onInterfaceSetSPI(symbol, event):
	if event["value"] == "SPI 4-Line":
		symbol.setVisible(True)
	else:
		symbol.setVisible(False)

def onInterfaceSetParallel(symbol, event):
	if event["value"] == "16-bit" or event["value"] == "8-bit":
		symbol.setVisible(True)
	else:
		symbol.setVisible(False)
