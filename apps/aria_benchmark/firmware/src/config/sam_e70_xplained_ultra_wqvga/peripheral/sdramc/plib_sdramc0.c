/*****************************************************************************
  Company:
    Microchip Technology Inc.

  File Name:
    plib_sdramc0.c

  Summary:
    SDRAMC PLIB Source file

  Description:
    None

*******************************************************************************/

/*******************************************************************************
Copyright (c) 2017-18 released Microchip Technology Inc.  All rights reserved.

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
#include "plib_sdramc0.h"
#include "device.h"

// *****************************************************************************
// *****************************************************************************
// Section: SDRAMC Implementation
// *****************************************************************************
// *****************************************************************************
void SW_DelayUs(uint32_t delay)
{
    uint32_t i, count;

    /* delay * (CPU_FREQ/1000000) / 6 */
    count = delay *  (300000000/1000000)/6;

    /* 6 CPU cycles per iteration */
    for (i = 0; i < count; i++)
        __NOP();
}

void SDRAMC0_Initialize( void )
{
    uint8_t i;
    uint16_t *pSdramBaseAddress = (uint16_t *)SDRAM_CS_ADDR;

    /* Enable the SDRAMC Chip Select */
    MATRIX_REGS->CCFG_SMCNFCS|= (1 << CCFG_SMCNFCS_SDRAMEN_Pos);

    /* Step 1:
     * Configure SDRAM features and timing parameters */
    SDRAMC_REGS->SDRAMC_CR = SDRAMC_CR_NC_COL8 | SDRAMC_CR_NR_ROW11 | SDRAMC_CR_NB_BANK2 | SDRAMC_CR_DBW_Msk \
                                | SDRAMC_CR_TRAS(6) |  SDRAMC_CR_TRP(3) |  SDRAMC_CR_TRC_TRFC(9) \
                                | SDRAMC_CR_TRCD(3) | SDRAMC_CR_CAS(3) | SDRAMC_CR_TWR(2) | SDRAMC_CR_TXSR(10);

    SDRAMC_REGS->SDRAMC_CFR1= SDRAMC_CFR1_TMRD(2) | SDRAMC_CFR1_UNAL_Msk;

    /* Step 2:
     * For mobile SDRAM, temperature-compensated self refresh (TCSR), drive strength (DS) and partial array
     * self refresh (PASR) must be set in the Low Power Register. */
    SDRAMC_REGS->SDRAMC_LPR=0;

    /* Step 3:
     * Select the SDRAM memory device type. */
     SDRAMC_REGS->SDRAMC_MDR = SDRAMC_MDR_MD_SDRAM;


    /* Step 4:
     * A pause of at least 200 us must be observed before a signal toggle */
    SW_DelayUs(200);

    /* Step 5:
     * Issue a NOP command to the SDRAM device by writing to the Mode Register.
     * Read back the Mode Register and add a memory barrier assembly instruction just after the read.
     * Write to any SDRAM address to acknowledge this command. Now the clock which drives SDRAM device is enabled */

    SDRAMC_REGS->SDRAMC_MR = SDRAMC_MR_MODE_NOP;
    SDRAMC_REGS->SDRAMC_MR;
    __DMB();
    *pSdramBaseAddress = 0x0;

    /* Step 6:
     * Issue an All banks precharge command by writing to the Mode Register.
     * Read back the Mode Register and add a memory barrier assembly instruction just after the read.
     * Write to any SDRAM address to acknowledge this command. */

    SDRAMC_REGS->SDRAMC_MR = SDRAMC_MR_MODE_ALLBANKS_PRECHARGE;
    SDRAMC_REGS->SDRAMC_MR;
    __DMB();
    *pSdramBaseAddress = 0x0;

    /* Step 7:
     * Issue 8 Auto Refresh(CBR) cycles by writing to the Mode Register.
     * Read back the Mode Register and add a memory barrier assembly instruction just after the read.
     * Perform a write access to any SDRAM address 8 times. */
    SDRAMC_REGS->SDRAMC_MR = SDRAMC_MR_MODE_AUTO_REFRESH;
    SDRAMC_REGS->SDRAMC_MR;
    __DMB();
    for (i = 0; i < 8; i++)
    {
        *pSdramBaseAddress = i;
    }

    /* Step 8:
     * Issue Mode Register Set(MRS) to program the parameters of the SDRAM device, in particular CAS latency and burst length */
    SDRAMC_REGS->SDRAMC_MR = SDRAMC_MR_MODE_LOAD_MODEREG;
    SDRAMC_REGS->SDRAMC_MR;
    __DMB();
    *((uint16_t *)(pSdramBaseAddress + 0x30)) = 0;

    /* Step 9:
     * Issue Extended Mode Register Set(EMRS) for mobile SDRAM to
     * program the parameters of the SDRAM(TCSR, PASR, DS). Read back the Mode
     * Register and add a memory barrier assembly instruction just after the
     * read. Perform a write access to the SDRAM. The address must be chosen
     * such that BA[1] or BA[0] are set to one. */
//    SDRAMC_REGS->SDRAMC_MR = SDRAMC_MR_MODE_EXT_LOAD_MODEREG;
//    SDRAMC_REGS->SDRAMC_MR;
//   __DMB();
//    *((uint16_t *)(pSdramBaseAddress + 22)) = 0;

    /* Step 10:
     * Transition the SDRAM to NORMAL mode. Read back the Mode
     * Register and add a memory barrier assembly instruction just after the
     * read. Perform a write access to any SDRAM address. */
    SDRAMC_REGS->SDRAMC_MR = SDRAMC_MR_MODE_NORMAL;
    SDRAMC_REGS->SDRAMC_MR;
    __DMB();
    *pSdramBaseAddress = 0x0;

    /* Step 11:
     * Configure the Refresh Timer Register. */
    SDRAMC_REGS->SDRAMC_TR = 2343;

} /* SDRAMC0_Initialize */
/*******************************************************************************
 End of File
*/
