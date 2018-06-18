#include "gfx/hal/inc/gfx_processor_interface.h"

<#if ProcInfoFunction?has_content>
GFX_Result ${ProcInfoFunction}(GFX_ProcessorInfo* info);
GFX_Result ${ProcInitFunction}(GFX_Context* context);

</#if>
GFX_Result GFX_InitializeProcessorList()
{
<#if ProcInfoFunction?has_content>
    GFX_ProcessorInterfaces[0].infoGet = &${ProcInfoFunction};
    GFX_ProcessorInterfaces[0].contextInitialize = &${ProcInitFunction};

</#if>
    return GFX_SUCCESS;
}