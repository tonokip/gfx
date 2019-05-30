
 /*******************************************************************************
  SYS CLK Static Functions for Clock System Service

  Company:
    Microchip Technology Inc.

  File Name:
    plib_clk.c.ftl

  Summary:
    SYS CLK static function implementations for the Clock System Service.

  Description:
    The Clock System Service provides a simple interface to manage the oscillators
    on Microchip microcontrollers. This file defines the static implementation for the
    Clock System Service.

  Remarks:
    Static functions incorporate all system clock configuration settings as
    determined by the user via the Microchip Harmony Configurator GUI.  It provides
    static version of the routines, eliminating the need for an object ID or
    object handle.

    Static single-open interfaces also eliminate the need for the open handle.
*******************************************************************************/
// *****************************************************************************
// *****************************************************************************
// Section: Include Files
// *****************************************************************************
// *****************************************************************************

#include "device.h"
#include "plib_clk.h"

// *****************************************************************************
// *****************************************************************************
// Section: File Scope Functions
// *****************************************************************************
// *****************************************************************************


// *****************************************************************************
/* Function:
    void CLK_Initialize ( void )

  Summary:
    Initializes hardware and internal data structure of the System Clock.

  Description:
    This function initializes the hardware and internal data structure of System
    Clock Service.

  Remarks:
    This is configuration values for the static version of the Clock System Service
    module is determined by the user via the Microchip Harmony Configurator GUI.

    The objective is to eliminate the user's need to be knowledgeable in the function of
    the 'configuration bits' to configure the system oscillators.
*/

void CLK_Initialize( void )
{
    bool int_flag = false;

    int_flag = (bool)__builtin_disable_interrupts();
    /* unlock system for clock configuration */
    SYSKEY = 0x00000000;
    SYSKEY = 0xAA996655;
    SYSKEY = 0x556699AA;
    if (int_flag)
    {
        __builtin_mtc0(12, 0,(__builtin_mfc0(12, 0) | 0x0001)); /* enable interrupts */
    }

    OSCCONbits.FRCDIV = 0;




    /* Set up Reference Clock 5 */
    /* REFO5CON register */
    /* ROSEL =  SYSCLK */
    /* DIVSWEN = 1 */
    /* RODIV = 0 */
    REFO5CON = 0x200;
    /* REFO5TRIM register */
    /* ROTRIM = 0 */
    REFO5TRIM = 0x0;
    /* Enable oscillator (ON bit) */
    REFO5CONSET = 0x00008000;


    /* CFGMPLL */
    /* MPLLDIS = DISABLED */
    /* MPLLODIV2 = DIV_7 */
    /* MPLLODIV1 = DIV_7 */
    /* MPLLVREGDIS = DISABLED */
    /* MPLLMULT = MUL_160 */
    /* INTVREFCON = INTERNAL_DDRV */
    /* MPLLIDIV = DIV_63 */
    CFGMPLL = 0x7f40ffff;
  
    /* Lock system since done with clock configuration */
    int_flag = (bool)__builtin_disable_interrupts();
    SYSKEY = 0x33333333;
    if (int_flag) /* if interrupts originally were enabled, re-enable them */
    {
        __builtin_mtc0(12, 0,(__builtin_mfc0(12, 0) | 0x0001));
    }
}




