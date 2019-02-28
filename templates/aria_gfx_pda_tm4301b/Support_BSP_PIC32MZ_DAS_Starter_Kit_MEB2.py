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

############ GLCD + TOUCH I2C CONFIG ######################################################
skActivateList = ["gfx_driver_glcd", "i2c1", "drv_i2c", "drv_i2c0", "core_timer", "sys_time"]
skAutoConnectList = [["gfx_hal", "gfx_display_driver", "gfx_driver_glcd", "gfx_driver_glcd"],
					["drv_i2c_0", "drv_i2c_I2C_dependency", "i2c1", "I2C1_I2C"],
					["gfx_maxtouch_controller", "i2c", "drv_i2c_0", "drv_i2c"],
					["sys_time", "sys_time_TMR_dependency", "core_timer", "CORE_TIMER_TMR"]]
skPinConfig = [{"pin": 16, "name": "CAMERA_ENABLE", "type": "GPIO", "direction": "Out", "latch": "", "abcd": "B"}, #RE4, B3
				{"pin": 22, "name": "BSP_MAXTOUCH_CHG", "type": "GPIO", "direction": "In", "latch": "", "abcd": "B"}, #RB1, B9
				{"pin": 60, "name": "GD20", "type": "GD20", "direction": "", "latch": "", "abcd": ""}, #RJ3, E8
				{"pin": 73, "name": "GD18", "type": "GD18", "direction": "", "latch": "", "abcd": ""}, #RJ10, F8
				{"pin": 74, "name": "GD9", "type": "GD9", "direction": "", "latch": "", "abcd": ""}, #RJ12, F9
				{"pin": 77, "name": "HSYNC", "type": "HSYNC", "direction": "", "latch": "", "abcd": ""}, #RJ5, F12
				{"pin": 78, "name": "VSYNC", "type": "VSYNC", "direction": "", "latch": "", "abcd": ""}, #RJ4, F13
				{"pin": 80, "name": "GD10", "type": "GD10", "direction": "", "latch": "", "abcd": ""}, #RD2, G2
				{"pin": 81, "name": "GD11", "type": "GD11", "direction": "", "latch": "", "abcd": ""}, #RD3, G3
				{"pin": 88, "name": "GD8", "type": "GD8", "direction": "", "latch": "", "abcd": ""}, #RJ14, G10
				{"pin": 89, "name": "GCLK", "type": "GCLK", "direction": "", "latch": "", "abcd": ""}, #RJ6, G11
				{"pin": 90, "name": "GD0", "type": "GD0", "direction": "", "latch": "", "abcd": ""}, #RJ13, G12
				{"pin": 91, "name": "GEN", "type": "GEN", "direction": "", "latch": "", "abcd": ""}, #RJ7, G13
				{"pin": 92, "name": "GD2", "type": "GD2", "direction": "", "latch": "", "abcd": ""}, #RD9, H1
				{"pin": 101, "name": "GD13", "type": "GD13", "direction": "", "latch": "", "abcd": ""}, #RK4, H10
				{"pin": 105, "name": "GD7", "type": "GD7", "direction": "", "latch": "", "abcd": ""}, #RD12, J1
				{"pin": 106, "name": "GD22", "type": "GD22", "direction": "", "latch": "", "abcd": ""}, #RD13, J2
				{"pin": 114, "name": "GD14", "type": "GD14", "direction": "", "latch": "", "abcd": ""}, #RK5, J10
				{"pin": 119, "name": "GD16", "type": "GD16", "direction": "", "latch": "", "abcd": ""}, #RF5, K2
				{"pin": 120, "name": "GD5", "type": "GD5", "direction": "", "latch": "", "abcd": ""}, #RF1, K3
				{"pin": 129, "name": "GD23", "type": "GD23", "direction": "", "latch": "", "abcd": ""}, #RK0, K12
				{"pin": 131, "name": "GD6", "type": "GD6", "direction": "", "latch": "", "abcd": ""}, #RF0, L1
				{"pin": 132, "name": "GD21", "type": "GD21", "direction": "", "latch": "", "abcd": ""}, #RH15, L2
				{"pin": 133, "name": "GD17", "type": "GD17", "direction": "", "latch": "", "abcd": ""}, #RF4, L3
				{"pin": 141, "name": "GD1", "type": "GD1", "direction": "", "latch": "", "abcd": ""}, #RA4, L11
				{"pin": 143, "name": "GD12", "type": "GD12", "direction": "", "latch": "", "abcd": ""}, #RK3, L13
				{"pin": 145, "name": "GD4", "type": "GD4", "direction": "", "latch": "", "abcd": ""}, #RG1, M2
				{"pin": 146, "name": "TM4301B_BACKLIGHT", "type": "GPIO", "direction": "Out", "latch": "High", "abcd": ""}, #RE3, M3
				{"pin": 155, "name": "GD19", "type": "GD19", "direction": "", "latch": "", "abcd": ""}, #RK7, M12
				{"pin": 156, "name": "GD15", "type": "GD15", "direction": "", "latch": "", "abcd": ""}, #RK6, M13
				{"pin": 158, "name": "GD3", "type": "GD3", "direction": "", "latch": "", "abcd": ""}, #RG0, N2
				{"pin": 154, "name": "SCL1", "type": "SCL1", "direction": "", "latch": "", "abcd": ""}, #RA14, M11
				{"pin": 167, "name": "SDA1", "type": "SDA1", "direction": "", "latch": "", "abcd": ""}] #RA15, N11
##################################################################################

def eventHandler(event):
	if (event == "configure"):
		try:
			#### FIXME: single layer only, since DDR is not yet working
			Database.setSymbolValue("gfx_driver_glcd", "FrameBufferMemoryMode", 0, 1)
			Database.setSymbolValue("gfx_driver_glcd", "PixelClockDivider", 6, 1)
			Database.setSymbolValue("gfx_hal", "ColorModeHint", "GFX_COLOR_MODE_RGBA_8888", 1)
		except:
			return

bspDisplayInterfaceList = ["GLCD"]

pic32mz_das_sk_meb2 = bspSupportObj(skPinConfig, skActivateList, None, skAutoConnectList, eventHandler)

addBSPSupport("BSP_PIC32MZ_DA_Starter_Kit", "GLCD", pic32mz_das_sk_meb2)
addDisplayIntfSupport("BSP_PIC32MZ_DA_Starter_Kit", bspDisplayInterfaceList)