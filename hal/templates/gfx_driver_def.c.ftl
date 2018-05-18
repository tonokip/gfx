#include "gfx/hal/inc/gfx_driver_interface.h"

<#if DriverInfoFunction?has_content>
GFX_Result ${DriverInfoFunction}(GFX_DriverInfo* info);
GFX_Result ${DriverInitFunction}(GFX_Context* context);
</#if>

GFX_Result GFX_InitializeDriverList()
{
<#if DriverInfoFunction?has_content>
    GFX_DriverInterfaces[0].infoGet = &${DriverInfoFunction};
    GFX_DriverInterfaces[0].contextInitialize = &${DriverInitFunction};
<#else>
    # error "No gfx display drivers have been configured."
</#if>

    return GFX_SUCCESS;
}