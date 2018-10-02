/*******************************************************************************
  SPI PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_spi0.c

  Summary:
    SPI0 Source File

  Description:
    This file has implementation of all the interfaces provided for particular
    SPI peripheral.

*******************************************************************************/

/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

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

#include "plib_spi0.h"

// *****************************************************************************
// *****************************************************************************
// Section: SPI0 Implementation
// *****************************************************************************
// *****************************************************************************
/* Global object to save SPI Exchange related data */
SPI_OBJECT spi0Obj;

void SPI0_Initialize ( void )
{
    /* Disable and Reset the SPI*/
    SPI0_REGS->SPI_CR = SPI_CR_SPIDIS_Msk | SPI_CR_SWRST_Msk;

    /* Enable Master mode, select particular NPCS line for chip select and disable mode fault detection */
    SPI0_REGS->SPI_MR =  SPI_MR_MSTR_Msk | SPI_MR_PCS_NPCS0 | SPI_MR_MODFDIS_Msk;

    /* Set up clock Polarity, data phase, Communication Width and Baud Rate */
    SPI0_REGS->SPI_CSR[0] = SPI_CSR_CPOL_IDLE_LOW | SPI_CSR_NCPHA_VALID_LEADING_EDGE | SPI_CSR_BITS_8_BIT | SPI_CSR_SCBR(7);

    /* Initialize global variables */
    spi0Obj.transferIsBusy = false;
    spi0Obj.callback = NULL;
    spi0Obj.status = SPI_ERROR_NONE;

    /* Enable SPI0 */
    SPI0_REGS->SPI_CR = SPI_CR_SPIEN_Msk;
    return;
}

bool SPI0_WriteRead (void* pTransmitData, size_t txSize, void* pReceiveData, size_t rxSize)
{
    bool isRequestAccepted = false;
    uint32_t dummyData;

    /* Verify the request */
    if((((txSize > 0) && (pTransmitData != NULL)) || ((rxSize > 0) && (pReceiveData != NULL))) && (spi0Obj.transferIsBusy == false))
    {
        isRequestAccepted = true;
        spi0Obj.txBuffer = pTransmitData;
        spi0Obj.rxBuffer = pReceiveData;
        spi0Obj.rxCount = 0;
        spi0Obj.txCount = 0;
        spi0Obj.dummySize = 0;
        if (pTransmitData != NULL)
        {
            spi0Obj.txSize = txSize;
        }
        else
        {
            spi0Obj.txSize = 0;
        }

        if (pReceiveData != NULL)
        {
            spi0Obj.rxSize = rxSize;
        }
        else
        {
            spi0Obj.rxSize = 0;
        }

        spi0Obj.transferIsBusy = true;
        spi0Obj.status = SPI_ERROR_NONE;

        /* Flush out any unread data in SPI read buffer */
        dummyData = (SPI0_REGS->SPI_RDR & SPI_RDR_RD_Msk) >> SPI_RDR_RD_Pos;
        (void)dummyData;

        if (spi0Obj.rxSize > spi0Obj.txSize)
        {
            spi0Obj.dummySize = spi0Obj.rxSize - spi0Obj.txSize;
        }

        /* Start the first write here itself, rest will happen in ISR context */
        if((SPI0_REGS->SPI_CSR[0] & SPI_CSR_BITS_Msk) == SPI_CSR_BITS_8_BIT)
        {
            if (spi0Obj.txCount < spi0Obj.txSize)
            {
                SPI0_REGS->SPI_TDR = *((uint8_t*)spi0Obj.txBuffer);
                spi0Obj.txCount++;
            }
            else if (spi0Obj.dummySize > 0)
            {
                SPI0_REGS->SPI_TDR = (uint8_t)(0xff);
                spi0Obj.dummySize--;
            }
        }
        else
        {
            spi0Obj.txSize >>= 1;
            spi0Obj.dummySize >>= 1;
            spi0Obj.rxSize >>= 1;

            if (spi0Obj.txCount < spi0Obj.txSize)
            {
                SPI0_REGS->SPI_TDR = *((uint16_t*)spi0Obj.txBuffer);
                spi0Obj.txCount++;
            }
            else if (spi0Obj.dummySize > 0)
            {
                SPI0_REGS->SPI_TDR = (uint16_t)(0xff);
                spi0Obj.dummySize--;
            }
        }

        if (rxSize > 0)
        {
            /* Enable receive interrupt to complete the transfer in ISR context */
            SPI0_REGS->SPI_IER = SPI_IER_RDRF_Msk;
        }
        else
        {
            /* Enable transmit interrupt to complete the transfer in ISR context */
            SPI0_REGS->SPI_IER = SPI_IER_TDRE_Msk;
        }
    }

    return isRequestAccepted;
}

