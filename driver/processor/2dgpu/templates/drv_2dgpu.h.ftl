/*******************************************************************************
 Module for Microchip Graphics Library - Graphics Driver Layer

  Company:
    Microchip Technology Inc.

  File Name:
    libnano2D.h

  Summary:
    Main header file for MPLAB Harmony Graphics Driver libnano2D GPU functions

  Description:
    The API functions to be used for the Nano2D graphics accelerator.

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2016 released Microchip Technology Inc.  All rights reserved.

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


#ifndef _nano2d_h__
#define _nano2d_h__

#include "framework/gfx/driver/processor/nano2d/libnano2D_types.h"
#include "drv_2dgpu_definitions.h"

#ifdef __cplusplus
extern "C" {
#endif

// *****************************************************************************
// *****************************************************************************
// Section: Data Types and Constants
// *****************************************************************************
// *****************************************************************************


// *****************************************************************************
/* Structure:
    n2d_module_parameters

  Summary:
    GPU peripheral Initialization parameters

  Description:
    irqLine2D         - command completion interrupt pin
    registerMemBase2D - base address of gpu (physical address)
    registerMemsize2D - size of gpu address space
    contiguousSize    - size of memory pool
    contiguousBase    - start address of memory (virtual address)
    baseAddress       - base address display buffer


  Remarks:
    None
*/

typedef struct n2d_module_parameters
{
    n2d_int32_t     irqLine2D;
    n2d_uint32_t    registerMemBase2D;
    n2d_uint32_t    registerMemSize2D;
    n2d_uint32_t    contiguousSize;
    n2d_uint32_t    contiguousBase;
    n2d_uint32_t    baseAddress;
}
n2d_module_parameters_t;

// *****************************************************************************
/* Structure:
    n2d_blend

  Summary:
    List of blending modes

  Description:
    N2D_BLEND_NONE      - S, i.e. no blending
    N2D_BLEND_SRC_OVER  - S + (1 - Sa) * D
    N2D_BLEND_DST_OVER  - (1 - Da) * S + D
    N2D_BLEND_SRC_IN    - Da * S
    N2D_BLEND_DST_IN    - Sa * D
    N2D_BLEND_ADDITIVE  - S + D
    N2D_BLEND_SUBTRACT  - D * (1 - S)

  Remarks:
    Some of the Nano2D API functions calls support blending. S and D represent source
    and destination color channels and Sa and Da represent the source and
    destination alpha channels
*/
typedef enum n2d_blend
{
    N2D_BLEND_NONE,
    N2D_BLEND_SRC_OVER,
    N2D_BLEND_DST_OVER,
    N2D_BLEND_SRC_IN,
    N2D_BLEND_DST_IN,
    N2D_BLEND_ADDITIVE,
    N2D_BLEND_SUBTRACT,
}
n2d_blend_t;

// *****************************************************************************
/* Structure:
    n2d_buffer_format

  Summary:
    List of blending modes

  Description:
    N2D_RGBA8888  - 32-bit RGBA format with 8 bits per color channel. Red is
                    in bits 7:0, green in bits 15:8, blue in bits 23:16, and
                    the alpha channel is in bits 31:24
    N2D_BGRA8888  - 32-bit RGBA format with 8 bits per color channel. Red is
                    in bits 23:16, green in bits 15:8, blue in bits 7:0, and
                    the alpha channel is in bits 31:24
    N2D_RGB565    - 16-bit RGB format with 5 and 6 bits per color channel. Red
                    is in bits 4:0, green in bits 10:5, and the blue color
                    channel is in bits 15:11
    N2D_BGR565    - 16-bit RGB format with 5 and 6 bits per color channel. Red
                    is in bits 15:11, green in bits 10:5, and the blue color
                    channel is in bits 4:0
    N2D_RGBA4444  - 16-bit RGBA format with 4 bits per color channel. Red is
                    in bits 3:0, green in bits 7:4, blue in bits 11:8 and the
                    alpha channel is in bits 15:12
    N2D_BGRA4444  - 16-bit RGBA format with 4 bits per color channel. Red is
                    in bits 11:8, green in bits 7:4, blue in bits 3:0 and the
                    alpha channel is in bits 15:12
    N2D_A8        - 8-bit alpha format. There are no RGB values.
    N2D_YUYV      - Packed YUV format, 32-bit for 2 pixels. Y0 is in bits 7:0
                    and V is in bits 31:23. This format can only be used as a
                    source
    N2D_UYVY      - Packed YUV format, 32-bit for 2 pixels. U is in bits 7:0
                    and Y1 is in bits 31:23. This format can only be used as a
                    source

  Remarks:
    The pixel type for a n2d_buffer_t structure
*/
typedef enum n2d_buffer_format
{
    N2D_RGBA8888,
    N2D_BGRA8888,
    N2D_RGB565,
    N2D_BGR565,
    N2D_RGBA4444,
    N2D_BGRA4444,
    N2D_A8,
    N2D_YUYV,
    N2D_UYVY,
}
n2d_buffer_format_t;

