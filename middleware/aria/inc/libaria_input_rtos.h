/*******************************************************************************
 Module for Microchip Graphics Library - Aria User Interface Library

  Company:
    Microchip Technology Inc.

  File Name:
    libaria_input_rtos.h

  Summary:

    This file contains the RTOS extensions of the libaria_input module.


*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2018 Microchip Technology Inc. and its subsidiaries.
*
* Subject to your compliance with these terms, you may use Microchip software
* and any derivatives exclusively with Microchip products. It is your
* responsibility to comply with third party license terms applicable to your
* use of third party software (including open source software) that may
* accompany Microchip software.
*
* THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
* EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
* WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
* PARTICULAR PURPOSE.
*
* IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
* INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
* WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
* BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
* FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
* ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
* THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
*******************************************************************************/
// DOM-IGNORE-END

#ifndef LIBARIA_INPUT_RTOS_H
#define LIBARIA_INPUT_RTOS_H

// DOM-IGNORE-BEGIN
laResult laInput_SendTouchDown_Ext_RTOS(uint32_t id, int32_t x, int32_t y);
laResult laInput_SendTouchUp_Ext_RTOS(uint32_t id, int32_t x, int32_t y);
laResult laInput_SendTouchMoved_Ext_RTOS(uint32_t id, int32_t x, int32_t y);
// DOM-IGNORE-END

#ifdef __cplusplus
    }
#endif

#endif // LIBARIA_INPUT_RTOS_H