#include "gfx/hal/inc/gfx_driver_interface.h"

GFX_Result driverILI9488InfoGet(GFX_DriverInfo* info);
GFX_Result driverILI9488ContextInitialize(GFX_Context* context);

GFX_Result GFX_InitializeDriverList()
{
    GFX_DriverInterfaces[0].infoGet = &driverILI9488InfoGet;
    GFX_DriverInterfaces[0].contextInitialize = &driverILI9488ContextInitialize;

    return GFX_SUCCESS;
}