// *****************************************************************************
/* Structure:
    n2d_orientation

  Summary:
    List of blending modes

  Description:
    N2D_0   - 32-bit RGBA format with 8 bits per color channel. Red is in bits 7:0, green in bits 15:8, blue in bits 23:16, and the alpha channel is in bits 31:24.
    N2D_90  - S + (1 - Sa) * D
    N2D_180 - (1 - Da) * S + D
    N2D_270 - Da * S

  Remarks:
    Some of the Nano2D API functions calls support blending. S and D
    represent source and destination color channels and Sa and Da
    represent the source and destination alpha channels
*/
typedef enum n2d_orientation
{
    N2D_0,
    N2D_90,
    N2D_180,
    N2D_270,
}
n2d_orientation_t;

// *****************************************************************************
/* Structure:
    n2d_buffer

  Summary:
    A wrapper structure for any image or render target

  Description:
    width       - Width of the buffer in pixels
    height      - Height of the buffer in pixels
    stride      - Stride of the buffer in bytes
    format      - Pixel format of the buffer
    orientation - Buffer's orientation
    handle      - Memory handle to the buffer's memory as allocated by the Nano kernel
    memory      - Logical pointer to the buffer's memory for the CPU
    gpu         - Physical address of the buffer's memory the hardware can access

  Remarks:
    Each piece of memory, whether it is an image used as a source or a buffer used as a
    destination, requires a structure to define it. This structure contains all the information
    the Nano2D API requires to access the buffer's memory by the hardware
*/
typedef struct n2d_buffer
{
    n2d_int32_t width;
    n2d_int32_t height;
    n2d_int32_t stride;
    n2d_buffer_format_t format;
    n2d_orientation_t orientation;
    void *handle;
    void *memory;
    n2d_uint32_t gpu;
}
n2d_buffer_t;

// *****************************************************************************
/* Structure:
    n2d_error

  Summary:
    Error codes that the Nano2D functions can return

  Description:
    N2D_SUCCESS          - Success
    N2D_INVALID_ARGUMENT - An invalid argument was specified
    N2D_OUT_OF_MEMORY    - Out of memory
    N2D_NO_CONTEXT       - No open context is present
    N2D_TIMEOUT          - A timeout has accored during a wait
    N2D_OUT_OF_RESOURCES - Out of system resources
    N2D_GENERIC_IO       - Cannot communicate with the kernel driver
    N2D_NOT_SUPPORTED    - The request is not supported

  Remarks:
   All API functions return a status code. On success, N2D_SUCCESS will be returned
   when a function is successful. This value is set to zero, so if any function returns
   a non-zero value, an error has occured
*/
typedef enum n2d_error
{
    N2D_SUCCESS = 0,
    N2D_INVALID_ARGUMENT,
    N2D_OUT_OF_MEMORY,
    N2D_NO_CONTEXT,
    N2D_TIMEOUT,
    N2D_OUT_OF_RESOURCES,
    N2D_GENERIC_IO,
    N2D_NOT_SUPPORTED,
}
n2d_error_t;

// *****************************************************************************
/* Structure:
    n2d_point

  Summary:
    A position on a pixel

  Description:
    Defines a position on the screen

    x - horizontal coordinate of the point
    y - vertical coordinate of the point

  Remarks:
*/
typedef struct n2d_point
{
    n2d_int32_t x;
    n2d_int32_t y;
}
n2d_point_t;

// *****************************************************************************
/* Structure:
    n2d_rectangle

  Summary:
    A rectangle

  Description:
    Defines a rectangular shape area of the screen

    x      - Left coordinate of the rectangle
    y      - Top coordinate of the rectangle
    width  - Width of the rectangle
    height - Height of the rectangle

  Remarks:

*/
typedef struct n2d_rectangle
{
    n2d_int32_t x;
    n2d_int32_t y;
    n2d_int32_t width;
    n2d_int32_t height;
}
n2d_rectangle_t;

// *****************************************************************************
/* Structure:
    n2d_transparency

  Summary:
    Transparency modes

  Description:
    N2D_TRANSPARENCY_NONE        - No transparency
    N2D_TRANSPARENCY_SOURCE      - The source defines the transparency
    N2D_TRANSPARENCY_DESTINATION - The destination defines the transparency

  Remarks:
    The Nano2D hardware can be programmed to use transparency, extracted from either
    the source or the destination
*/
typedef enum n2d_transparency
{
    N2D_TRANSPARENCY_NONE,
    N2D_TRANSPARENCY_SOURCE,
    N2D_TRANSPARENCY_DESTINATION,
}
n2d_transparency_t;

// *****************************************************************************
/* Color

  Summary:
    Identifies a specific pixel color

  Description:
    Color container

  Remarks:
*/
typedef n2d_int32_t n2d_color_t;

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

#ifdef __cplusplus
}
#endif

#endif /* _nano2d_h__ */
