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

spi4PinComponentIDList = ["spi0", "drv_spi", "drv_spi_0", "gfx_intf_spi4"]
spi4PinAutoConnectList = [["drv_spi_0", "drv_spi_SPI_dependency", "spi0", "SPI0_SPI"],
							["gfx_intf_spi4", "DRV_SPI", "drv_spi_0", "drv_spi"],
							["gfx_driver_ili9488", "Display Interface", "gfx_intf_spi4", "gfx_intf_spi4"]]
spi4PinConfigs = [{"pin": 31, "name": "GFX_DISP_INTF_PIN_RSDC", "type": "GPIO", "direction": "Out", "latch": "High", "abcd": ""}, #PB3
				{"pin": 52, "name": "GFX_DISP_INTF_PIN_CS", "type": "GPIO", "direction": "Out", "latch": "High", "abcd": ""}, #PD25
				{"pin": 60, "name": "SPI0_SPCK", "type": "SPI0_SPCK", "direction": "", "latch": "", "abcd": "B"}, #PD22
				{"pin": 63, "name": "SPI0_MOSI", "type": "SPI0_MOSI", "direction": "", "latch": "", "abcd": "B"}, #PD21
				{"pin": 65, "name": "SPI0_MISO", "type": "SPI0_MISO", "direction": "", "latch": "", "abcd": "B"}, #PD20
				{"pin": 102, "name": "GFX_DISP_INTF_PIN_BACKLIGHT", "type": "GPIO", "direction": "Out", "latch": "High", "abcd": ""}, #PA0
				{"pin": 103, "name": "GFX_DISP_INTF_PIN_RESET", "type": "GPIO", "direction": "Out", "latch": "High", "abcd": ""}] #PC17

parallelComponentIDList = ["smc", "gfx_intf_parallel_smc"]
parallelAutoConnectList = [["gfx_intf_parallel_smc", "smc", "smc", "smc_cs0"],
							["gfx_driver_ili9488", "Display Interface", "gfx_intf_parallel_smc", "gfx_intf_parallel_smc"]]
ParallelPinConfigs = [{"pin": 4, "name": "EBI_D8", "type": "EBI_D8", "direction": "", "latch": "", "abcd": "A"}, #PE0
					{"pin": 6, "name": "EBI_D9", "type": "EBI_D9", "direction": "", "latch": "", "abcd": "A"}, #PE1
					{"pin": 7, "name": "EBI_D10", "type": "EBI_D10", "direction": "", "latch": "", "abcd": "A"}, #PE2
					{"pin": 10, "name": "EBI_D11", "type": "EBI_D11", "direction": "", "latch": "", "abcd": "A"}, #PE3
					{"pin": 11, "name": "EBI_D0", "type": "EBI_D0", "direction": "", "latch": "", "abcd": "A"}, #PC0
					{"pin": 15, "name": "EBI_A12", "type": "EBI_A12", "direction": "", "latch": "", "abcd": "A"}, #PC30
					{"pin": 19, "name": "GFX_DISP_INTF_PIN_RESET", "type": "GPIO", "direction": "Out", "latch": "High", "abcd": ""}, #PC13
					{"pin": 27, "name": "EBI_D12", "type": "EBI_D12", "direction": "", "latch": "", "abcd": "A"}, #PE4
					{"pin": 28, "name": "EBI_D13", "type": "EBI_D13", "direction": "", "latch": "", "abcd": "A"}, #PE5
					{"pin": 38, "name": "EBI_D1", "type": "EBI_D1", "direction": "", "latch": "", "abcd": "A"}, #PC1
					{"pin": 39, "name": "EBI_D2", "type": "EBI_D2", "direction": "", "latch": "", "abcd": "A"}, #PC2
					{"pin": 40, "name": "EBI_D3", "type": "EBI_D3", "direction": "", "latch": "", "abcd": "A"}, #PC3
					{"pin": 41, "name": "EBI_D4", "type": "EBI_D4", "direction": "", "latch": "", "abcd": "A"}, #PC4S
					{"pin": 45, "name": "EBI_D15", "type": "EBI_D15", "direction": "", "latch": "", "abcd": "A"}, #PA16
					{"pin": 48, "name": "EBI_D7", "type": "EBI_D7", "direction": "", "latch": "", "abcd": "A"}, #PC7
					{"pin": 49, "name": "EBI_D14", "type": "EBI_D14", "direction": "", "latch": "", "abcd": "A"}, #PA15
					{"pin": 54, "name": "EBI_D6", "type": "EBI_D6", "direction": "", "latch": "", "abcd": "A"}, #PC6
					{"pin": 58, "name": "EBI_D5", "type": "EBI_D5", "direction": "", "latch": "", "abcd": "A"}, #PC5
					{"pin": 67, "name": "GFX_DISP_INTF_PIN_CS", "type": "GPIO", "direction": "Out", "latch": "High", "abcd": ""}, #PD19
					{"pin": 82, "name": "EBI_NWR0/NWE", "type": "EBI_NWR0/NWE", "direction": "", "latch": "", "abcd": "A"}, #PC8
					{"pin": 86, "name": "GFX_DISP_INTF_PIN_BACKLIGHT", "type": "GPIO", "direction": "Out", "latch": "High", "abcd": ""}, #PC9
					{"pin": 94, "name": "EBI_NRD", "type": "EBI_NRD", "direction": "", "latch": "", "abcd": "A"}] #PC11

def eventHandlerSPI4line(event):
	if (event == "configure"):
		#set the SPI clock to 20MHz
		try:
			Database.setSymbolValue("spi0", "SPI_BAUD_RATE", 20000000, 1)
		except:
			print("Unable to configure SPI baud rate.")

sam_e70_xplained_ultra_SPI = bspSupportObj(spi4PinConfigs, spi4PinComponentIDList, None, spi4PinAutoConnectList, eventHandlerSPI4line)
sam_e70_xplained_ultra_Parallel = bspSupportObj(ParallelPinConfigs, parallelComponentIDList, None, parallelAutoConnectList, None)



addBSPSupport("BSP_SAM_E70_Xplained_Ultra", "SPI 4-line", sam_e70_xplained_ultra_SPI)
addBSPSupport("BSP_SAM_E70_Xplained_Ultra", "Parallel", sam_e70_xplained_ultra_Parallel)