HALConnected = comp.createBooleanSymbol("HALConnected", None)
HALConnected.setVisible(False)
HALConnected.setDefaultValue(False)
HALConnected.setDependencies(onHALConnected, ["HALConnected"])

# these two symbols are read by the HAL for initialization purposes
# they must match the function names in the actual driver code
DriverInfoFunction = comp.createStringSymbol("DriverInfoFunction", None)
DriverInfoFunction.setLabel("Driver Info Function Name")
DriverInfoFunction.setReadOnly(True)
DriverInfoFunction.setDefaultValue("driverSSD1963InfoGet")
DriverInfoFunction.setVisible(False)

DriverInitFunction = comp.createStringSymbol("DriverInitFunction", None)
DriverInitFunction.setLabel("Driver Init Function Name")
DriverInitFunction.setReadOnly(True)
DriverInitFunction.setDefaultValue("driverSSD1963ContextInitialize")
DriverInitFunction.setVisible(False)

#General Comment
DriverComment = comp.createCommentSymbol("DriverComment", None)
DriverComment.setLabel("The settings for this driver are limited to displays that support 16-bit RGB 565 format. For other display types, the driver may need to be modified manually.")

# configuration options
Interface = comp.createComboSymbol("Interface", None, ["Parallel 8080"])
Interface.setLabel("Interface Mode")
Interface.setDescription("Interface to SSD1963.")
Interface.setVisible(False)

## Display Settings Menu
DisplaySettingsMenu = comp.createMenuSymbol("DisplaySettingsMenu", None)
DisplaySettingsMenu.setLabel("Display Settings")

HALComment = comp.createCommentSymbol("HALComment", None)
HALComment.setLabel("'Display Settings' are being managed by the GFX HAL and have been hidden.")
HALComment.setVisible(False)

DisplayWidth = comp.createIntegerSymbol("DisplayWidth", DisplaySettingsMenu)
DisplayWidth.setLabel("Width")
DisplayWidth.setDescription("The width of the frame buffer in pixels.")
DisplayWidth.setMax(864)
DisplayWidth.setMin(1)
DisplayWidth.setDefaultValue(480)

DisplayHeight = comp.createIntegerSymbol("DisplayHeight", DisplaySettingsMenu)
DisplayHeight.setLabel("Height")
DisplayHeight.setDescription("The height of the frame buffer in pixels.")
DisplayWidth.setMax(480)
DisplayWidth.setMin(1)
DisplayHeight.setDefaultValue(272)

DisplayHorzPulseWidth = comp.createIntegerSymbol("DisplayHorzPulseWidth", DisplaySettingsMenu)
DisplayHorzPulseWidth.setLabel("Horizontal Pulse Width")
DisplayHorzPulseWidth.setMin(0)
DisplayHorzPulseWidth.setDefaultValue(44)

DisplayHorzBackPorch = comp.createIntegerSymbol("DisplayHorzBackPorch", DisplaySettingsMenu)
DisplayHorzBackPorch.setLabel("Horizontal Back Porch")
DisplayHorzBackPorch.setMin(0)
DisplayHorzBackPorch.setDefaultValue(2)

DisplayHorzFrontPorch = comp.createIntegerSymbol("DisplayHorzFrontPorch", DisplaySettingsMenu)
DisplayHorzFrontPorch.setLabel("Horizontal Front Porch")
DisplayHorzFrontPorch.setMin(0)
DisplayHorzFrontPorch.setDefaultValue(2)

DisplayVertPulseWidth = comp.createIntegerSymbol("DisplayVertPulseWidth", DisplaySettingsMenu)
DisplayVertPulseWidth.setLabel("Vertical Pulse Width")
DisplayVertPulseWidth.setMin(0)
DisplayVertPulseWidth.setDefaultValue(22)

DisplayVertBackPorch = comp.createIntegerSymbol("DisplayVertBackPorch", DisplaySettingsMenu)
DisplayVertBackPorch.setLabel("Vertical Back Porch")
DisplayVertBackPorch.setMin(0)
DisplayVertBackPorch.setDefaultValue(2)

