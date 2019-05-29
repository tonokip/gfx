# Microchip MPLAB® Harmony 3 Graphics Release Notes
## Graphics Release v3.3.0
### NEW FEATURES


- **Graphics Contents** - This graphics release consist of apps, displays, drivers, hardware abstractions, input, middleware, and templates. The following table lists the contents in this graphics release.

| Category | Component | Description | Release Type | 
| --- | --- | ---- |---- |
| apps | aria_quickstart | Getting started in Graphics | N/A|
| displays | ATMXT-XPRO-480x320 | ATMXT Xplained Pro 480x320| Production |
|      | ATOLED1_XPRO-128x32 | AT OLED Xplained Pro 128x32| Beta |
|      | PDA TM4301B 480x272| PDA 4.3" 480x272 | Production |
|      | PDA TM50000 800x480| PDA 5" 800x480 | Beta |
|  drivers    | glcd | Graphics 3 Layer Display Driver | Beta |
|      | ili9488| Display Driver for the ili9488 Controller |Beta | 
|      | interface | Display Driver interface driver | Production |
|      | LCC | Display Driver for the LCC software Controller| Production |
|      | LCDC | Display Driver for the LCDC Controller| Beta |
|      | ssd1306 | Display Driver for the ssd1306 Controller  | Beta |
|      | ssd1963 | Display Driver for the ssd1963 Controller |     Beta |
|  hal    | hal | Aria Hardware Abstration Layer | Production |
|  input    | maxtouch | Microchip maXTouch Touch Input Driver | Production |
|  middleware    | aria | Harmony Graphics Middleware Solution | Production |
| templates   | aria_gfx_oled1_xpro | MHC for oled xpro| Beta |
|             | aria_gfx_pda_tm4301b| MHC config for pda 4" display | Production |
|             | aria_gfx_pda_tm5000| MHC config for pda 5" display | Beta |
|             | aria_gfx_xplained_pro| MHC config for xpro | Production |
|             | common| MHC config for common board |Production |

- **Driver support** - The following table provides the list of updates for graphics and input drivers.

| Driver | Description | 
| --- | --- |
| 2DGPU (nano2D) | Added 2DGPU Nano2D Driver|
| LCC | Added support for RGB332 in LCC driver|
| LCDC | Added HAL control for LCDC backlight PWM|
| maXTouch| Fixed non-portable Nop() in drv_maxtouch.c|
| GLCD| Fixed hardcoded WVGA frame buffer size allocation GLCD|
| | Added GLCD driver and plib support|
| Interface| Improved external controller and display interface drivers|
| | Added parallel interface driver for E54|
| ILI9488| Added support for rectangular fill |
| SSD1963 | Added support for rectangular fill |

- **Middleware/HAL support** - The following table provides the list of updates for middleware and HAL content.

| Middleware/HAL | Description | 
| --- | --- |
| aria| Added pre-processing support for images in external media|
| | Added touch support for maXTouch Xplained Pro display board|
| | Fixed removal of screens and widgets during project regeneration using command line|
| | Fixed Draw Surface widget not generating custom code|
| | Fixed coded generation failure in MHC for radial menu widget|
| | Added Alpha Enable flag to HAL|
| | Fixed GLCD layer buffer swaps incorrectly|
| | Fixed alpha blending of 32bpp images|
| | Added parse to configLoad API|
| | Fixed color masking for images|

- **Graphics Application Templates** - The following table provides the list of updates for graphics templates use within MHC.

| Template | Description |
| --- | --- |
| oled1_xpro| Fixed C21 graphics templates to target C21 XPLD board|
| xplained_pro| Fixed C21 graphics templates to target C21 XPLD board|
| pda_tm4301b| Fixed PDA TM4301B template causing stretch display output|

- **Board Support Packages (BSP)s** - The following table provides the list of updates for board support packages for use within MHC.

| BSP | Description |
| --- | --- |
| none | |

- **Development Interfaces** - The following table provides the list of updates for interface tools.

| Interface Tool | Description |
| --- | --- |
| MPLAB Harmony 3 Interactive Help | Added interactive help menu using Show User Manual Mouse Right-click  |

- **Development kit support** - The following table lists  applications available for different development kits.

| Applications | [SAM C21N Xplained Pro Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/PartNO/ATSAMC21-XPRO) | [SAM E54 Xplained Pro Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/PartNO/ATSAME54-XPRO) | [SAM E70 Xplained Ultra Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/PartNO/ATSAME70-XPLD) | [SAM A5D2 Xplained Ultra Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/atsama5d2c-xult) | [Multimedia Expansion Board II](https://www.microchip.com/DevelopmentTools/ProductDetails/PartNO/DM320005-5) |
| --- | --- | --- | --- | --- | --- |
| aria_quickstart           | x | x | x | x | x |

### KNOWN ISSUES

The current known issues are as follows:

* Code is compliant to MISRA C 2012 Mandatory guidelines, with the exception of Rule 9.1 (Code 530). 
In gfx.c, the variable args is falsely detected in violation of Code 530: &quot;Symbol not initialized&quot; at line 358.  In fact, va_start at line 358 is exactly where args is initialized.

* Interactive help using the Show User Manual Entry in the Right-click menu for configuration options provided by this module is not yet available from within the MPLAB Harmony Configurator (MHC).  Please see the *Configuring the Library* section in the help documentation in the doc folder for this Harmony 3 module instead.  Help is available in both CHM and PDF formats.

* The target configuration aria_quickstart_e70_xult_xpro_spi does not support touch.

* The Heap Estimator can be inaccurate with estimating PNG images that have high pixel fidelity.

* Project regeneration from command line can remove Aria generated screens and widgets.

* MHGC GAC does not generated a 2DGPU comaptible palette table. A translation step is required to create word values from little endian byte array. 

* Applications for PIC32MZ DA using external DDR are only supported on Rev A1 silicon.

### DEVELOPMENT TOOLS

| Tool | Version |
| --- | --- |
| [MPLAB X IDE](https://www.microchip.com/mplab/mplab-x-ide) | v5.20 |
| [MPLAB XC32 C/C++ Compiler](https://www.microchip.com/mplab/compilers)      | v2.20 | 
| MPLAB X IDE plug-ins          |  |
| MPLAB Harmony Configurator (MHC) plug-in   | v3.3.0 | 
| Harmony 3 BSP (https://github.com/Microchip-MPLAB-Harmony/bsp)   | v3.3.0 |
| Harmony 3 CSP (https://github.com/Microchip-MPLAB-Harmony/csp)  | v3.3.0 |
| Harmony 3 Core (https://github.com/Microchip-MPLAB-Harmony/core)  | v3.3.0|
| Harmony 3 Graphics (https://github.com/Microchip-MPLAB-Harmony/gfx)   | v3.3.0 |
| Harmony 3 Dev_Packs (https://github.com/Microchip-MPLAB-Harmony/dev_packs)   | v3.3.0 |