libraryOptionsMenu = component.createMenuSymbol("libraryOptionsMenu", None)
libraryOptionsMenu.setLabel("Library Configuration")

displayWidth = component.createIntegerSymbol("displayWidth", libraryOptionsMenu)
displayWidth.setVisible(False)
displayWidth.setDefaultValue(480)
displayWidth.setMin(0)
displayWidth.setDependencies(onDisplayWidthChanged, ["gfx_hal:DisplayWidth"]) #anonymous dependency

displayHeight = component.createIntegerSymbol("displayHeight", libraryOptionsMenu)
displayHeight.setVisible(False)
displayHeight.setDefaultValue(272)
displayHeight.setMin(0)
displayHeight.setDependencies(onDisplayHeightChanged, ["gfx_hal:DisplayHeight"]) #anonymous dependency

displayOrientation = component.createComboSymbol("displayOrientation", libraryOptionsMenu, ["0", "90", "180", "270"])
displayOrientation.setLabel("Display Orientation")
displayOrientation.setDescription("Configures software-based display orientation.")

displayMirroring = component.createBooleanSymbol("displayMirroring", libraryOptionsMenu)
displayMirroring.setLabel("Display Mirroring")
displayMirroring.setDescription("Enables software-based display mirroring.")

useAcceleration = component.createBooleanSymbol("useAcceleration", libraryOptionsMenu)
useAcceleration.setLabel("Enable Display Accleration?")
useAcceleration.setDescription("<html>Enables graphics acceleration pipeline <b>if available<b>.")

useGlobalPalette = component.createBooleanSymbol("useGlobalPalette", libraryOptionsMenu)
useGlobalPalette.setLabel("Enable Global Palette Mode?")
useGlobalPalette.setDescription("Enables global palette mode.")
useGlobalPalette.setDependencies(onUseGlobalPaletteChanged, ["useGlobalPalette"])

codeGenerationMenu = component.createMenuSymbol("codeGenerationMenu", None)
codeGenerationMenu.setLabel("Code Generator Options")

genAriaAssets = component.createBooleanSymbol("genAriaAssets", codeGenerationMenu)
genAriaAssets.setLabel("Generate Assets?")
genAriaAssets.setDefaultValue(True)
genAriaAssets.setDescription("Indicates that any configured MHGC assets should be automatically generated and added to the application.")

genAriaDesign = component.createBooleanSymbol("genAriaDesign", codeGenerationMenu)
genAriaDesign.setLabel("Generate Design?")
genAriaDesign.setDefaultValue(True)
genAriaDesign.setDescription("Indicates that any configured MHGC screens should be automatically generated and added to the application.")
genAriaDesign.setDependencies(onGenAriaDesignChanged, ["genAriaDesign"])

genAriaEvents = component.createBooleanSymbol("genAriaEvents", genAriaDesign)
genAriaEvents.setLabel("Generate Event Handlers?")
genAriaEvents.setDefaultValue(True)
genAriaEvents.setDescription("Indicates that any configured MHGC events should be automatically generated and added to the application.")

genAriaMacros = component.createBooleanSymbol("genAriaMacros", genAriaDesign)
genAriaMacros.setLabel("Generate Macros?")
genAriaMacros.setDefaultValue(True)
genAriaMacros.setDescription("Indicates that any configured MHGC macros should be automatically generated and added to the application.")

genAriaMediaIntf = component.createBooleanSymbol("genAriaMediaIntf", genAriaDesign)
genAriaMediaIntf.setLabel("Generate External Media Interface?")
genAriaMediaIntf.setDefaultValue(True)
genAriaMediaIntf.setDescription("Indicates that the code generator should create the binding code to allow Aria to request external media data.")


enableInput = component.createBooleanSymbol("enableInput", codeGenerationMenu)
enableInput.setLabel("Enable Input Event Interface?")
enableInput.setDefaultValue(False)
enableInput.setDescription("Indicates that Aria should interface with the Input System Service for input events.")
enableInput.setDependencies(onEnableInputChanged, ["enableInput"])

widgetMenu = component.createMenuSymbol("widgetMenu", None)
widgetMenu.setLabel("Widget Configuration")

enableArcWidget = component.createBooleanSymbol("enableArcWidget", widgetMenu)
enableArcWidget.setLabel("Enable Arc Widget?")
enableArcWidget.setDefaultValue(True)
enableArcWidget.setDescription("Enables the Aria Arc widget.  Disabling this will remove the code for this widget and it will not be available for use.</html>")

enableBarGraphWidget = component.createBooleanSymbol("enableBarGraphWidget", widgetMenu)
enableBarGraphWidget.setLabel("Enable Bar Graph Widget?")
enableBarGraphWidget.setDefaultValue(True)
enableBarGraphWidget.setDescription("Enables the Aria Bar Graph widget.  Disabling this will remove the code for this widget and it will not be available for use.")