DisplayVertFrontPorch = comp.createIntegerSymbol("DisplayVertFrontPorch", DisplaySettingsMenu)
DisplayVertFrontPorch.setLabel("Vertical Front Porch")
DisplayVertFrontPorch.setMin(0)
DisplayVertFrontPorch.setDefaultValue(2)

## Clock Settings Menu
MCLK_DefaultValue_Hz = 100000000 #100MHz
PCLK_DefaultValue_Hz = 15000000 #15MHz
PCLK_PRESCLR_DefaultValue = float( float(MCLK_DefaultValue_Hz)/float(PCLK_DefaultValue_Hz))

ClockSettingsMenu = comp.createMenuSymbol("ClockSettingsMenu", None)
ClockSettingsMenu.setLabel("Clock Settings")

MasterClock = comp.createIntegerSymbol("MasterClock", ClockSettingsMenu)
MasterClock.setLabel("Master Clock (Hz)")
MasterClock.setDescription("PLL Frequency")
MasterClock.setDefaultValue(MCLK_DefaultValue_Hz)
MasterClock.setReadOnly(True)

PixelClock = comp.createIntegerSymbol("PixelClock", ClockSettingsMenu)
PixelClock.setLabel("Pixel Clock (Hz)")
PixelClock.setDescription("Output Pixel Clock")
PixelClock.setDefaultValue(PCLK_DefaultValue_Hz)
PixelClock.setDependencies(onPixelClockSet, ["PixelClock"])

PixelClockPreScaler = comp.createStringSymbol("PixelClockPreScaler", ClockSettingsMenu)
PixelClockPreScaler.setLabel("Pixel Clock PreScaler")
PixelClockPreScaler.setDescription("Pixel Clock PreScaler")
PixelClockPreScaler.setDefaultValue(str(float("{0:.4f}".format(PCLK_PRESCLR_DefaultValue))))
PixelClockPreScaler.setReadOnly(True)

DisplayTimingOptionsEnabled = comp.createBooleanSymbol("DisplayTimingOptionsEnabled", None)
DisplayTimingOptionsEnabled.setLabel("Display Timing Options Enabled")
DisplayTimingOptionsEnabled.setDescription("Hints to the HAL if display timing is configurable for this display.")
DisplayTimingOptionsEnabled.setDefaultValue(True)
DisplayTimingOptionsEnabled.setVisible(False)

### Interface Settings Menu
InterfaceSettingsSMCMenu = comp.createMenuSymbol("InterfaceSettingsSMCMenu", None)
InterfaceSettingsSMCMenu.setLabel("Parallel 8080 Display Interface Settings")
InterfaceSettingsSMCMenu.setVisible(False)

### Parallel mode specific options
ParallelInterfaceWidth = comp.createComboSymbol("ParallelInterfaceWidth", InterfaceSettingsSMCMenu, ["16-bit", "8-bit"])
ParallelInterfaceWidth.setLabel("Data Bus Width")
ParallelInterfaceWidth.setDescription("Data Bus Width")
ParallelInterfaceWidth.setDefaultValue("16-bit")
#ParallelInterfaceWidth.setReadOnly(True)

EBIChipSelectIndex = comp.createIntegerSymbol("EBIChipSelectIndex", InterfaceSettingsSMCMenu)
EBIChipSelectIndex.setLabel("EBI Chip Select Index")
EBIChipSelectIndex.setDescription("The chip select index")
EBIChipSelectIndex.setDefaultValue(0)
EBIChipSelectIndex.setMin(0)
EBIChipSelectIndex.setMax(4)
EBIChipSelectIndex.setVisible(False)

ControlPinsMenu = comp.createMenuSymbol("ControlPinsMenu", InterfaceSettingsSMCMenu)
ControlPinsMenu.setLabel("Control Pin Settings")

ChipSelectControl = comp.createComboSymbol("ChipSelectControl", ControlPinsMenu, ["GPIO", "Peripheral"])
ChipSelectControl.setLabel("CS# Control")
ChipSelectControl.setDescription("Chip Select Control. Configures for bit-bang or peripheral mode.")
ChipSelectControl.setDefaultValue("GPIO")
ChipSelectControl.setReadOnly(True)

