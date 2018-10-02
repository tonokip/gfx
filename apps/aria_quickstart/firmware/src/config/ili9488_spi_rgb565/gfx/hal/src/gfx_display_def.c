#include "gfx/hal/inc/gfx_display.h"
#include "gfx/hal/inc/gfx_common.h"

GFX_DisplayInfo GFX_DisplayInfoList[] =
{
    {
        "ATMXT-XPRO", // description
        0, // unused
        {
			0,  // x position (always 0)
			0,  // y position (always 0)
			320,  // display width
			480, // display height
		},
		{
		    16,  // data bus width
		    {
				41,  // horizontal pulse width
				2,  // horizontal back porch
				2,  // horizontal front porch
		    },
		    {
				10,  // vertical pulse width
				2,  // vertical back porch
				2,  // vertical front porch
		    },
			0,  // inverted left shift
		},
	},
};