#include "gfx/hal/inc/gfx_display.h"
#include "gfx/hal/inc/gfx_common.h"

GFX_DisplayInfo GFX_DisplayInfoList[] =
{
    {
        "${DisplayName}", // description
        0, // unused
        {
			0,  // x position (always 0)
			0,  // y position (always 0)
			${DisplayWidth},  // display width
			${DisplayHeight}, // display height
		},
		{
		    ${DisplayDataWidth},  // data bus width
		    {
				${DisplayHorzPulseWidth},  // horizontal pulse width
				${DisplayHorzBackPorch},  // horizontal back porch
				${DisplayHorzFrontPorch},  // horizontal front porch
		    },
		    {
				${DisplayVertPulseWidth},  // vertical pulse width
				${DisplayVertBackPorch},  // vertical back porch
				${DisplayVertFrontPorch},  // vertical front porch
		    },
			<#if DisplayInvLeftShift == true>1<#else>0</#if>,  // inverted left shift
		},
	},
};