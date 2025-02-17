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

#ifndef GFX_CONFIG_H
#define GFX_CONFIG_H

#ifndef LIB_EXPORT
#define LIB_EXPORT
#endif

#define GFX_MAX_BUFFER_COUNT    2
#define GFX_DRIVER_COUNT        1
#define GFX_DISPLAY_COUNT       1
#define GFX_PROCESSOR_COUNT     1

/* configuration flags */
#define GFX_DRAW_PIPELINE_ENABLED     1
#define GFX_ALPHA_BLENDING_ENABLED    1
#define GFX_BOUNDS_CLIPPING_ENABLED   1
#define GFX_COLOR_CONVERSION_ENABLED  1
#define GFX_COLOR_MASKING_ENABLED     1
#define GFX_LAYER_CLIPPING_ENABLED    1
#define GFX_ORIENTATION_ENABLED       1

#define GFX_DRAW_ARC_ENABLED           1
#define GFX_DRAW_ELLIPSE_ENABLED       1


#endif /* GFX_CONFIG_H */