enableButtonWidget = component.createBooleanSymbol("enableButtonWidget", widgetMenu)
enableButtonWidget.setLabel("Enable Button Widget?")
enableButtonWidget.setDefaultValue(True)
enableButtonWidget.setDescription("Enables the Aria Button widget.  Disabling this will remove the code for this widget and it will not be available for use.")

enableCheckBoxWidget = component.createBooleanSymbol("enableCheckBoxWidget", widgetMenu)
enableCheckBoxWidget.setLabel("Enable Check Box Widget?")
enableCheckBoxWidget.setDefaultValue(True)
enableCheckBoxWidget.setDescription("Enables the Aria Check Box widget.  Disabling this will remove the code for this widget and it will not be available for use.")

enableCircleWidget = component.createBooleanSymbol("enableCircleWidget", widgetMenu)
enableCircleWidget.setLabel("Enable Circle Widget?")
enableCircleWidget.setDefaultValue(True)
enableCircleWidget.setDescription("Enables the Aria Circle widget.  Disabling this will remove the code for this widget and it will not be available for use.")

enableCircularGuageWidget = component.createBooleanSymbol("enableCircularGuageWidget", widgetMenu)
enableCircularGuageWidget.setLabel("Enable Circular Guage Widget?")
enableCircularGuageWidget.setDefaultValue(True)
enableCircularGuageWidget.setDescription("Enables the Aria Circular Guage widget.  Disabling this will remove the code for this widget and it will not be available for use.")

enableCircularSliderWidget = component.createBooleanSymbol("enableCircularSliderWidget", widgetMenu)
enableCircularSliderWidget.setLabel("Enable Circular Slider Widget?")
enableCircularSliderWidget.setDefaultValue(True)
enableCircularSliderWidget.setDescription("Enables the Aria Circular Slider widget.  Disabling this will remove the code for this widget and it will not be available for use.")

enableDrawSurfaceWidget = component.createBooleanSymbol("enableDrawSurfaceWidget", widgetMenu)
enableDrawSurfaceWidget.setLabel("Enable Draw Surface Widget?")
enableDrawSurfaceWidget.setDefaultValue(True)
enableDrawSurfaceWidget.setDescription("Enables the Aria Draw Surface widget.  Disabling this will remove the code for this widget and it will not be available for use.")


enableImageWidget = component.createBooleanSymbol("enableImageWidget", widgetMenu)
enableImageWidget.setLabel("Enable Image Widget?")
enableImageWidget.setDefaultValue(True)
enableImageWidget.setDescription("Enables the Aria Image widget.  Disabling this will remove the code for this widget and it will not be available for use.")

enableImagePlusWidget = component.createBooleanSymbol("enableImagePlusWidget", widgetMenu)
enableImagePlusWidget.setLabel("Enable Image Plus Widget?")
enableImagePlusWidget.setDefaultValue(True)
enableImagePlusWidget.setDescription("Enables the Aria Image Plus widget.  Disabling this will remove the code for this widget and it will not be available for use.")

enableImageSequenceWidget = component.createBooleanSymbol("enableImageSequenceWidget", widgetMenu)
enableImageSequenceWidget.setLabel("Enable Image Sequence Widget?")
enableImageSequenceWidget.setDefaultValue(True)
enableImageSequenceWidget.setDescription("Enables the Aria Image Sequence widget.  Disabling this will remove the code for this widget and it will not be available for use.")

enableGradientWidget = component.createBooleanSymbol("enableGradientWidget", widgetMenu)
enableGradientWidget.setLabel("Enable Gradient Widget?")
enableGradientWidget.setDefaultValue(True)
enableGradientWidget.setDescription("Enables the Aria Gradient widget.  Disabling this will remove the code for this widget and it will not be available for use.")

enableGroupBoxWidget = component.createBooleanSymbol("enableGroupBoxWidget", widgetMenu)
enableGroupBoxWidget.setLabel("Enable Group Box Widget?")
enableGroupBoxWidget.setDefaultValue(True)
enableGroupBoxWidget.setDescription("Enables the Aria Group Box widget.  Disabling this will remove the code for this widget and it will not be available for use.")

enableKeyPadWidget = component.createBooleanSymbol("enableKeyPadWidget", widgetMenu)
enableKeyPadWidget.setLabel("Enable Key Pad Widget?")
enableKeyPadWidget.setDefaultValue(True)
enableKeyPadWidget.setDescription("Enables the Aria Key Pad widget.  Disabling this will remove the code for this widget and it will not be available for use.")

enableLabelWidget = component.createBooleanSymbol("enableLabelWidget", widgetMenu)
enableLabelWidget.setLabel("Enable Label Widget?")
enableLabelWidget.setDefaultValue(True)
enableLabelWidget.setDescription("Enables the Aria Label widget.  Disabling this will remove the code for this widget and it will not be available for use.")

enableLineWidget = component.createBooleanSymbol("enableLineWidget", widgetMenu)
enableLineWidget.setLabel("Enable Line Widget?")
enableLineWidget.setDefaultValue(True)
enableLineWidget.setDescription("Enables the Aria Line widget.  Disabling this will remove the code for this widget and it will not be available for use.")

