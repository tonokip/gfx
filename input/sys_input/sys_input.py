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

def instantiateComponent(component):
	RTOSMode = component.createBooleanSymbol("RTOSMode", None)
	RTOSMode.setLabel("Use RTOS Mode?")
	RTOSMode.setDescription("Enables RTOS compatibility mode for this service.")
	RTOSMode.setDependencies(onRTOSMode, ["RTOSMode"])
	RTOSMode.setVisible(False) #Hide unsupported RTOS options
	
	RTOSTaskSize = component.createIntegerSymbol("RTOSTaskSize", RTOSMode)
	RTOSTaskSize.setLabel("Task Size")
	RTOSTaskSize.setMin(0)
	RTOSTaskSize.setDefaultValue(1024)
	RTOSTaskSize.setVisible(False)
	
	RTOSTaskPriority = component.createIntegerSymbol("RTOSTaskPriority", RTOSMode)
	RTOSTaskPriority.setLabel("Task Priority")
	RTOSTaskPriority.setDefaultValue(1)
	RTOSTaskPriority.setVisible(False)
	
	RTOSUseDelay = component.createBooleanSymbol("RTOSUseDelay", RTOSMode)
	RTOSUseDelay.setLabel("Use Task Delay?")
	RTOSUseDelay.setDefaultValue(True)
	RTOSUseDelay.setVisible(False)
	
	RTOSTaskDelay = component.createIntegerSymbol("RTOSTaskDelay", RTOSUseDelay)
	RTOSTaskDelay.setLabel("Task Delay")
	RTOSTaskDelay.setDefaultValue(1000)
	RTOSTaskDelay.setMin(0)
	RTOSTaskDelay.setDependencies(onRTOSUseDelay, ["RTOSUseDelay"])

	projectPath = "config/" + Variables.get("__CONFIGURATION_NAME") + "/system/input"
	
	SYS_INPUT_H = component.createFileSymbol("SYS_INPUT_H", None)
	SYS_INPUT_H.setSourcePath("src/sys_input.h")
	SYS_INPUT_H.setDestPath("system/input/")
	SYS_INPUT_H.setProjectPath(projectPath)
	SYS_INPUT_H.setType("HEADER")
	
	SYS_INPUT_GESTURE_H = component.createFileSymbol("SYS_INPUT_GESTURE_H", None)
	SYS_INPUT_GESTURE_H.setSourcePath("src/sys_input_gesture.h")
	SYS_INPUT_GESTURE_H.setDestPath("system/input/")
	SYS_INPUT_GESTURE_H.setProjectPath(projectPath)
	SYS_INPUT_GESTURE_H.setType("HEADER")
	
	SYS_INPUT_KEYBOARD_H = component.createFileSymbol("SYS_INPUT_KEYBOARD_H", None)
	SYS_INPUT_KEYBOARD_H.setSourcePath("src/sys_input_keyboard.h")
	SYS_INPUT_KEYBOARD_H.setDestPath("system/input/")
	SYS_INPUT_KEYBOARD_H.setProjectPath(projectPath)
	SYS_INPUT_KEYBOARD_H.setType("HEADER")
	
	SYS_INPUT_LISTENER_H = component.createFileSymbol("SYS_INPUT_LISTENER_H", None)
	SYS_INPUT_LISTENER_H.setSourcePath("src/sys_input_listener.h")
	SYS_INPUT_LISTENER_H.setDestPath("system/input/")
	SYS_INPUT_LISTENER_H.setProjectPath(projectPath)
	SYS_INPUT_LISTENER_H.setType("HEADER")
	
	SYS_INPUT_MOUSE_H = component.createFileSymbol("SYS_INPUT_MOUSE_H", None)
	SYS_INPUT_MOUSE_H.setSourcePath("src/sys_input_mouse.h")
	SYS_INPUT_MOUSE_H.setDestPath("system/input/")
	SYS_INPUT_MOUSE_H.setProjectPath(projectPath)
	SYS_INPUT_MOUSE_H.setType("HEADER")
	
	SYS_INPUT_TOUCH_H = component.createFileSymbol("SYS_INPUT_TOUCH_H", None)
	SYS_INPUT_TOUCH_H.setSourcePath("src/sys_input_touch.h")
	SYS_INPUT_TOUCH_H.setDestPath("system/input/")
	SYS_INPUT_TOUCH_H.setProjectPath(projectPath)
	SYS_INPUT_TOUCH_H.setType("HEADER")
	
	SYS_INPUT_C = component.createFileSymbol("SYS_INPUT_C", None)
	SYS_INPUT_C.setSourcePath("src/sys_input.c")
	SYS_INPUT_C.setDestPath("system/input/")
	SYS_INPUT_C.setProjectPath(projectPath)
	SYS_INPUT_C.setType("SOURCE")
	
	SYS_INPUT_LISTENER_C = component.createFileSymbol("SYS_INPUT_LISTENER_C", None)
	SYS_INPUT_LISTENER_C.setSourcePath("src/sys_input_listener.c")
	SYS_INPUT_LISTENER_C.setDestPath("system/input/")
	SYS_INPUT_LISTENER_C.setProjectPath(projectPath)
	SYS_INPUT_LISTENER_C.setType("SOURCE")
	
	SysInitIncludeString = component.createListEntrySymbol("SysInitIncludeString", None)
	SysInitIncludeString.addValue('#include "system/input/sys_input.h"')
	SysInitIncludeString.setTarget("core.LIST_SYSTEM_CONFIG_H_GLOBAL_INCLUDES")
	
	SysInitString = component.createListEntrySymbol("SYSInitString", None)
	SysInitString.addValue("SYS_INP_Init();")
	SysInitString.setTarget("core.LIST_SYSTEM_INIT_C_INITIALIZE_MIDDLEWARE")
	
	SysTasksString = component.createListEntrySymbol("SYSTasksString", None)
	SysTasksString.addValue("SYS_INP_Tasks();")
	SysTasksString.setTarget("core.LIST_SYSTEM_TASKS_C_CALL_LIB_TASKS")
	
def onRTOSMode(symbol, event):
	event["source"].getSymbolByID("RTOSTaskSize").setVisible(event["value"])
	event["source"].getSymbolByID("RTOSTaskPriority").setVisible(event["value"])
	event["source"].getSymbolByID("RTOSUseDelay").setVisible(event["value"])
	
def onRTOSUseDelay(symbol, event):
	symbol.setVisible(event["value"] == True)