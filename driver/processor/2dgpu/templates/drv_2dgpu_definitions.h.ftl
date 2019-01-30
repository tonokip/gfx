/*******************************************************************************
  2DGPU Driver Definitions Header File

  Company:
    Microchip Technology Inc.

  File Name:
    drv_2dgpu_definitions.h

  Summary:
    GFX2D Driver Definitions Header File

  Description:
    This file provides implementation-specific definitions for the 2DGPU
    driver's system interface.
*******************************************************************************/

//DOM-IGNORE-BEGIN
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
//DOM-IGNORE-END

#ifndef DRV_2DGPU_DEFINITIONS_H
#define DRV_2DGPU_DEFINITIONS_H

// *****************************************************************************
// *****************************************************************************
// Section: File includes
// *****************************************************************************
// *****************************************************************************

#include "stddef.h"
#include "system/system_module.h"
#include "driver/driver.h"
#include "driver/driver_common.h"
#include "system/int/sys_int.h"

#include "driver/driver_common.h"
#include "gfx/hal/inc/gfx_common.h"
#include "gfx/hal/inc/gfx_driver_interface.h"
#include "gfx/hal/inc/gfx_default_impl.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

#ifndef SYS_DEBUG
    #define SYS_DEBUG(x, y)
#endif


#define IN
#define OUT

typedef int                 n2d_bool_t;
typedef unsigned char       n2d_uint8_t;
typedef short               n2d_int16_t;
typedef unsigned short      n2d_uint16_t;
typedef int                 n2d_int32_t;
typedef unsigned int        n2d_uint32_t;
typedef unsigned long long  n2d_uint64_t;
typedef unsigned int        n2d_size_t;
typedef float               n2d_float_t;

#ifdef __cplusplus
#define N2D_NULL 0
#else
#define N2D_NULL ((void *) 0)
#endif

#define N2D_TRUE  1
#define N2D_FALSE 0

#define N2D_INFINITE ((n2d_uint32_t) ~0U)

#define __gcmSTART(reg_field) \
    (0 ? reg_field)

#define __gcmEND(reg_field) \
    (1 ? reg_field)

#define __gcmGETSIZE(reg_field) \
    (__gcmEND(reg_field) - __gcmSTART(reg_field) + 1)

#define __gcmALIGN(data, reg_field) \
    (((n2d_uint32_t) (data)) << __gcmSTART(reg_field))

#define __gcmMASK(reg_field) \
    ((n2d_uint32_t) ((__gcmGETSIZE(reg_field) == 32) \
        ?  ~0 \
        : (~(~0 << __gcmGETSIZE(reg_field)))))

