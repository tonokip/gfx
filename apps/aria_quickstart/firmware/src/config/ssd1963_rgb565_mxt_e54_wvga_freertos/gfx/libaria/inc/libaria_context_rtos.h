/*******************************************************************************
 Module for Microchip Graphics Library - Aria User Interface Library

  Company:
    Microchip Technology Inc.

  File Name:
    libaria_context_rtos.h

  Summary:
    RTOS extensions for libaria_context.h/c
    
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

#ifndef LIBARIA_CONTEXT_RTOS_H
#define LIBARIA_CONTEXT_RTOS_H

#ifdef __cplusplus
    extern "C" {
#endif

laResult laContext_Create_RTOS(laContext* context);
laResult laContext_Destroy_RTOS(laContext* context);
laResult laContext_RefreshActiveScreen_Ext_RTOS();
laResult laContext_SetActiveScreen_RTOS(uint32_t idx);
laResult laContext_SendSetActiveScreenEvent_Ext_RTOS(uint32_t idx);
void laContext_Update_RTOS(laBool fullBlock, uint32_t dt);


#ifdef __cplusplus
    }
#endif

#endif