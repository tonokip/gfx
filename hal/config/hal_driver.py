DriverInfoMenu = halComponent.createMenuSymbol("DriverInfoMenu", None)
DriverInfoMenu.setLabel("Display Driver Information")
DriverInfoMenu.setDescription("Displays display driver information.")

DriverInfoFunction = halComponent.createStringSymbol("DriverInfoFunction", DriverInfoMenu)
DriverInfoFunction.setLabel("Driver Info Function Name")
DriverInfoFunction.setReadOnly(True)

DriverInitFunction = halComponent.createStringSymbol("DriverInitFunction", DriverInfoMenu)
DriverInitFunction.setLabel("Driver Init Function Name")
DriverInitFunction.setReadOnly(True)


