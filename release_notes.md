# Microchip MPLAB Harmony 3 Release Notes
## GFX Release v3.2.0
### NEW FEATURES


- **GFX Contents** - This GFX release consist of apps, displays, drivers, hardware abstractions, input, middleware, and templates. The following table lists the contents in this GFX release.

| Category | Component | Description | Release Type | 
| --- | --- | ---- |---- |
| apps | aria_quickstart | Getting started in Graphics | Beta|
| displays | ATMXT-XPRO-480x320 | ATMXT Xplained Pro 480x320| Beta |
|      | ATOLED1_XPRO-128x32 | AT OLED Xplained Pro 128x32| Beta |
|      | PDA TM4301B 480x272| PDA 4.3" 480x272 | Beta |
|  drivers    | glcd | Graphics 3 Layer Display Driver | Beta |
|      | ili9488| Display Driver for the ili9488 Controller |Beta | 
|      | interface | Display Driver interface driver | Beta |
|      | LCC | Display Driver for the LCC software Controller| Beta |
|      | LCDC | Display Driver for the LCDC Controller| Beta |
|      | ssd1306 | Display Driver for the ssd1306 Controller  | Beta |
|      | ssd1963 | Display Driver for the ssd1963 Controller |     Beta |
|  hal    | hal | Aria Hardware Abstration Layer | Beta |
|  input    | maxtouch | Microchip maXTouch Touch Input Driver | Beta |
|  middleware    | aria | Harmony Graphics Middleware Solution | Beta |
| templates   | aria_gfx_oled1_xpro | MHC for oled xpro| Beta |
|             | aria_gfx_pda_tm4301b| MHC config for pda | Beta |
|             | aria_gfx_xplained_pro| MHC config for xpro | Beta |
|             | common| MHC config for common board |Beta |


- **New driver support** - The following table provides the list of new support for graphics and input drivers.

| Driver | Name | Feature | 
| --- | --- | --- |
| LCDC| LCDC | Added LCDC Driver|
| maXtouch| drv_maxtouch | Added maXtouch Configuration APIs|

- **New Middleware/HAL support** - The following table provides the list of added middleware and HAL content.

| Middleware/HAL | Additions | 
| --- | --- |
| aria| Added RTOS support for Aria|
| | Added backlight driver to GFX LCC driver|
| | Added LCDC Component and driver in MHC|
| | Added SSD1963 Component and Driver|
| | Added RTOS support for Input System Service|
| | Added ILI9488 SPI display driver support on E54|
| | Fixed laRectArray_RemoveDuplicates() block when arr->size is 0|
| | Fixed Color picker decimal value update for Alpha channel after setting the Hex value|
| | Fixed Circular Gauge Widget - wrong order for laCircularGaugeWidget_SetValue() call|

- **New Graphics Application Templates** - The following table provides the list of new MHC templates for use within MHC.

| Template | Description |
| --- | --- |
| aria_gfx_pda_tm4301b | Aria Graphics w/ PDA TM4301B Display  |
| aria_gfx_xplained_pro | Aria Graphics w/ Xplained Pro Display |

- **New Board Support Packages (BSP)s** - The following table provides the list of new MHC board support packages for use within MHC.

| BSP | Description |
| --- | --- |
| none | |

- **New Development Interfaces** - The following table provides the list of new interface tools support.

| Interface Tool | Description |
| --- | --- |
| MPLAB Harmony 3 Interactive Help | Added interactive help menu using Show User Manual Mouse Right-click  |

- **Development kit support** - The following table provides  applications available for different development kits.

| Applications | [SAM C21N Xplained Pro Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/PartNO/ATSAMC21-XPRO) | [SAM E54 Xplained Pro Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/PartNO/ATSAME54-XPRO) | [SAM E70 Xplained Ultra Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/PartNO/ATSAME70-XPLD) | [SAM A5D2 Xplained Ultra Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/atsama5d2c-xult) |
| --- | --- | --- | --- | --- |
| aria_quickstart           | x | x | x | x |

### KNOWN ISSUES

The current known issues are as follows:

* **Programming and debugging through EDBG is not supported**. The ICD4 needs to be used for programming and debugging.

* The ICD4 loads the reset line of the SAM V71 Xplained Ultra board. The following demo project drives the reset line and requires the ICD4 flex cable to be removed after programming to run the application.

* Code is compliant to MISRA C 2012 Mandatory guidelines, except for Rules R.9.1 and R.17.3

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
- MPLAB Harmony Configurator (MHC) v3.2.0.
