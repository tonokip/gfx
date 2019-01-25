/*******************************************************************************
  GFX GFX2D Driver Interface Declarations for Static Single Instance Driver

  Company:
    Microchip Technology Inc.

  File Name:
    drv_gfx2d.h

  Summary:
    GFX GFX2D driver interface declarations for the static single instance driver.

  Description:
    The GFX2D device driver provides a simple interface to manage the GFX2D
    module on Microchip microcontrollers. This file defines the interface
    Declarations for the GFX2D driver.

  Remarks:
    Static interfaces incorporate the driver instance number within the names
    of the routines, eliminating the need for an object ID or object handle.

    Static single-open interfaces also eliminate the need for the open handle.
*******************************************************************************/

//DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2019 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED AS IS  WITHOUT  WARRANTY  OF  ANY  KIND,
EITHER EXPRESS  OR  IMPLIED,  INCLUDING  WITHOUT  LIMITATION,  ANY  WARRANTY  OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A  PARTICULAR  PURPOSE.
IN NO EVENT SHALL MICROCHIP OR  ITS  LICENSORS  BE  LIABLE  OR  OBLIGATED  UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION,  BREACH  OF  WARRANTY,  OR
OTHER LEGAL  EQUITABLE  THEORY  ANY  DIRECT  OR  INDIRECT  DAMAGES  OR  EXPENSES
INCLUDING BUT NOT LIMITED TO ANY  INCIDENTAL,  SPECIAL,  INDIRECT,  PUNITIVE  OR
CONSEQUENTIAL DAMAGES, LOST  PROFITS  OR  LOST  DATA,  COST  OF  PROCUREMENT  OF
SUBSTITUTE  GOODS,  TECHNOLOGY,  SERVICES,  OR  ANY  CLAIMS  BY  THIRD   PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE  THEREOF),  OR  OTHER  SIMILAR  COSTS.
*******************************************************************************/
//DOM-IGNORE-END

#ifndef _DRV_GFX_GFX2D_H
#define _DRV_GFX_GFX2D_H


// *****************************************************************************
// *****************************************************************************
// Section: File includes
// *****************************************************************************
// *****************************************************************************
/* Note:  A file that maps the interface definitions above to appropriate static
          implementations (depending on build mode) is included at the bottom of
          this file.
*/

#include "driver/driver_common.h"
#include "gfx/hal/inc/gfx_common.h"
#include "gfx/hal/inc/gfx_driver_interface.h"
#include "gfx/hal/inc/gfx_default_impl.h"
#include "peripheral/gfx2d/plib_gfx2d.h"

#include "drv_gfx2d_definitions.h"

#ifdef __cplusplus
    extern "C" {
#endif

// *****************************************************************************
/* Function:
    SYS_MODULE_OBJ DRV_GFX2D_Initialize
    (
        const SYS_MODULE_INDEX drvIndex,
        const SYS_MODULE_INIT * const init
    )

  Summary:
    Initializes the GFX2D instance for the specified driver index.

  Description:
    This routine initializes the GFX2D driver instance for the specified driver
    index, making it ready for clients to open and use it. The initialization
    data is specified by the init parameter. The initialization may fail if the
    number of driver objects allocated are insufficient or if the specified
    driver instance is already initialized. The driver instance index is
    independent of the GFX2D peripheral instance it is associated with.
    For example, driver instance 0 can be assigned to GFX2D peripheral instance 2.

  Precondition:
    None.

  Parameters:
    drvIndex - Identifier for the instance to be initialized

    init - Pointer to the init data structure containing any data necessary to
    initialize the driver.

  Returns:
    If successful, returns a valid handle to a driver instance object.
    Otherwise, returns SYS_MODULE_OBJ_INVALID.

  Example:
    <code>
    // The following code snippet shows an example GFX2D driver initialization.

    SYS_MODULE_OBJ objectHandle;

    DRV_GFX2D_PLIB_INTERFACE drvGFX2DPLibAPI = {
        .read = (DRV_GFX2D_PLIB_FILL)GFX2D_Fill,
        .copy = (DRV_GFX2D_PLIB_COPY)GFX2D_Copy,
        .blend = (DRV_GFX2D_PLIB_BLEND)GFX2D_Blend,
        .isBusy = (DRV_GFX2D_PLIB_ISBUSY)GFX2D_IsBusy,
        .statusGet = (DRV_GFX2D_PLIB_STATUSGET)GFX2D_StatusGet,
        .callbackRegister = (DRV_GFX2D_PLIB_CALLBACK_REGISTER)GFX2D_CallbackRegister,
    };

    DRV_GFX2D_INIT drvGFX2DInitData = {

        .GFX2DPlib = &drvGFX2D0PLibAPI,
        .interruptGFX2D = DRV_GFX2D_INT_SRC_IDX0,
        .queueSize = DRV_GFX2D_QUEUE_SIZE_IDX0,
    };

    objectHandle = DRV_GFX2D_Initialize(DRV_GFX2D_INDEX, (SYS_MODULE_INIT*)&drvGFX2DInitData);
    if (objectHandle == SYS_MODULE_OBJ_INVALID)
    {
        // Handle error
    }
    </code>

  Remarks:
    This routine must be called before any other GFX2D routine is called.
    This routine should only be called once during system initialization.
*/
SYS_MODULE_OBJ DRV_GFX2D_Initialize( const SYS_MODULE_INDEX drvIndex, const SYS_MODULE_INIT * const init );


// *****************************************************************************
// *****************************************************************************
// Section: Interface Headers for the Static Driver
// *****************************************************************************
// *****************************************************************************


// *****************************************************************************
/* Function:
    void  DRV_GFX2D_Fill()

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
void  DRV_GFX2D_Fill(
    GFX2D_BUFFER *destination,
    GFX2D_RECTANGLE *rectangle,
    gpu_color_t color);

// *****************************************************************************
/* Function:
    void DRV_GFX2D_Copy()

   Summary:
    Copy a source buffer to the the destination buffer

   Description:
    The specified region of the source buffer is copied to the specified region
    of the destination buffer. If the regions are different in size, simple low-quality
    scaling will automatically be performed.

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

  Returns:
    Returns the status as defined by GFX_STATUS

  Remarks:
    This function will wait until the hardware is complete, i.e. it is synchronous.
  */
void DRV_GFX2D_Copy(
    GFX2D_BUFFER *destination,
    GFX2D_RECTANGLE *destination_rectangle,
    GFX2D_BUFFER *source,
    GFX2D_RECTANGLE *source_rectangle);

// *****************************************************************************
// *****************************************************************************
// Section: Functions
// *****************************************************************************
// *****************************************************************************

GFX_Result driverGfx2DInfoGet(GFX_DriverInfo* info);
GFX_Result driverGfx2DContextInitialize(GFX_Context* context);

#ifdef __cplusplus
    }
#endif
    
#endif // #ifndef _DRV_GFX_GFX2D_H
/*******************************************************************************
 End of File
*/
