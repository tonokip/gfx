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

spi4PinComponentIDList = ["spi0", "drv_spi", "drv_spi_0"]
spi4PinAutoConnectList = [["drv_spi_0", "drv_spi_SPI_dependency", "spi0", "SPI0_SPI"],
							["gfx_driver_ili9488", "DRV_SPI", "drv_spi_0", "drv_spi"]]
spi4PinConfigs = [{"pin": 31, "name": "GFX_DISP_INTF_PIN_RSDC", "type": "GPIO", "direction": "Out", "latch": "High"},
				{"pin": 52, "name": "GFX_DISP_INTF_PIN_CS", "type": "GPIO", "direction": "Out", "latch": "High"},
				{"pin": 60, "name": "SPI0_SPCK", "type": "SPI0_SPCK", "direction": "", "latch": ""},
				{"pin": 63, "name": "SPI0_MOSI", "type": "SPI0_MOSI", "direction": "", "latch": ""},
				{"pin": 65, "name": "SPI0_MISO", "type": "SPI0_MISO", "direction": "", "latch": ""},
				{"pin": 102, "name": "GFX_DISP_INTF_PIN_BACKLIGHT", "type": "GPIO", "direction": "Out", "latch": "High"},
				{"pin": 103, "name": "GFX_DISP_INTF_PIN_RESET", "type": "GPIO", "direction": "Out", "latch": "High"}]

parallelComponentIDList = ["smc"]
parallelAutoConnectList = [["gfx_driver_ili9488", "SMC_CS", "smc", "smc_cs0"]]
ParallelPinConfigs = [{"pin": 4, "name": "EBI_D8", "type": "EBI_D8", "direction": "", "latch": ""},
					{"pin": 6, "name": "EBI_D9", "type": "EBI_D9", "direction": "", "latch": ""},
					{"pin": 7, "name": "EBI_D10", "type": "EBI_D10", "direction": "", "latch": ""},
					{"pin": 10, "name": "EBI_D11", "type": "EBI_D11", "direction": "", "latch": ""},
					{"pin": 11, "name": "EBI_D0", "type": "EBI_D0", "direction": "", "latch": ""},
					{"pin": 15, "name": "EBI_A12", "type": "EBI_A12", "direction": "", "latch": ""},
					{"pin": 19, "name": "GFX_DISP_INTF_PIN_RESET", "type": "GPIO", "direction": "Out", "latch": "High"},
					{"pin": 27, "name": "EBI_D12", "type": "EBI_D12", "direction": "", "latch": ""},
					{"pin": 28, "name": "EBI_D13", "type": "EBI_D13", "direction": "", "latch": ""},
					{"pin": 38, "name": "EBI_D1", "type": "EBI_D1", "direction": "", "latch": ""},
					{"pin": 39, "name": "EBI_D2", "type": "EBI_D2", "direction": "", "latch": ""},
					{"pin": 40, "name": "EBI_D3", "type": "EBI_D3", "direction": "", "latch": ""},
					{"pin": 41, "name": "EBI_D4", "type": "EBI_D4", "direction": "", "latch": ""},
					{"pin": 45, "name": "EBI_D15", "type": "EBI_D15", "direction": "", "latch": ""},
					{"pin": 48, "name": "EBI_D7", "type": "EBI_D7", "direction": "", "latch": ""},
					{"pin": 49, "name": "EBI_D14", "type": "EBI_D14", "direction": "", "latch": ""},
					{"pin": 54, "name": "EBI_D6", "type": "EBI_D6", "direction": "", "latch": ""},
					{"pin": 58, "name": "EBI_D5", "type": "EBI_D5", "direction": "", "latch": ""},
					{"pin": 67, "name": "GFX_DISP_INTF_PIN_CS", "type": "GPIO", "direction": "Out", "latch": "High"},
					{"pin": 82, "name": "EBI_NWR0/NWE", "type": "EBI_NWR0/NWE", "direction": "", "latch": ""},
					{"pin": 86, "name": "GFX_DISP_INTF_PIN_BACKLIGHT", "type": "GPIO", "direction": "Out", "latch": "High"},
					{"pin": 94, "name": "EBI_NRD", "type": "EBI_NRD", "direction": "", "latch": ""}]

					
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