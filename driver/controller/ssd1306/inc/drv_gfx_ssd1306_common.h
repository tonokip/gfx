/*******************************************************************************
 Module for Microchip Graphics Library - Hardware Abstraction Layer

  Company:
    Microchip Technology Inc.

  File Name:
    drv_gfx_ssd1603_common.h

  Summary:
    Contains SSD1306 driver type definitions and interface prototypes.

  Description:
    Contains SSD1306 driver type definitions and interface prototypes.
*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.
IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR
OTHER LEGAL EQUITABLE THEORY ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES
INCLUDING BUT NOT LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR
CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF
SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS.
*******************************************************************************/
// DOM-IGNORE-END

#ifndef DRV_GFX_SSD1306_COMMON_H    /* Guard against multiple inclusion */
#define DRV_GFX_SSD1306_COMMON_H

/** SSD1306_DRV_STATE

  Summary:
    Enum of SSD1306 driver states.
    
*/
typedef enum
{
    INIT = 0,
    RUN
} SSD1306_DRV_STATE;

/** SSD1306_DRVmary:
    Structure contains driver-specific data and ops pointers.
    
*/
typedef struct
{
    /* GFX context pointer */
    GFX_Context* gfx;
    
    /* Driver state */
    SSD1306_DRV_STATE state;
    
    /* interface-specific private data */
    void *port_priv;
} SSD1306_DRV;

/* Provide C++ Compatibility */
#ifdef __cplusplus
}
#endif

#endif // DRV_GFX_SSD1306_COMMON_H

/* *****************************************************************************
 End of File
 */