enableLineGraphWidget = component.createBooleanSymbol("enableLineGraphWidget", widgetMenu)
enableLineGraphWidget.setLabel("Enable Line Graph Widget?")
enableLineGraphWidget.setDefaultValue(True)
enableLineGraphWidget.setDescription("Enables the Aria Line Graph widget.  Disabling this will remove the code for this widget and it will not be available for use.")

enableListWidget = component.createBooleanSymbol("enableListWidget", widgetMenu)
enableListWidget.setLabel("Enable List Widget?")
enableListWidget.setDefaultValue(True)
enableListWidget.setDescription("Enables the Aria List widget.  Disabling this will remove the code for this widget and it will not be available for use.")

enableListWheelWidget = component.createBooleanSymbol("enableListWheelWidget", widgetMenu)
enableListWheelWidget.setLabel("Enable List Wheel Widget?")
enableListWheelWidget.setDefaultValue(True)
enableListWheelWidget.setDescription("Enables the Aria List Wheel widget.  Disabling this will remove the code for this widget and it will not be available for use.")

enablePieChartWidget = component.createBooleanSymbol("enablePieChartWidget", widgetMenu)
enablePieChartWidget.setLabel("Enable Pie Chart Widget?")
enablePieChartWidget.setDefaultValue(True)
enablePieChartWidget.setDescription("Enables the Aria Pie Chart widget.  Disabling this will remove the code for this widget and it will not be available for use.")

enableProgressBarWidget = component.createBooleanSymbol("enableProgressBarWidget", widgetMenu)
enableProgressBarWidget.setLabel("Enable Progress Bar Widget?")
enableProgressBarWidget.setDefaultValue(True)
enableProgressBarWidget.setDescription("Enables the Aria Progress Bar widget.  Disabling this will remove the code for this widget and it will not be available for use.")

enableRadialMenuWidget = component.createBooleanSymbol("enableRadialMenuWidget", widgetMenu)
enableRadialMenuWidget.setLabel("Enable Radial Menu Widget?")
enableRadialMenuWidget.setDefaultValue(True)
enableRadialMenuWidget.setDescription("Enables the Aria Radial Menu widget.  Disabling this will remove the code for this widget and it will not be available for use.")

enableRadioButtonWidget = component.createBooleanSymbol("enableRadioButtonWidget", widgetMenu)
enableRadioButtonWidget.setLabel("Enable Radio Button Widget?")
enableRadioButtonWidget.setDefaultValue(True)
enableRadioButtonWidget.setDescription("Enables the Aria Radio Button widget.  Disabling this will remove the code for this widget and it will not be available for use.")

enableRectangleWidget = component.createBooleanSymbol("enableRectangleWidget", widgetMenu)
enableRectangleWidget.setLabel("Enable Rectangle Widget?")
enableRectangleWidget.setDefaultValue(True)
enableRectangleWidget.setDescription("Enables the Aria Rectangle widget.  Disabling this will remove the code for this widget and it will not be available for use.")

enableScrollBarWidget = component.createBooleanSymbol("enableScrollBarWidget", widgetMenu)
enableScrollBarWidget.setLabel("Enable Scroll Bar Widget?")
enableScrollBarWidget.setDefaultValue(True)
enableScrollBarWidget.setDescription("Enables the Aria Scroll Bar widget.  Disabling this will remove the code for this widget and it will not be available for use.")

enableSliderWidget = component.createBooleanSymbol("enableSliderWidget", widgetMenu)
enableSliderWidget.setLabel("Enable Slider Widget?")
enableSliderWidget.setDefaultValue(True)
enableSliderWidget.setDescription("Enables the Aria Slider widget.  Disabling this will remove the code for this widget and it will not be available for use.")

enableTextFieldWidget = component.createBooleanSymbol("enableTextFieldWidget", widgetMenu)
enableTextFieldWidget.setLabel("Enable Text Field Widget?")
enableTextFieldWidget.setDefaultValue(True)
enableTextFieldWidget.setDescription("Enables the Aria Text Field widget.  Disabling this will remove the code for this widget and it will not be available for use.")

enableTouchTestWidget = component.createBooleanSymbol("enableTouchTestWidget", widgetMenu)
enableTouchTestWidget.setLabel("Enable Touch Test Widget?")
enableTouchTestWidget.setDefaultValue(True)
enableTouchTestWidget.setDescription("Enables the Aria Touch Test widget.  Disabling this will remove the code for this widget and it will not be available for use.")

enableWindowWidget = component.createBooleanSymbol("enableWindowWidget", widgetMenu)
enableWindowWidget.setLabel("Enable Window Widget?")
enableWindowWidget.setDefaultValue(True)
enableWindowWidget.setDescription("Enables the Aria Window widget.  Disabling this will remove the code for this widget and it will not be available for use.")