DataCommandSelectControl = comp.createComboSymbol("DataCommandSelectControl", ControlPinsMenu, ["GPIO", "Peripheral"])
DataCommandSelectControl.setLabel("D/C# Control")
DataCommandSelectControl.setDescription("Data Command Select Control. Configures for bit-bang or peripheral mode.")
DataCommandSelectControl.setDefaultValue("GPIO")
#DataCommandSelectControl.setReadOnly(True)
DataCommandSelectControl.setDependencies(onDataCommandSelectSet, ["DataCommandSelectControl"])

ReadStrobeControl = comp.createComboSymbol("ReadStrobeControl", ControlPinsMenu, ["GPIO", "Peripheral"])
ReadStrobeControl.setLabel("RD# Control")
ReadStrobeControl.setDescription("Read Strobe Control. Configures for bit-bang or peripheral mode.")
ReadStrobeControl.setDefaultValue("GPIO")
#ReadStrobeControl.setReadOnly(True)

WriteStrobeControl = comp.createComboSymbol("WriteStrobeControl", ControlPinsMenu, ["GPIO", "Peripheral"])
WriteStrobeControl.setLabel("WR# Control")
WriteStrobeControl.setDescription("Write Strobe Control. Configures for bit-bang or peripheral mode.")
WriteStrobeControl.setDefaultValue("GPIO")
#WriteStrobeControl.setReadOnly(True)

DelayNOPCount = comp.createIntegerSymbol("DelayNOPCount", InterfaceSettingsSMCMenu)
DelayNOPCount.setLabel("Number of NOPs for delay.")
DelayNOPCount.setDescription("Number of NOPs for bit-bang delay.")
DelayNOPCount.setDefaultValue(4)

DCXAddressBit = comp.createIntegerSymbol("DCXAddressBit", DataCommandSelectControl)
DCXAddressBit.setLabel("DCX Address Bit")
DCXAddressBit.setDescription("Address bit used for DCX signal.")
DCXAddressBit.setDefaultValue(12)
DCXAddressBit.setMin(0)
DCXAddressBit.setMax(31)
DCXAddressBit.setVisible(False)

## Driver Settings Menu
DriverSettingsMenu = comp.createMenuSymbol("DRIVER_SETTINGS_MENU", None)
DriverSettingsMenu.setLabel("Driver Settings")
DriverSettingsMenu.setVisible(False)

UseSyncBarriers = comp.createBooleanSymbol("UseSyncBarriers", DriverSettingsMenu)
UseSyncBarriers.setLabel("Use Synchronization Barriers")
UseSyncBarriers.setDescription("Use Synchronization Barriers.")
UseSyncBarriers.setDefaultValue(True)
UseSyncBarriers.setVisible(False)

PaletteMode = comp.createBooleanSymbol("PaletteMode", DriverSettingsMenu)
PaletteMode.setLabel("Palette Mode")
PaletteMode.setDescription("Enables Palette Mode.")
PaletteMode.setDefaultValue(False)
PaletteMode.setVisible(False)
### Unsupported options

### Start of Backlight config options
BacklightSettings = comp.createMenuSymbol("BacklightSettings", None)
BacklightSettings.setLabel("Backlight Settings")

BacklightPWMFrequency = comp.createIntegerSymbol("BacklightPWMFrequency", BacklightSettings)
BacklightPWMFrequency.setLabel("Backlight PWM Frequency (Hz)")
BacklightPWMFrequency.setDescription("The Backlight PWM Frequency")
BacklightPWMFrequency.setMin(0)
BacklightPWMFrequency.setMax(1000)
BacklightPWMFrequency.setDefaultValue(200)
BacklightPWMFrequency.setDependencies(onBacklightPWMFrequencySet, ["BacklightPWMFrequency"])

DefaultBrightness = comp.createIntegerSymbol("DefaultBrightness", BacklightSettings)
DefaultBrightness.setLabel("Default Brightness (%)")
DefaultBrightness.setDescription("The default brightness setting at driver startup")
DefaultBrightness.setMin(0)
DefaultBrightness.setMax(100)
DefaultBrightness.setDefaultValue(100)




