/*******************************************************************************
 Module for Microchip Graphics Library - Graphics Driver Layer

  Company:
    Microchip Technology Inc.

  File Name:
    drv_2dgpu.h

  Summary:
    Main header file for MPLAB Harmony Graphics Driver 2DGPU functions

  Description:
    The API functions to be used for the 2DGPU graphics accelerator.

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2019 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.
IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR
OTHER LEGAL EQUITABLE THEORY ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES
INCLUDING BUT NOT LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR
CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF
SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS.
*******************************************************************************/

/****************************************************************************
*
*    Copyright (c) 2005 - 2014 by Vivante Corp.  All rights reserved.
*
*    The material in this file is confidential and contains trade secrets
*    of Vivante Corporation. This is proprietary information owned by
*    Vivante Corporation. No part of this work may be disclosed,
*    reproduced, copied, transmitted, or used in any way for any purpose,
*    without the express written permission of Vivante Corporation.
*
*****************************************************************************/


#ifndef _2dgpu_h__
#define _2dgpu_h__

#include "gfx/driver/processor/2dgpu/drv_2dgpu_definitions.h"

#ifdef __cplusplus
extern "C" {
#endif

// *****************************************************************************
// *****************************************************************************
// Section: Data Types and Constants
// *****************************************************************************
// *****************************************************************************


// *****************************************************************************
// *****************************************************************************
// Section: GFX Driver Nano2d Client Routines
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    n2d_error_t n2d_blit()

   Summary:
    Copy a source buffer to the the destination buffer

   Description:
    The specified region of the source buffer is copied to the specified region
    of the destination buffer. If the regions are different in size, simple low-quality
    scaling will automatically be performed.

    N2D_YUYV and N2D_UYVY can only be used as the source buffer format. When the
    source buffer format is N2D_YUYV or N2D_UYVY, the source rectangle size and
    destination rectangle size must be equal, otherwise it will return N2D_INVALID_ARGUMENT.
    And the rop or transparency will be ignored.

    An optional blend mode can be specified that defines the blending of the
    source onto the destination.

   Precondition:

   Parameters:
    destination           - Pointer to a n2d_buffer_t structure that describes the destination of the
                            blit
    destination_rectangle - Optional pointer to the rectangle that defines the region inside the
                            destination buffer. If this rectangle is not specified, the entire destination
                            buffer is used as the destination region
    source                - Pointer to a n2d_buffer_t structure that describes the source of the blit
    source_rectangle      - Optional pointer to the rectangle that defines the region inside the source buffer.
                            If this rectangle is not specified, the entire source buffer is used as the source
                            region
    blend                 - Optional blending mode to be applied to each pixel. If no blending is required, set this
                            value to N2D_BLEND_NONE (0)

  Returns:
    Returns the status as defined by n2d_error_t

  Remarks:
    This function will wait until the hardware is complete, i.e. it is synchronous.
  */
n2d_error_t n2d_blit(
    n2d_buffer_t *destination,
    n2d_rectangle_t *destination_rectangle,
    n2d_buffer_t *source,
    n2d_rectangle_t *source_rectangle,
    n2d_blend_t blend);

// *****************************************************************************
/* Function:
    n2d_error_t n2d_draw_state()

   Summary:
    Set the drawing state for any following Nano2D API draw call

   Description:
    In order to setup transparency for the n2d_blit function, this function needs to
    be called. Note that this function is static, so set once, all draw commands that
    follow this function will take this transparency into effect. Call this function
    again with different parameters to set another transparency mode or turn transparency off.

    It will return N2D_INVALID_ARGUMENT if the source defines the transparency but the
    rop has nothing to do with the source buffer.

    The default transparency mode for any newly opened context is N2D_TRANSPARENCY_NONE,
    using a foreground_rop of 0xC (copy source).

    Binary ROPs supported in both foreground and background operations:
        ROP 	Formula 	Description
        0x0 	0 	Set all destination bits to 0.
        0x1 	~(D|S) 	Inverse of merge source and destination.
        0x2 	D&~S 	Mask inverse of source and destination.
        0x3 	~S 	Copy inverse of source.
        0x4 	S&~D 	Mask source and inverse of destination.
        0x5 	~D 	Invert destination.
        0x6 	D^S 	Exclusive or of source and destination.
        0x7 	~(D&S) 	Inverse of mask source and destination.
        0x8 	D&S 	Mask source and destination.
        0x9 	~(D^S) 	Inverse of exclusive or of source and destination.
        0xA 	D 	Copy destination.
        0xB 	D|~S 	Merge inverse of source and destination.
        0xC 	S 	Copy source.
        0xD 	S|~D 	Merge source and inverse of destination.
        0xE 	D|S 	Merge source and destination.
        0xF 	1 	Set all destination bits to 1.

   Precondition:

   Parameters:
    transparency   - The transparency mode applied to each pixel. See n2d_transparency_t for a list of
                     all supported transparency modes
    color          - If transparency is not N2D_TRANSPARENCY_NONE, this color value specifies if a
                     pixel is a foreground or a background pixel. If the color matches, it is a background pixel,
                     otherwise it is a foreground pixel
    foreground_rop - A Binary ROP (ROP2) code that gets executed by the hardware for each foreground pixel
    background_rop - A Binary ROP (ROP2) code that gets executed by the hardware for each background pixel

  Returns:
    Returns the status as defined by n2d_error_t

  Remarks:
    When using a source buffer with the A8 pixel format, transparency must be enabled to N2D_TRANSPARENCY_SOURCE and the alpha channel of color will be used to check for transparency. If the pixel is not transparent, the RGB channels of color value will be used as the color for the pixel.

*/
n2d_error_t n2d_draw_state(
    n2d_transparency_t transparency,
    n2d_color_t color,
    n2d_uint8_t foreground_rop,
    n2d_uint8_t background_rop);

// *****************************************************************************
/* Function:
    n2d_error_t n2d_fill()

   Summary:
    Fill a (partial) buffer with a specified color

   Description:
    Draws and fills a rectangle with a specific color onto destination buffer.

    An optional blend mode can be specified that defines the blending of the
    color onto the destination.

   Precondition:

   Parameters:
    destination   - Pointer to a n2d_buffer_t structure that describes the buffer to be filled
    rectangle     - Pointer to a rectangle that specifies the area to be filled. If rectangle is NULL,
                    the entire buffer will be filled with the specified color
    color         - The color value to use for filling the buffer
    blend         - The blending mode to be applied to each pixel. If no blending is required, set this
                    value to N2D_BLEND_NONE (0)

  Returns:
    Returns the status as defined by n2d_error_t

  Remarks:
    This function will wait until the hardware is complete, i.e. it is synchronous
*/
n2d_error_t n2d_fill(
    n2d_buffer_t *destination,
    n2d_rectangle_t *rectangle,
    n2d_color_t color,
    n2d_blend_t blend);

// *****************************************************************************
/* Function:
    n2d_error_t n2d_line()

   Summary:
    Draw a line

   Description:
    Draw a line with a specific color. The last pixel of the line will not be drawn.

    An optional blend mode can be specified that defines the blending of the
    color onto the destination.

   Precondition:

   Parameters:
    destination  - Pointer to a n2d_buffer_t structure that describes the buffer to be
                    used to draw the line into.
    start        - The starting point of the line, given in destination coordinates.
    end          - The ending point of the line, given in destination coordinates. The last
                   pixel will not be drawn.
    clip         - Optional pointer to a rectangle that specifies the clipping region of
                   the destination. If clip is NULL, the clipping region will be the entire
                   destination buffer.
    color        - The color value to use for drawing the line.
    blend        - The blending mode to be applied to each pixel on the line. If no
                   blending is required, set this value to N2D_BLEND_NONE (0).

  Returns:
    Returns the status as defined by n2d_error_t

  Remarks:
    This function will wait until the hardware is complete, i.e. it is synchronous
*/
n2d_error_t n2d_line(
    n2d_buffer_t *destination,
    n2d_point_t start,
    n2d_point_t end,
    n2d_rectangle_t *clip,
    n2d_color_t color,
    n2d_blend_t blend);

// *****************************************************************************
/* Function:
    n2d_error_t n2d_open()

   Summary:
    Open Nano2d context

   Description:
    The n2d_line, n2d_fill, n2d_blit, and n2d_draw_state functions require
    a Nano2D context to be opened. This function is the first interface that
    accesses the hardware. The hardware will be turned on and initialized.

   Precondition:

   Parameters:

   Returns:
    Returns the status as defined by n2d_error_t.

   Remarks:
    There is only one Nano2d context per application, so this function must
    be called once in your application.
*/
n2d_error_t n2d_open(
    void);

// *****************************************************************************
// *****************************************************************************
// Section: GFX Driver Nano2d Module Initialization Routines
// *****************************************************************************
// *****************************************************************************


// *****************************************************************************
/* Function:
    n2d_error_t n2d_init_hardware()

   Summary:
    Initializes the n2d driver and peripheral hardware

   Description:
    The initializes the memory region, sets base address, establishes the irq
    and connects the hardware to application.

   Precondition:

   Parameters:
    params           - Initialization parameters. See n2d_module_parameters_t

  Returns:
    Returns the status as defined by n2d_error_t

  Remarks:
    For PIC32MZ DA, registerMemBase2D is 0xBF8EB000 and baseAddress is 0
*/
n2d_error_t n2d_init_hardware(
    n2d_module_parameters_t *params
    );

DRV_2DGPU_STATUS DRV_2DGPU_Line ( n2d_buffer_t *destination, n2d_point_t start,
        n2d_point_t end, n2d_rectangle_t *clip, n2d_color_t color, n2d_blend_t blend);

DRV_2DGPU_STATUS DRV_2DGPU_Fill( n2d_buffer_t *, n2d_rectangle_t *, n2d_color_t );

DRV_2DGPU_STATUS DRV_2DGPU_Blit( n2d_buffer_t *, n2d_rectangle_t *, n2d_buffer_t *, n2d_rectangle_t * );

DRV_2DGPU_STATUS DRV_2DGPU_StatusGet( void );

void DRV_2DGPU_CallbackRegister (DRV_2DGPU_LIB_CALLBACK, uintptr_t);

SYS_MODULE_OBJ DRV_2DGPU_Initialize( const SYS_MODULE_INDEX drvIndex, const SYS_MODULE_INIT * const init );


#ifdef __cplusplus
}
#endif

#endif /* _2dgpu_h__ */
