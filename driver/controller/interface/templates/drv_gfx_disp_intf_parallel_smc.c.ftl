/*******************************************************************************
  MPLAB Harmony Generated Driver Implementation File

  File Name:
    drv_gfx_intf_spi4.c

  Summary:
    Implements the parallel display interface driver over SMC

  Description:
    Implements the parallel display interface driver over SMC

    Created with MPLAB Harmony Version 3.0
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

SOFTWARE AND DOCUMENTATION ARE PROVIDED AS IS WITHOUT WARRANTY OF ANY KIND,
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

#include "definitions.h"

#include "gfx/hal/inc/gfx_common.h"
#include "gfx/hal/inc/gfx_context.h"
#include "drv_gfx_disp_intf.h"

// This is the base address of the SMC0 peripheral on V71.
// Update to appropriate base address for other MCUs.

#define EBI_CS_INDEX  ${EBIChipSelectIndex}

<#if EBIChipSelectIndex == 0>
#define EBI_BASE_ADDR  EBI_CS0_ADDR
<#elseif EBIChipSelectIndex == 1>
#define EBI_BASE_ADDR  EBI_CS1_ADDR
<#elseif EBIChipSelectIndex == 2>
#define EBI_BASE_ADDR  EBI_CS2_ADDR
<#elseif EBIChipSelectIndex == 3>
#define EBI_BASE_ADDR  EBI_CS3_ADDR
</#if> 

// Use Address bit ${DCXAddressBit} as DCX
// This lets set set DCX = 1 by writing the data/params to ILI9488_DBIB_DATA_ADDR
#define GFX_DISP_INTF_SMC_DATA_ADDR  (EBI_BASE_ADDR | (1 << ${DCXAddressBit}))
#define GFX_DISP_INTF_SMC_CMD_ADDR EBI_BASE_ADDR

<#if ParallelInterfaceWidth == "16-bit">
// Data width for 16-bit SMC
typedef uint16_t DBUS_WIDTH_T;
</#if>
<#if ParallelInterfaceWidth == "8-bit">
// Data width for 8-bit SMC
typedef uint8_t DBUS_WIDTH_T;
</#if>

/** GFX_DISP_INTF_SMC

  Summary:
    Structure contains status and handles for SPI interface.
    
 */
typedef struct
{
    /* The GFX HAL context */
    GFX_Context * gfx;
    
    /* Address to write commands */
    volatile DBUS_WIDTH_T * cmdAddr;
    
    /* Address to write data/parameters */
    volatile DBUS_WIDTH_T * dataAddr;
} GFX_DISP_INTF_SMC;

/** GFX_Disp_Intf_Sync

  Function:
    static inline void GFX_Disp_Intf_Sync(void)

  Summary:
    Add synchronization for core writes to the SMC

 */
static inline void GFX_Disp_Intf_Sync(void)
{
    __ASM volatile ("dsb");
    __ASM volatile ("dmb");
}

GFX_Disp_Intf GFX_Disp_Intf_Open(GFX_Context * gfx, unsigned int index)
{   
    GFX_DISP_INTF_SMC * intf = NULL;
    
    if (gfx == NULL)
        return 0;
    
    intf = (GFX_DISP_INTF_SMC *) gfx->memory.calloc(1, sizeof (GFX_DISP_INTF_SMC));
    
    if (intf == NULL)
        return 0;
    
    intf->dataAddr = (DBUS_WIDTH_T *) GFX_DISP_INTF_SMC_DATA_ADDR;
    intf->cmdAddr = (DBUS_WIDTH_T *) GFX_DISP_INTF_SMC_CMD_ADDR;
    
    intf->gfx = gfx;

    return (GFX_Disp_Intf) intf;
}

void GFX_Disp_Intf_Close(GFX_Disp_Intf intf)
{
    if (((GFX_DISP_INTF_SMC *) intf) == NULL)
        return;

    ((GFX_DISP_INTF_SMC *) intf)->gfx->memory.free(((GFX_DISP_INTF_SMC *) intf));
}

GFX_Result GFX_Disp_Intf_PinControl(GFX_Disp_Intf intf, GFX_DISP_INTF_PIN pin, GFX_DISP_INTF_PIN_VALUE value)
{
    GFX_Result res = GFX_FAILURE;
    
    if (((GFX_DISP_INTF_SMC *) intf) == NULL)
        return GFX_FAILURE;
    
    switch(pin)
    {
        case GFX_DISP_INTF_PIN_CS:
#ifdef GFX_DISP_INTF_PIN_CS_Set
            if (value == GFX_DISP_INTF_PIN_CLEAR)
                GFX_DISP_INTF_PIN_CS_Clear();
            else
                GFX_DISP_INTF_PIN_CS_Set();
            
            res = GFX_SUCCESS;
#endif
            break;
        case GFX_DISP_INTF_PIN_WR:
#ifdef GFX_DISP_INTF_PIN_WR_Set
            if (value == GFX_DISP_INTF_PIN_CLEAR)
                GFX_DISP_INTF_PIN_WR_Clear();
            else
                GFX_DISP_INTF_PIN_WR_Set();

            res = GFX_SUCCESS;            
#endif
            break;
        case GFX_DISP_INTF_PIN_RD:
#ifdef GFX_DISP_INTF_PIN_RD_Set
            if (value == GFX_DISP_INTF_PIN_CLEAR)
                GFX_DISP_INTF_PIN_RD_Clear();
            else
                GFX_DISP_INTF_PIN_RD_Set();
            
            res = GFX_SUCCESS;
#endif
            break;
        case GFX_DISP_INTF_PIN_RSDC:
#ifdef GFX_DISP_INTF_PIN_RSDC_Set
            if (value == GFX_DISP_INTF_PIN_CLEAR)
                GFX_DISP_INTF_PIN_RSDC_Clear();
            else
                GFX_DISP_INTF_PIN_RSDC_Set();
            
            res = GFX_SUCCESS;
#endif            
            break;
        default:
            break;
    }
    
    return res;
}

