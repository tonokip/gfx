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

useRTOS = component.createBooleanSymbol("USE_RTOS", None)
useRTOS.setLabel("Enable RTOS Mode?")
useRTOS.setDependencies(onRTOSEnable, ["USE_RTOS"])
useRTOS.setVisible(False) #Hide unsupported RTOS options

#rtosMenu = component.createMenuSymbol("RTOS_MENU", None)
#rtosMenu.setLabel("RTOS Configuration")
#

useRTOSExtensions = component.createBooleanSymbol("useRTOSExtensions", useRTOS)
useRTOSExtensions.setLabel("Use RTOS Extensions?")
useRTOSExtensions.setVisible(False)

rtosFullBlockingMode = component.createBooleanSymbol("rtosFullBlockingMode", useRTOS)
rtosFullBlockingMode.setLabel("Full Blocking?")
rtosFullBlockingMode.setDefaultValue(True)
rtosFullBlockingMode.setVisible(False)

rtosTaskSize = component.createIntegerSymbol("rtosTaskSize", useRTOS)
rtosTaskSize.setLabel("Task Size")
rtosTaskSize.setDefaultValue(1024)
rtosTaskSize.setVisible(False)

rtosTaskPriority = component.createIntegerSymbol("rtosTaskPriority", useRTOS)
rtosTaskPriority.setLabel("Task Priority")
rtosTaskPriority.setDefaultValue(1)
rtosTaskPriority.setVisible(False)

rtosEnableTaskDelay = component.createBooleanSymbol("rtosEnableTaskDelay", useRTOS)
rtosEnableTaskDelay.setLabel("Use Task Delay?")
rtosEnableTaskDelay.setDefaultValue(True)
rtosEnableTaskDelay.setVisible(False)

rtosTaskDelay = component.createIntegerSymbol("rtosTaskDelay", useRTOS)
rtosTaskDelay.setLabel("Task Delay")
rtosTaskDelay.setDefaultValue(1000)
rtosTaskDelay.setVisible(False)

LIBARIA_RTOS_H = component.createFileSymbol("LIBARIA_RTOS_H", None)
LIBARIA_RTOS_H.setSourcePath("inc/libaria_rtos.h")
LIBARIA_RTOS_H.setDestPath("gfx/libaria/")
LIBARIA_RTOS_H.setOutputName("libaria_rtos.h")
LIBARIA_RTOS_H.setProjectPath(projectPath)
LIBARIA_RTOS_H.setType("HEADER")
LIBARIA_RTOS_H.setEnabled(False)

LIBARIA_EVENT_RTOS_H = component.createFileSymbol("LIBARIA_EVENT_RTOS_H", None)
LIBARIA_EVENT_RTOS_H.setSourcePath("inc/libaria_event_rtos.h")
LIBARIA_EVENT_RTOS_H.setDestPath("gfx/libaria/inc/")
LIBARIA_EVENT_RTOS_H.setProjectPath(projectPath)
LIBARIA_EVENT_RTOS_H.setType("HEADER")
LIBARIA_EVENT_RTOS_H.setEnabled(False)

LIBARIA_INPUT_RTOS_H = component.createFileSymbol("LIBARIA_INPUT_RTOS_H", None)
LIBARIA_INPUT_RTOS_H.setSourcePath("inc/libaria_input_rtos.h")
LIBARIA_INPUT_RTOS_H.setDestPath("gfx/libaria/inc/")
LIBARIA_INPUT_RTOS_H.setProjectPath(projectPath)
LIBARIA_INPUT_RTOS_H.setType("HEADER")
LIBARIA_INPUT_RTOS_H.setEnabled(False)

LIBARIA_CONTEXT_RTOS_H = component.createFileSymbol("LIBARIA_CONTEXT_RTOS_H", None)
LIBARIA_CONTEXT_RTOS_H.setSourcePath("inc/libaria_context_rtos.h")
LIBARIA_CONTEXT_RTOS_H.setDestPath("gfx/libaria/inc/")
LIBARIA_CONTEXT_RTOS_H.setProjectPath(projectPath)
LIBARIA_CONTEXT_RTOS_H.setType("HEADER")
LIBARIA_CONTEXT_RTOS_H.setEnabled(False)