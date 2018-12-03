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

spi4PinComponentIDList = ["sercom1", "drv_spi", "drv_spi_0"]
spi4PinAutoConnectList = [["drv_spi_0", "drv_spi_SPI_dependency", "sercom1", "SERCOM1_SPI"],
							["gfx_driver_ili9488", "DRV_SPI", "drv_spi_0", "drv_spi"]]
spi4PinConfigs = [{"pin": 70, "name": "GFX_DISP_INTF_PIN_RSDC", "type": "GPIO", "direction": "Out", "latch": "High", "abcd": ""}, #PA20
				{"pin": 53, "name": "GFX_DISP_INTF_PIN_CS", "type": "GPIO", "direction": "Out", "latch": "High", "abcd": ""}, #PA17
				{"pin": 52, "name": "SERCOM1_PAD0", "type": "SERCOM1_PAD0", "direction": "", "latch": "", "abcd": "C"}, #PA16
				{"pin": 54, "name": "SERCOM1_PAD2", "type": "SERCOM1_PAD2", "direction": "", "latch": "", "abcd": "C"}, #PA18
				{"pin": 55, "name": "SERCOM1_PAD3", "type": "SERCOM1_PAD3", "direction": "", "latch": "", "abcd": "C"}, #PA19
				{"pin": 32, "name": "GFX_DISP_INTF_PIN_BACKLIGHT", "type": "GPIO", "direction": "Out", "latch": "High", "abcd": ""}, #PB12
				{"pin": 35, "name": "GFX_DISP_INTF_PIN_RESET", "type": "GPIO", "direction": "Out", "latch": "High", "abcd": ""}] #PB15

def eventHandlerSPI4line(event):
	if (event == "configure"):
		#set the SPI clock to 8MHz
		try:
			Database.setSymbolValue("sercom1", "SPI_BAUD_RATE", 8000000, 1)
		except:
			print("Unable to configure SPI baud rate.")
		
		try:
			Database.setSymbolValue("sercom1", "SPI_DOPO", 1, 1)
		except:
			print("Unable to configure SERCOM1 DOPO Pads.")
		### set heap to 16kB for C21
		Database.setSymbolValue("core", "HEAP_SIZE", 16384, 0)
			
def eventHandlerParallel(event):
	print("Parallel mode is not supported.")

sam_c21n_xplained_pro_SPI = bspSupportObj(spi4PinConfigs, spi4PinComponentIDList, None, spi4PinAutoConnectList, eventHandlerSPI4line)
sam_c21n_xplained_pro_Parallel = bspSupportObj(None, None, None, None, eventHandlerParallel)

addBSPSupport("BSP_SAM_C21N_Xplained_Pro", "SPI 4-line", sam_c21n_xplained_pro_SPI)
addBSPSupport("BSP_SAM_C21N_Xplained_Pro", "Parallel", sam_c21n_xplained_pro_Parallel)
