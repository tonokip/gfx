# Microchip MPLAB Harmony 3 Release Notes
## GFX Release v3.2.0
### NEW FEATURES

- **Development kit support** - The following table provides  applications available for different development kits

| Development Kits | applications |
| --- | --- |
| [SAM C21N Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMC21-XPRO) | aria_quickstart |
| [SAM D20 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMD20-XPRO) | aria_quickstart |
| [SAM D21 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMD21-XPRO) | aria_quickstart |
| [SAM E70 Xplained Ultra Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAME70-XULT) | aria_quickstart |
| [SAM V71 Xplained Ultra Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMV71-XULT) | aria_quickstart |

- **New driver support** - The following table provides the list of new support for graphics and input drivers.

| Driver | Name | Feature | 
| --- | --- | --- |
| LCDC| LCDC | Added LCDC Driver|
| maXtouch| drv_maxtouch | Added LCDC Driver|

- **New Middleware/HAL support** - The following table provides the list of middleware and HAL support for different product families.

| Middleware/HAL | Additions | 
| --- | --- |
| aria| Added RTOS support for Aria|
| | Added backlight driver to GFX LCC driver|
| | Added LCDC Component and driver in MHC|
| | Added SSD1963 Component and Driver|
| | Added RTOS support for Input System
Service|
| | Added ILI9488 SPI display driver support on
E54|
| | Fixed laRectArray_RemoveDuplicates()
block when arr->size is 0|
| | Fixed Color picker decimal value update for
Alpha channel after setting the Hex value|
| | Fixed Circular Gauge Widget - wrong order
for laCircularGaugeWidget_SetValue() call|

- **New Graphics Application Templates** - The following table provides the list of middleware and HAL support for different product families.

| Template | Description |
| --- | --- |
| aria_gfx_pda_tm4301b | "Aria Graphics w/ PDA TM4301B Display" -
New to Harmony 3 |
| aria_gfx_xplained_pro | "Aria Graphics w/ Xplained Pro Display" - New to Harmony 3 |

- **New Board Support Packages (BSP)s** - The following table provides the list of middleware and HAL support for different product families.

| BSP | Description |
| --- | --- |

- **New Applications** - The following table provides the list of middleware and HAL support for different product families.

| Application | Description | 
| --- | --- |
| aria_mxt_configure | maXTouch configuration | 
| aria_flash |  Widgets and advance capabilities|
| aria_flash (redisign) | Circular and graphing widgets| 
| aria_benchmark | Metrics on graphics operations | 

- **New Development Interfaces** - The following table provides the list of middleware and HAL support for different product families.

| Interface Tool | Description |
| --- | --- |
| MPLAB Harmony 3 Interactive Help | Added interactive help menu using Show User Manual Mouse Right-click  |

- **Development kit support** - The following table provides number of peripheral library application available for different development kits

| Development Kit | applications |
| --- | --- |
| [SAM C21N Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMC21-XPRO) | aria_quickstart |
| [SAM D20 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMD20-XPRO) | aria_quickstart |
| [SAM D21 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMD21-XPRO) | aria_quickstart |
| [SAM E70 Xplained Ultra Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAME70-XULT) | aria_quickstart |
| [SAM V71 Xplained Ultra Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMV71-XULT) | aria_quickstart |

### KNOWN ISSUES

The current known issues are as follows:

* **Programming and debugging through EDBG is not supported**. The ICD4 needs to be used for programming and debugging.

* The ICD4 loads the reset line of the SAM V71 Xplained Ultra board. The following demo project drives the reset line and requires the ICD4 flex cable to be removed after programming to run the application.

| Project Name | Development Kit |
| --- | --- |
| supc\_wakeup\_rtc | SAM V71 Xplained Ultra Evaluation Kit  |
| supc\_wakeup\_rtt | SAM V71 Xplained Ultra Evaluation Kit  |
| rswdt\_timeout | SAM V71 Xplained Ultra Evaluation Kit  |
| wdt\_timeout | SAM V71 Xplained Ultra Evaluation Kit  |

* Interactive help using the Show User Manual Entry in the Right-click menu for configuration options provided by this module is not yet available from within the MPLAB Harmony Configurator (MHC).  Please see the *Configuring the Library* section in the help documentation in the doc folder for this Harmony 3 module instead.  Help is available in both CHM and PDF formats.

* The target configuration aria_quickstart_e70_xult_xpro_spi does not support touch.

* The Heap Estimator can be inaccurate with estimating PNG images that have high pixel fidelity.

### DEVELOPMENT TOOLS

- [MPLAB X IDE v5.10](https://www.microchip.com/mplab/mplab-x-ide)
- [MPLAB XC32 C/C++ Compiler v2.15](https://www.microchip.com/mplab/compilers)
- MPLAB X IDE plug-ins:
- MPLAB Harmony Configurator (MHC) v3.1.0.