#define gcmVERIFYFIELDVALUE(data, reg, field, value) \
( \
    (((n2d_uint32_t) (data)) >> __gcmSTART(reg##_##field) & \
                             __gcmMASK(reg##_##field)) \
        == \
    (reg##_##field##_##value & __gcmMASK(reg##_##field)) \
)

#define gcmSETFIELD(data, reg, field, value) \
( \
    (((n2d_uint32_t) (data)) \
        & ~__gcmALIGN(__gcmMASK(reg##_##field), reg##_##field)) \
        |  __gcmALIGN((n2d_uint32_t) (value) \
            & __gcmMASK(reg##_##field), reg##_##field) \
)

#define gcmGETFIELD(data, reg, field) \
( \
    ((((n2d_uint32_t) (data)) >> __gcmSTART(reg##_##field)) \
        & __gcmMASK(reg##_##field)) \
)

#define gcmSETFIELDVALUE(data, reg, field, value) \
( \
    (((n2d_uint32_t) (data)) \
        & ~__gcmALIGN(__gcmMASK(reg##_##field), reg##_##field)) \
        |  __gcmALIGN(reg##_##field##_##value \
            & __gcmMASK(reg##_##field), reg##_##field) \
)

#define gcmSETMASKEDFIELDVALUE(reg, field, value) \
( \
    gcmSETFIELDVALUE(~0, reg,          field, value) & \
    gcmSETFIELDVALUE(~0, reg, MASK_ ## field, ENABLED) \
)

#define gcmSETMASKEDFIELD(reg, field, value) \
( \
    gcmSETFIELD     (~0, reg,          field, value) & \
    gcmSETFIELDVALUE(~0, reg, MASK_ ## field, ENABLED) \
)

#define gcmALIGN(n, align) \
( \
    ((n) + ((align) - 1)) & ~((align) - 1) \
)

#define gcmMIN(x, y) \
( \
    ((x) <= (y)) \
        ? (x) \
        : (y) \
)

#define gcmMAX(x, y) \
( \
    ((x) >= (y)) \
        ? (x) \
        : (y) \
)

#define gcmINT2PTR(i) \
( \
    (void *)(n2d_uint32_t)(i) \
)

#define gcmPTR2INT(p) \
( \
    (n2d_uint32_t)(p) \
)

#define N2D_IS_SUCCESS(error) (error == N2D_SUCCESS)
#define N2D_IS_ERROR(error)   (error != N2D_SUCCESS)

#define N2D_ON_ERROR(func) \
    do \
    { \
        error = func; \
        if (N2D_IS_ERROR(error)) \
        { \
            goto on_error; \
        } \
    } \
    while (0)

#ifndef gcmCOUNTOF
#   define gcmCOUNTOF(array) \
        (sizeof(array) / sizeof(array[0]))
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
                    alpha channel is in bits 15:12. Note: currently not available in HAL
    N2D_BGRA4444  - 16-bit RGBA format with 4 bits per color channel. Red is
                    in bits 11:8, green in bits 7:4, blue in bits 3:0 and the
                    alpha channel is in bits 15:12. Note: currently not available in HAL
    N2D_A8        - 8-bit alpha format. There are no RGB values.

  Remarks:
    The pixel type for a n2d_buffer_t structure
*/
typedef enum n2d_buffer_format
{
    N2D_RGBA8888,
    N2D_BGRA8888,
    N2D_RGB565,
    N2D_BGR565,
        N2D_RGBA4444,   /* currently not available in MPLAB Harmony HAL */
    N2D_BGRA4444,   /* currently not available in MPLAB Harmony HAL */
    N2D_A8,
}
n2d_buffer_format_t;

// *****************************************************************************
/* Structure:
    n2d_orientation

  Summary:
    List of blending modes

  Description:
    N2D_0   - Buffer is 0 degrees rotated.
    N2D_90  - Buffer is 90 degrees rotated.
    N2D_180 - Buffer is 180 degrees rotated.
    N2D_270 - Buffer is 270 degrees rotated.

  Remarks:
   Orientation is orthogonal. Rotation which is not parallel to the x or y axis
   is not supported.
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
// Section: Data Types
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* 2DGPU Driver Status

  Summary:
    Defines the status values

  Description:
    This data type defines the error values for the errors occured during transfer.

  Remarks:
    None.
*/

typedef enum
{
    /* Busy*/
    DRV_2DGPU_STATUS_NONE,

    /* Commit Successful */
    DRV_2DGPU_STATUS_NACK,

} DRV_2DGPU_STATUS;

// *****************************************************************************

typedef void (*DRV_2DGPU_LIB_CALLBACK)( uintptr_t context);
// *****************************************************************************

typedef struct
{
    DRV_2DGPU_LIB_CALLBACK callback_fn;
    uintptr_t context;
}DRV_2DGPU_CALLBACK_OBJECT;


typedef void (* DRV_2DGPU_LIB_CALLBACK)( uintptr_t );

typedef DRV_2DGPU_STATUS (*DRV_2DGPU_LIB_LINE) ( n2d_buffer_t *, n2d_point_t ,
        n2d_point_t , n2d_rectangle_t *, n2d_color_t , n2d_blend_t );

typedef DRV_2DGPU_STATUS (* DRV_2DGPU_LIB_FILL)(n2d_buffer_t *, n2d_rectangle_t *,
            n2d_color_t , n2d_blend_t );

typedef DRV_2DGPU_STATUS (* DRV_2DGPU_LIB_COPY)(n2d_buffer_t *,n2d_rectangle_t *,n2d_buffer_t *,n2d_rectangle_t *,
                                                 n2d_blend_t );

typedef DRV_2DGPU_STATUS (* DRV_2DGPU_LIB_BLIT)(n2d_buffer_t *,n2d_rectangle_t *,n2d_buffer_t *,n2d_rectangle_t *,
            n2d_blend_t );

typedef DRV_2DGPU_STATUS (* DRV_2DGPU_LIB_STATUS_GET)( void );

typedef void (* DRV_2DGPU_LIB_CALLBACK_REGISTER)(DRV_2DGPU_LIB_CALLBACK, uintptr_t);

// *****************************************************************************
/* 2DGPU Driver library Interface Data

  Summary:
    Defines the data required to initialize the 2DGPU driver library Interface.

  Description:
    This data type defines the data required to initialize the 2DGPU driver library
    Interface. If the driver is built statically, the members of this data
    structure are statically over-ridden by static override definitions in the
    configuration.h file.

  Remarks:
    None.
*/

typedef struct
{
    /* 2DGPU Lib line API */
    DRV_2DGPU_LIB_LINE line;

    /* 2DGPU Lib fill API */
    DRV_2DGPU_LIB_FILL fill;

    /* 2DGPU Lib copy API */
    DRV_2DGPU_LIB_COPY copy;

    /* 2DGPU Lib blit API */
    DRV_2DGPU_LIB_BLIT blit;

    /* 2DGPU Lib status API */
    DRV_2DGPU_LIB_STATUS_GET statusGet;

    /* 2DGPU Lib callback register API */
    DRV_2DGPU_LIB_CALLBACK_REGISTER callbackRegister;

} DRV_2DGPU_LIB_INTERFACE;

// *****************************************************************************
/* 2DGPU Driver Initialization Data

  Summary:
    Defines the data required to initialize the 2DGPU driver

  Description:
    This data type defines the data required to initialize or the 2DGPU driver.
    If the driver is built statically, the members of this data structure are
    statically over-ridden by static override definitions in the
    configuration.h file.

  Remarks:
    None.
*/

typedef struct
{
    /* Identifies the PLIB API set to be used by the driver to access the
     * peripheral. */
    //const DRV_2DGPU_PLIB_INTERFACE* 2DgpuPlib;

    /* Number of clients */
    uint32_t numClients;
//<#if DRV_2DGPU_MODE == "Asynchronous">
//
//    /* Interrupt source ID for the I2C interrupt. */
//    INT_SOURCE interrupt2DGPU;
//
//    /* Driver Queue Size */
//    size_t queueSize;
//</#if>

} DRV_2DGPU_INIT;

//DOM-IGNORE-BEGIN
#ifdef __cplusplus
}
#endif
//DOM-IGNORE-END

#endif // #ifndef DRV_2DGPU_DEFINITIONS_H

/*******************************************************************************
 End of File
*/
