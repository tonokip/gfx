def instantiateComponent(comp):
	DriverInfoFunction = comp.createStringSymbol("DriverInfoFunction", None)
	DriverInfoFunction.setLabel("Driver Info Function Name")
	DriverInfoFunction.setReadOnly(True)
	DriverInfoFunction.setDefaultValue("driverLCCInfoGet")
	
	DriverInitFunction = comp.createStringSymbol("DriverInitFunction", None)
	DriverInitFunction.setLabel("Driver Init Function Name")
	DriverInitFunction.setReadOnly(True)
	DriverInitFunction.setDefaultValue("driverLCCContextInitialize")