bool SPI0_TransferSetup (SPI_TRANSFER_SETUP * setup, uint32_t spiSourceClock )
{
    uint32_t scbr;
    if ((setup == NULL) || (setup->clockFrequency == 0))
	{
		return false;
	}
    if(spiSourceClock == 0)
    {
        // Fetch Master Clock Frequency directly
        spiSourceClock = 150000000;
    }

    scbr = spiSourceClock/setup->clockFrequency;

    if(scbr == 0)
    {
        scbr = 1;
    }
    else if(scbr > 255)
    {
        scbr = 255;
    }

    SPI0_REGS->SPI_CSR[0]= setup->clockPolarity | setup->clockPhase | SPI_CSR_BITS(setup->dataBits) | SPI_CSR_SCBR(scbr);

    return true;
}

SPI_ERROR SPI0_ErrorGet ( void )
{
    return (SPI_ERROR)(spi0Obj.status & (SPI_SR_OVRES_Msk));
}

void SPI0_CallbackRegister (SPI_CALLBACK callback, uintptr_t context)
{
    spi0Obj.callback = callback;
    spi0Obj.context = context;
}

bool SPI0_IsBusy()
{
    return spi0Obj.transferIsBusy;
}

void SPI0_InterruptHandler(void)
{
    uint32_t dataBits ;
    uint32_t receivedData;
    dataBits = SPI0_REGS->SPI_CSR[0] & SPI_CSR_BITS_Msk;

    /* save the status in global object before it gets cleared */
    spi0Obj.status = SPI0_REGS->SPI_SR;

    if ((SPI0_REGS->SPI_SR & SPI_SR_RDRF_Msk ) == SPI_SR_RDRF_Msk)
    {
        receivedData = (SPI0_REGS->SPI_RDR & SPI_RDR_RD_Msk) >> SPI_RDR_RD_Pos;

        if (spi0Obj.rxCount < spi0Obj.rxSize)
        {
            if(dataBits == SPI_CSR_BITS_8_BIT)
            {
                ((uint8_t*)spi0Obj.rxBuffer)[spi0Obj.rxCount++] = receivedData;
            }
            else
            {
                ((uint16_t*)spi0Obj.rxBuffer)[spi0Obj.rxCount++] = receivedData;
            }
        }
    }

    /* If there are more words to be transmitted, then transmit them here and keep track of the count */
    if((SPI0_REGS->SPI_SR & SPI_SR_TDRE_Msk) == SPI_SR_TDRE_Msk)
    {
        if(dataBits == SPI_CSR_BITS_8_BIT)
        {
            if (spi0Obj.txCount < spi0Obj.txSize)
            {
                SPI0_REGS->SPI_TDR = ((uint8_t*)spi0Obj.txBuffer)[spi0Obj.txCount++];
            }
            else if (spi0Obj.dummySize > 0)
            {
                SPI0_REGS->SPI_TDR = (uint8_t)(0xff);
                spi0Obj.dummySize--;
            }
        }
        else
        {
            if (spi0Obj.txCount < spi0Obj.txSize)
            {
                SPI0_REGS->SPI_TDR = ((uint16_t*)spi0Obj.txBuffer)[spi0Obj.txCount++];
            }
            else if (spi0Obj.dummySize > 0)
            {
                SPI0_REGS->SPI_TDR = (uint16_t)(0xff);
                spi0Obj.dummySize--;
            }
        }
        if ((spi0Obj.txCount == spi0Obj.txSize) && (spi0Obj.dummySize == 0))
        {
            /* Disable the TDRE interrupt and enable TXEMPTY interrupt to ensure
             * no data is present in the shift register before CS is de-selected
             */
            SPI0_REGS->SPI_IDR = SPI_IDR_TDRE_Msk;
            SPI0_REGS->SPI_IER = SPI_IER_TXEMPTY_Msk;
        }
    }

    /* See if Exchange is complete */
    if (((SPI0_REGS->SPI_IMR & SPI_IMR_TXEMPTY_Msk) == SPI_IMR_TXEMPTY_Msk) && ((SPI0_REGS->SPI_SR & SPI_SR_TXEMPTY_Msk) == SPI_SR_TXEMPTY_Msk))
    {
        if (spi0Obj.rxCount == spi0Obj.rxSize)
        {
            spi0Obj.transferIsBusy = false;

            /* Disable TDRE, RDRF and TXEMPTY interrupts */
            SPI0_REGS->SPI_IDR = SPI_IDR_TDRE_Msk | SPI_IDR_RDRF_Msk | SPI_IDR_TXEMPTY_Msk;

            /* Flush out any pending SPI IRQ with NVIC */
            NVIC_ClearPendingIRQ(SPI0_IRQn);

            /* If it was only transmit, then ignore receiver overflow error, if any */
            if(spi0Obj.rxSize == 0)
            {
                spi0Obj.status = SPI_ERROR_NONE;
            }

            if(spi0Obj.callback != NULL)
            {
                spi0Obj.callback(spi0Obj.context);
            }
        }
    }
}


/*******************************************************************************
 End of File
*/

