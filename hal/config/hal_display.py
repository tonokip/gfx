DisplayMenu = halComponent.createMenuSymbol("DisplayMenu", None)
DisplayMenu.setLabel("Display Settings")
DisplayMenu.setDescription("Contains various settings for the graphics display.")

DisplayName = halComponent.createStringSymbol("DisplayName", DisplayMenu)
DisplayName.setLabel("Name")
DisplayName.setDescription("The display name.")
DisplayName.setDefaultValue("Custom Display")

DisplayWidth = halComponent.createIntegerSymbol("DisplayWidth", DisplayMenu)
DisplayWidth.setLabel("Width")
DisplayWidth.setDescription("The width of the display in pixels.")
DisplayWidth.setDefaultValue(480)

DisplayHeight = halComponent.createIntegerSymbol("DisplayHeight", DisplayMenu)
DisplayHeight.setLabel("Height")
DisplayHeight.setDescription("The height of the display in pixels.")
DisplayHeight.setDefaultValue(272)

DisplayDataWidth = halComponent.createIntegerSymbol("DisplayDataWidth", DisplayMenu)
DisplayDataWidth.setLabel("Data Width")
DisplayDataWidth.setDescription("The width of the display data bus in bits.")
DisplayDataWidth.setDefaultValue(16)

DisplayHorzMenu = halComponent.createMenuSymbol("DisplayHorzMenu", DisplayMenu)
DisplayHorzMenu.setLabel("Horizontal Attributes")
DisplayHorzMenu.setDescription("Contains the display horizontal refresh values.")

DisplayHorzPulseWidth = halComponent.createIntegerSymbol("DisplayHorzPulseWidth", DisplayHorzMenu)
DisplayHorzPulseWidth.setLabel("Horizontal Pulse Width")
DisplayHorzPulseWidth.setDescription("The horizontal pulse width.")
DisplayHorzPulseWidth.setDefaultValue(41)

DisplayHorzBackPorch = halComponent.createIntegerSymbol("DisplayHorzBackPorch", DisplayHorzMenu)
DisplayHorzBackPorch.setLabel("Horizontal Back Porch")
DisplayHorzBackPorch.setDescription("The horizontal back porch size in pixels.")
DisplayHorzBackPorch.setDefaultValue(2)

DisplayHorzFrontPorch = halComponent.createIntegerSymbol("DisplayHorzFrontPorch", DisplayHorzMenu)
DisplayHorzFrontPorch.setLabel("Horizontal Front Porch")
DisplayHorzFrontPorch.setDescription("The horizontal front porch size in pixels.")
DisplayHorzFrontPorch.setDefaultValue(2)

DisplayVertMenu = halComponent.createMenuSymbol("DisplayVertMenu", DisplayMenu)
DisplayVertMenu.setLabel("Vertical Attributes")
DisplayVertMenu.setDescription("Contains the display vertical refresh values.")

DisplayVertPulseWidth = halComponent.createIntegerSymbol("DisplayVertPulseWidth", DisplayVertMenu)
DisplayVertPulseWidth.setLabel("Vertical Pulse Width")
DisplayVertPulseWidth.setDescription("The vertical pulse width.")
DisplayVertPulseWidth.setDefaultValue(41)

DisplayVertBackPorch = halComponent.createIntegerSymbol("DisplayVertBackPorch", DisplayVertMenu)
DisplayVertBackPorch.setLabel("Vertical Back Porch")
DisplayVertBackPorch.setDescription("The vertical back porch size in pixels.")
DisplayVertBackPorch.setDefaultValue(2)

DisplayVertFrontPorch = halComponent.createIntegerSymbol("DisplayVertFrontPorch", DisplayVertMenu)
DisplayVertFrontPorch.setLabel("Vertical Front Porch")
DisplayVertFrontPorch.setDescription("The vertical front porch size in pixels.")
DisplayVertFrontPorch.setDefaultValue(2)

DisplayInvLeftShift = halComponent.createBooleanSymbol("DisplayInvLeftShift", DisplayMenu)
DisplayInvLeftShift.setLabel("Inverted Left Shift")
DisplayInvLeftShift.setDescription("Indicates if this display requries inverted left shift.")
DisplayInvLeftShift.setDefaultValue(False)

