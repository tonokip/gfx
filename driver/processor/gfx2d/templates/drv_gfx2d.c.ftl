/********************************************************************************
  GFX GFX2D Driver Functions

  Company:
    Microchip Technology Inc.

  File Name:
    drv_glcd.c

  Summary:
    Source code for the GFX GFX2D driver static implementation.

  Description:
    This file contains the source code for the static implementation of the
    GFX GFX2D driver.
*******************************************************************************/

//DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2019 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute Software
only when embedded on a Microchip microcontroller or digital  signal  controller
that is integrated into your product or third party  product  (pursuant  to  the
sublicense terms in the accompanying license agreement).

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

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include "gfx/driver/processor/gfx2d/drv_gfx2d.h"
#include "definitions.h"

// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* GFX2D Driver Instance Object

  Summary:
    Object used to keep any data required for an instance of the GFX2D driver.

  Description:
    None.

  Remarks:
    None.
*/

typedef struct
{
    /* Flag to indicate this object is in use  */
    bool inUse;

    /* Flag to indicate that driver has been opened Exclusively*/
    bool isExclusive;

    /* The status of the driver */
    SYS_STATUS status;

    /* PLIB API list that will be used by the driver to access the hardware */
    const DRV_GFX2D_PLIB_INTERFACE* gfx2DPlib;

    /* Interrupt Source of GFX2D */
    //IRQn_Type interruptGFX2D;

} DRV_GFX2D_OBJ;

/* This is the driver instance object array. */
static DRV_GFX2D_OBJ gDrvGFX2DObj;

const char* DRIVER_GFX2D_NAME = "GFX2D";

//static int DRV_GFX2D_Start();

// function that returns the information for this driver
GFX_Result driverGFX2DInfoGet(GFX_DriverInfo* info)
{
    if(info == NULL)
    return GFX_FAILURE;

    // populate info struct
    strcpy(info->name, DRIVER_GFX2D_NAME);

    return GFX_SUCCESS;
}

//static GFX_Result gfx2DUpdate()
//{
//    GFX_Context* context = GFX_ActiveContext();
//
//    if(context == NULL)
//        return GFX_FAILURE;
//
//    if(state == INIT)
//    {
//        if(DRV_GFX2D_Start() != 0)
//            return GFX_FAILURE;
//
//        state = RUN;
//    }
//
//    return GFX_SUCCESS;
//}

//static void gfx2DDestroy(GFX_Context* context)
//{
//    // driver specific shutdown tasks
//    if(context->driver_data != GFX_NULL)
//    {
//        context->memory.free(context->driver_data);
//        context->driver_data = GFX_NULL;
//    }
//
//    // general default shutdown
//    defDestroy(context);
//}

//static GFX_Result gfx2DInitialize(GFX_Context* context)
//{
//    // general default initialization
//    if(defInitialize(context) == GFX_FAILURE)
//            return GFX_FAILURE;
//
//    /* gfx2D initialization */
//
//    return GFX_SUCCESS;
//}

// function that initialized the driver context
GFX_Result driverGfx2DContextInitialize(GFX_Context* context)
{

    return GFX_SUCCESS;
}

/*
void __ISR(_GLCD_VECTOR, ipl1AUTO) _IntHandlerVSync(void)
{
    uint32_t i;
    GFX_Context* context = GFX_ActiveContext();
    
	// disable vsync interrupt
    PLIB_GLCD_VSyncInterruptDisable(GLCD_ID_0); 
	
	// clear interrupt flag
    PLIB_INT_SourceFlagClear(INT_ID_0, INT_SOURCE_GLCD);
}
*/

/**** End Hardware Abstraction Interfaces ****/


//static int DRV_GFX2D_Start()
//{
//    return 0;
//}


SYS_MODULE_OBJ DRV_GFX2D_Initialize( const SYS_MODULE_INDEX drvIndex, const SYS_MODULE_INIT * const init )
{
    DRV_GFX2D_OBJ* dObj     = (DRV_GFX2D_OBJ*)NULL;
    DRV_GFX2D_INIT* gfx2DInit = (DRV_GFX2D_INIT*)init;

    if(gDrvGFX2DObj.status == SYS_STATUS_READY)
    {
        SYS_DEBUG(SYS_ERROR_ERROR, "Instance already initialized");
        return SYS_MODULE_OBJ_INVALID;
    }

    /* Allocate the driver object */
    dObj = &gDrvGFX2DObj;
    dObj->inUse = true;

    /* Update the driver parameters */
    dObj->gfx2DPlib                     = gfx2DInit->gfx2DPlib;

    /* Register a callback with PLIB.
     * dObj as a context parameter will be used to distinguish the events
     * from different instances. */
    //dObj->gfx2DPlib->callbackRegister(_DRV_GFX2D_PLibCallbackHandler, (uintptr_t)dObj);

    /* Update the status */
    dObj->status = SYS_STATUS_READY;

    /* Return the object structure */
    return ( (SYS_MODULE_OBJ)drvIndex );
}

/*******************************************************************************
 End of File
*/