GFX_Result GFX_Disp_Intf_WriteCommand(GFX_Disp_Intf intf, uint8_t cmd)
{
    GFX_DISP_INTF_SMC * smcIntf = (GFX_DISP_INTF_SMC *) intf;
    
    if (smcIntf == NULL)
        return GFX_FAILURE;

    GFX_Disp_Intf_Sync();  
    *(smcIntf->cmdAddr) = cmd ;
    GFX_Disp_Intf_Sync();
    
    return GFX_SUCCESS;
}

GFX_Result GFX_Disp_Intf_WriteData(GFX_Disp_Intf intf, uint8_t * data, int bytes)
{
    GFX_DISP_INTF_SMC * smcIntf = (GFX_DISP_INTF_SMC *) intf;
    unsigned int i;
    
    if (smcIntf == NULL ||
        data == NULL ||
        bytes == 0)
        return GFX_FAILURE;

    GFX_Disp_Intf_Sync();
    
    for (i = 0; i < bytes; i++)
    {
        *(smcIntf->dataAddr) = *(data);
        data++;
        GFX_Disp_Intf_Sync();  
    }
    
    return GFX_SUCCESS;
}

GFX_Result GFX_Disp_Intf_WriteData16(GFX_Disp_Intf intf, uint16_t * data, int num)
{
    GFX_DISP_INTF_SMC * smcIntf = (GFX_DISP_INTF_SMC *) intf;
    unsigned int i;
    
    if ((smcIntf) == NULL ||
        data == NULL ||
        num == 0)
        return GFX_FAILURE;

    GFX_Disp_Intf_Sync();
    
    for (i = 0; i < num; i++)
    {
        *(smcIntf->dataAddr) = *(data);
        data++;
        GFX_Disp_Intf_Sync();  
    }
    
    return GFX_SUCCESS;
}

GFX_Result GFX_Disp_Intf_ReadData16(GFX_Disp_Intf intf, uint16_t * data, int num)
{
    GFX_DISP_INTF_SMC * smcIntf = (GFX_DISP_INTF_SMC *) intf;
    unsigned int i;
    
    if (smcIntf == NULL ||
        num == 0 ||
        data == NULL)
        return GFX_FAILURE;
    
    GFX_Disp_Intf_Sync();
    
    for (i = 0; i < num; i++)
    {
        *data = *(smcIntf->dataAddr); 
        data++;
    }
    
    return GFX_SUCCESS;
}

GFX_Result GFX_Disp_Intf_ReadData(GFX_Disp_Intf intf, uint8_t * data, int bytes)
{
    GFX_DISP_INTF_SMC * smcIntf = (GFX_DISP_INTF_SMC *) intf;
    unsigned int i;
    
    if (smcIntf == NULL ||
        bytes == 0 ||
        data == NULL)
        return GFX_FAILURE;
    
    GFX_Disp_Intf_Sync();
    
    for (i = 0; i < bytes; i++)
    {
        *data = *(smcIntf->dataAddr); 
        data++;
    }
    
    return GFX_SUCCESS;
}

GFX_Result GFX_Disp_Intf_WriteCommandParm(GFX_Disp_Intf intf, uint8_t cmd, uint8_t * parm, int num_parms)
{
    GFX_Result retval;
    GFX_DISP_INTF_SMC * smcIntf;
    unsigned int i;
    
    retval = GFX_Disp_Intf_WriteCommand(intf, cmd);
    if (retval != GFX_SUCCESS)
        return GFX_FAILURE;
    
    if (num_parms > 0 && parm != NULL)
    {
        smcIntf = (GFX_DISP_INTF_SMC *) intf;
        
        for (i = 0; i < num_parms; i++)
        {
            *(smcIntf->dataAddr) = *(parm);
            parm++;
            GFX_Disp_Intf_Sync();  
        }
    }

    return retval;
}

GFX_Result GFX_Disp_Intf_Write(GFX_Disp_Intf intf, uint8_t * data, int bytes)
{
    GFX_DISP_INTF_SMC * smcIntf;
    unsigned int i;
    
    if (((GFX_DISP_INTF_SMC *) intf) == NULL ||
        data == NULL ||
        bytes == 0)
        return GFX_FAILURE;

    smcIntf = (GFX_DISP_INTF_SMC *) intf;
    
    GFX_Disp_Intf_Sync();
    
    for (i = 0; i < bytes; i++)
    {
        *(smcIntf->cmdAddr) = *(data);
        data++;
        GFX_Disp_Intf_Sync();  
    }
    
    return GFX_SUCCESS;
}

GFX_Result GFX_Disp_Intf_Read(GFX_Disp_Intf intf, uint8_t * data, int bytes)
{
    GFX_DISP_INTF_SMC * smcIntf = (GFX_DISP_INTF_SMC *) intf;
    unsigned int i;
    
    if (smcIntf == NULL ||
        bytes == 0 ||
        data == NULL)
        return GFX_FAILURE;
    
    GFX_Disp_Intf_Sync();
    
    for (i = 0; i < bytes; i++)
    {
        *(data + i) = *(smcIntf->cmdAddr); 
    }
    
    return GFX_SUCCESS;
}


/* *****************************************************************************
 End of File
 */
