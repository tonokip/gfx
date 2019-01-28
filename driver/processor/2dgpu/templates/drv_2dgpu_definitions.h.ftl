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
#include "peripheral/2dgpu/plib_2dgpu.h"

#include "driver/driver_common.h"
#include "gfx/hal/inc/gfx_common.h"
#include "gfx/hal/inc/gfx_driver_interface.h"
#include "gfx/hal/inc/gfx_default_impl.h"
#include "peripheral/2dgpu/plib_2dgpu.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

#ifndef SYS_DEBUG
    #define SYS_DEBUG(x, y)
#endif
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
    2DGPU_CALLBACK callback_fn;
    uintptr_t context;
}2DGPU_CALLBACK_OBJECT;


typedef void (* DRV_2DGPU_PLIB_CALLBACK)( uintptr_t );

typedef 2DGPU_STATUS (* DRV_2DGPU_PLIB_FILL)( 2DGPU_BUFFER *, 2DGPU_RECTANGLE *, gpu_color_t );

typedef 2DGPU_STATUS (* DRV_2DGPU_PLIB_COPY)( 2DGPU_BUFFER *, 2DGPU_RECTANGLE *, 2DGPU_BUFFER *, 2DGPU_RECTANGLE * );

typedef 2DGPU_STATUS (* DRV_2DGPU_PLIB_BLEND)( 2DGPU_BUFFER *, 2DGPU_RECTANGLE *, 2DGPU_BUFFER *, 2DGPU_RECTANGLE *,
                                               2DGPU_BUFFER *, 2DGPU_RECTANGLE *, 2DGPU_BLEND );

typedef 2DGPU_STATUS (* DRV_2DGPU_PLIB_STATUS_GET)( void );

typedef void (* DRV_2DGPU_PLIB_CALLBACK_REGISTER)(DRV_2DGPU_PLIB_CALLBACK, uintptr_t);

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
    DRV_2DGPU_PLIB_LINE line;

    /* 2DGPU Lib fill API */
    DRV_2DGPU_PLIB_FILL fill;

    /* 2DGPU Lib copy API */
    DRV_2DGPU_PLIB_COPY copy;

    /* 2DGPU Lib blit API */
    DRV_2DGPU_PLIB_BLEND blit;

    /* 2DGPU Lib status API */
    DRV_2DGPU_PLIB_STATUS_GET statusGet;

    /* 2DGPU Lib callback register API */
    DRV_2DGPU_PLIB_CALLBACK_REGISTER callbackRegister;

} DRV_2DGPU_PLIB_INTERFACE;

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
    const DRV_2DGPU_PLIB_INTERFACE* 2DgpuPlib;

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
