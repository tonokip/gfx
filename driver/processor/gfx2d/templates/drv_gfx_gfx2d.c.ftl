/********************************************************************************
  GFX GLCD Driver Functions for Static Single Instance Driver

  Company:
    Microchip Technology Inc.

  File Name:
    drv_gfx_glcd.c

  Summary:
    Source code for the GFX GLCD driver static implementation.

  Description:
    This file contains the source code for the static implementation of the
    GFX GLCD driver.
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

#include "gfx/driver/processor/gfx2d/drv_gfx_gfx2d.h"
#include "definitions.h"

// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************


const char* DRIVER_NAME = "GFX2D";

static int DRV_GFX_GLCD_Start();

// function that returns the information for this driver
GFX_Result driverGFX2DInfoGet(GFX_DriverInfo* info)
{
    if(info == NULL)
    return GFX_FAILURE;

    // populate info struct
    strcpy(info->name, DRIVER_NAME);

    return GFX_SUCCESS;
}

static GFX_Result gfx2dUpdate()
{
    GFX_Context* context = GFX_ActiveContext();

    if(context == NULL)
        return GFX_FAILURE;

    if(state == INIT)
    {
        if(DRV_GFX_GFX2D_Start() != 0)
            return GFX_FAILURE;

        state = RUN;
    }

    return GFX_SUCCESS;
}

static void gfx2dDestroy(GFX_Context* context)
{
    // driver specific shutdown tasks
    if(context->driver_data != GFX_NULL)
    {
        context->memory.free(context->driver_data);
        context->driver_data = GFX_NULL;
    }

    // general default shutdown
    defDestroy(context);
}

static GFX_Result glcdInitialize(GFX_Context* context)
{
    cntxt = context;

    // general default initialization
    if(defInitialize(context) == GFX_FAILURE)
            return GFX_FAILURE;

    /* glcd initialization */
    PLIB_GLCD_Enable(GLCD_ID_0);   
	
    SYS_INT_VectorPrioritySet(INT_VECTOR_GLCD, INT_PRIORITY_LEVEL1);
    SYS_INT_VectorSubprioritySet(INT_VECTOR_GLCD, INT_SUBPRIORITY_LEVEL0);
    SYS_INT_SourceStatusClear(INT_SOURCE_GLCD);
    SYS_INT_SourceEnable(INT_SOURCE_GLCD);

    return GFX_SUCCESS;
}

// function that initialized the driver context
GFX_Result driverGLCDContextInitialize(GFX_Context* context)
{
    // set driver-specific data initialization function address
    context->hal.initialize = &glcdInitialize;

    // set driver-specific destroy function address
    context->hal.destroy = &glcdDestroy;

    // vsync support
    context->hal.layerSwapPending = &layerSwapPending;

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


static int DRV_GFX_GLCD_Start()
{
    return 0;
}

/*******************************************************************************
 End of File
*/
