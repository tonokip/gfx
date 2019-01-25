/*******************************************************************************
  2D Graphics Engine(${GFX2D_INSTANCE_NAME}) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${GFX2D_INSTANCE_NAME?lower_case}.h

  Summary
    ${GFX2D_INSTANCE_NAME} PLIB Header File.

  Description
    This file defines the interface to the GFX2D peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
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

#ifndef PLIB_${GFX2D_INSTANCE_NAME}_H      // Guards against multiple inclusion
#define PLIB_${GFX2D_INSTANCE_NAME}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include "device.h"

#include <stdbool.h>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************
/* The following data type definitions are used by the functions in this
    interface and should be considered part it.
*/
// *****************************************************************************
/* GFX2D Instruction Status

   Summary:
    GFX2D Instruction Status data type.

   Description:
    This data type defines the GFX2D Instruction Status.

   Remarks:
    None.
*/

typedef enum
{
    /* No Error */
    GFX2D_ERROR_NONE,

    /* GPU returned Nack */
    GFX2D_ERROR_NACK,

} GFX2D_STATUS;

// *****************************************************************************
/* GFX2D State.

   Summary:
    GFX2D PLib Task State.

   Description:
    This data type defines the GFX2D PLib Task State.

   Remarks:
    None.

*/

typedef enum {

    /* GFX2D PLib Task Error State */
    GFX2D_STATE_ERROR = -1,

    /* GFX2D PLib Task Idle State */
    GFX2D_STATE_IDLE,

    /* GFX2D PLib Task Instruction Done State */
    GFX2D_STATE_TRANSFER_DONE,

} GFX2D_STATE;

// *****************************************************************************
/* GFX2D Callback

   Summary:
    GFX2D Callback Function Pointer.

   Description:
    This data type defines the GFX2D Callback Function Pointer.

   Remarks:
    None.
*/

typedef void (*GFX2D_CALLBACK)
(
    /* Transfer context */
    uintptr_t contextHandle
);

// *****************************************************************************
/* GFX2D PLib Instance Object

   Summary:
    GFX2D PLib Object structure.

   Description:
    This data structure defines the GFX2D PLib Instance Object.

   Remarks:
    None.
*/

typedef struct
{
    uint16_t address;

    /* State */
    GFX2D_STATE state;

    /* Transfer status */
    GFX2D_STATUS error;

    /* Transfer Event Callback */
    GFX2D_CALLBACK callback;

    /* Transfer context */
    uintptr_t context;

} GFX2D_OBJ;

// *****************************************************************************
/**
 * \berif GFX2D buffer format
 */
 typedef enum gpu_buffer_format {
    GFX2D_A8       = 1,  /*!< 8 bits per pixel alpha, with user-defined constant color */
    GFX2D_RGB12    = 4,  /*!< 12 bits per pixel, 4 bits per color channel */
    GFX2D_ARGB16   = 5,  /*!< 16 bits per pixel with 4-bit width alpha value, and 4 bits per color channel */
    GFX2D_RGB15    = 6,  /*!< 15 bits per pixel, 5 bits per color channel */
    GFX2D_TRGB16   = 7,  /*!< 16 bits per pixel, 5 bits for the red and blue channels and 6 bits for the green channel */
    GFX2D_RGBT16   = 8,  /*!< 16 bits per pixel, with 1 bit for transparency and 5 bits for color channels */
    GFX2D_RGB16    = 9,  /*!< 16 bits per pixel, 5 bits for the red and blue channels and 6 bits for the green channel */
    GFX2D_ARGB8888 = 10, /*!< 32 bits per pixel, 8 bits for alpha and color channels */
    GFX2D_RGBA8888 = 11, /*!< 32 bits per pixel, 8 bits for alpha and color channels */
    GFX2D_BUFFER_FORMAT_SIZE
} GFX2D_BUFFER_FORMAT;

/* GPU BUffer format's pixel size in bytes */
#define GFX2D_BUFFER_FORMAT_PIXEL_SIZE {1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 4, 4};

/**
 * \berif GFX2D Buffer
 */
typedef struct gpu_buffer {
    uint32_t               width;  /*!< Buffer width in pixel */
    uint32_t               height; /*!< Buffer height in pixel */
    enum gpu_buffer_format fmt;    /*!< Buffer pixel format */
    uint32_t               addr;   /*!< Buffer memory address */
} GFX2D_BUFFER;

typedef struct gpu_rectangle {
    uint32_t x;      /*!< X position in pixel, start from 0 */
    uint32_t y;      /*!< Y position in pixel, start from 0 */
    uint32_t width;  /*!< Width in pixel */
    uint32_t height; /*!< Height in pixel */
} GFX2D_RECTANGLE;

/**
 * \berif GFX2D color
 * A(31-24), R(23-16), G(15-8), B(7-0)
 */
typedef uint32_t gpu_color_t;
#define GFX2D_COLOR(a, r, g, b) (((a) << 24) | ((r) << 16) | ((g) << 8) | (b))

/**
 * \berif GFX2D Blend functions
 */
typedef enum gpu_blend {
    GFX2D_BLEND_SRC_OVER, /* S + (1-Sa)*D */
    GFX2D_BLEND_DST_OVER, /* (1-Da) * S + D */
    GFX2D_BLEND_SRC_IN,   /* Da * S */
    GFX2D_BLEND_DST_IN,   /* Sa * D */
    GFX2D_BLEND_ADDITIVE, /* S + D */
    GFX2D_BLEND_SUBTRACT  /* D * (1 - S) */
} GFX2D_BLEND;


// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
/* The following functions make up the methods (set of possible operations) of
    this interface.
*/

void ${GFX2D_INSTANCE_NAME}_Initialize( void );

void ${GFX2D_INSTANCE_NAME}_Enable( void );

void ${GFX2D_INSTANCE_NAME}_Disable( void );

void ${GFX2D_INSTANCE_NAME}_CallbackRegister(GFX2D_CALLBACK callback, uintptr_t contextHandle);

GFX2D_STATUS ${GFX2D_INSTANCE_NAME}_Fill(struct gpu_buffer *dst, struct gpu_rectangle *rect, gpu_color_t color);

GFX2D_STATUS ${GFX2D_INSTANCE_NAME}_Copy(struct gpu_buffer *dst, struct gpu_rectangle *dst_rect, struct gpu_buffer *src,
                        struct gpu_rectangle *src_rect);

GFX2D_STATUS ${GFX2D_INSTANCE_NAME}_Blend(struct gpu_buffer *dst, struct gpu_rectangle *dst_rect, struct gpu_buffer *fg,
                         struct gpu_rectangle *fg_rect, struct gpu_buffer *bg, struct gpu_rectangle *bg_rect,
                         enum gpu_blend blend);

bool ${GFX2D_INSTANCE_NAME}_IsBusy(void);

GFX2D_STATUS ${GFX2D_INSTANCE_NAME}_StatusGet(void);

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif /* PLIB_${GFX2D_INSTANCE_NAME}_H */