DisplayBackLightMenu = halComponent.createMenuSymbol("DisplayBackLightMenu", DisplayMenu)
DisplayBackLightMenu.setLabel("Back Light Settings")
DisplayBackLightMenu.setDescription("Contains values for controlling the back light.")

DisplayBacklightDisable = halComponent.createIntegerSymbol("DisplayBacklightDisable", DisplayBackLightMenu)
DisplayBacklightDisable.setLabel("Back Light Disable Value")
DisplayBacklightDisable.setDescription("The value used to disable the display back light.")
DisplayBacklightDisable.setDefaultValue(1)

DisplayBacklightEnable = halComponent.createIntegerSymbol("DisplayBacklightEnable", DisplayBackLightMenu)
DisplayBacklightEnable.setLabel("Back Light Enable Value")
DisplayBacklightEnable.setDescription("The value used to enable the display back light.")
DisplayBacklightEnable.setDefaultValue(1)
DisplayBacklightEnable.setReadOnly(True)

DisplayPolarityMenu = halComponent.createMenuSymbol("DisplayPolarityMenu", DisplayMenu)
DisplayPolarityMenu.setLabel("Polarity Settings")
DisplayPolarityMenu.setDescription("Contains the display polarity values.")

DisplayVSYNCNegative = halComponent.createBooleanSymbol("DisplayVSYNCNegative", DisplayPolarityMenu)
DisplayVSYNCNegative.setLabel("VSYNC Negative?")
DisplayVSYNCNegative.setDescription("Indicates if this display requries negative VSYNC polarity.")
DisplayVSYNCNegative.setDefaultValue(False)

DisplayHSYNCNegative = halComponent.createBooleanSymbol("DisplayHSYNCNegative", DisplayPolarityMenu)
DisplayHSYNCNegative.setLabel("HSYNC Negative?")
DisplayHSYNCNegative.setDescription("Indicates if this display requries negative HSYNC polarity.")
DisplayHSYNCNegative.setDefaultValue(False)

DisplayDataEnable = halComponent.createBooleanSymbol("DisplayDataEnable", DisplayMenu)
DisplayDataEnable.setLabel("Use Data Enable?")
DisplayDataEnable.setDescription("Indicates if this display requries the use of the Data Enable line.")
DisplayDataEnable.setDefaultValue(True)

DisplayDataEnablePolarity = halComponent.createBooleanSymbol("DisplayDataEnablePolarity", DisplayMenu)
DisplayDataEnablePolarity.setLabel("Data Enable Polarity Positive?")
DisplayDataEnablePolarity.setDescription("Indicates if this display Data Enable polarity is positive.")
DisplayDataEnablePolarity.setDefaultValue(True)

DisplayUseReset = halComponent.createBooleanSymbol("DisplayUseReset", DisplayMenu)
DisplayUseReset.setLabel("Use Reset?")
DisplayUseReset.setDescription("Indicates if this display reset line should be used.")
DisplayUseReset.setDefaultValue(True)

DisplayResetPolarity = halComponent.createBooleanSymbol("DisplayResetPolarity", DisplayMenu)
DisplayResetPolarity.setLabel("Reset Polarity Positive?")
DisplayResetPolarity.setDescription("Indicates if this display reset line should be reset positive.")
DisplayResetPolarity.setDefaultValue(True)

DisplayUseChipSelect = halComponent.createBooleanSymbol("DisplayUseChipSelect", DisplayMenu)
DisplayUseChipSelect.setLabel("Use Chip Select?")
DisplayUseChipSelect.setDescription("Indicates if this display uses the chip select line.")
DisplayUseChipSelect.setDefaultValue(True)

DisplayChipSelectPolarity = halComponent.createBooleanSymbol("DisplayChipSelectPolarity", DisplayMenu)
DisplayChipSelectPolarity.setLabel("Chip Select Polarity Positive?")
DisplayChipSelectPolarity.setDescription("Indicates if this display chip select line should be positive.")
DisplayChipSelectPolarity.setDefaultValue(True)



