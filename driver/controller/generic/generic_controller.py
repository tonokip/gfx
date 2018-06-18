def instantiateComponent(comp):
	projectPath = "config/" + Variables.get("__CONFIGURATION_NAME") + "/gfx/driver/controller/generic"
	
	# some configuration values
	UseStaticBuffer = comp.createBooleanSymbol("UseStaticBuffer", None)
	UseStaticBuffer.setLabel("Use Static Frame Buffer?")
	UseStaticBuffer.setDescription("Configures the driver to use a static flash-based frame buffer.")
	UseStaticBuffer.setDefaultValue(False)

	# the HAL uses these values to populate the driver initialization table
	DriverInfoFunction = comp.createStringSymbol("DriverInfoFunction", None)
	DriverInfoFunction.setLabel("Driver Info Function Name")
	DriverInfoFunction.setReadOnly(True)
	DriverInfoFunction.setDefaultValue("driverGenericInfoGet")
	DriverInfoFunction.setVisible(False)
	
	DriverInitFunction = comp.createStringSymbol("DriverInitFunction", None)
	DriverInitFunction.setLabel("Driver Init Function Name")
	DriverInitFunction.setReadOnly(True)
	DriverInitFunction.setDefaultValue("driverGenericContextInitialize")
	DriverInitFunction.setVisible(False)
	
	# driver code template files
	DRIVER_C = comp.createFileSymbol("DRIVER_C", None)
	DRIVER_C.setSourcePath("drv_gfx_generic.c.ftl")
	DRIVER_C.setDestPath("gfx/driver/controller/generic/")
	DRIVER_C.setOutputName("drv_gfx_generic.c")
	DRIVER_C.setProjectPath(projectPath)
	DRIVER_C.setType("SOURCE")
	DRIVER_C.setMarkup(True)
	
	DRIVER_H = comp.createFileSymbol("DRIVER_H", None)
	DRIVER_H.setSourcePath("drv_gfx_generic.h.ftl")
	DRIVER_H.setDestPath("gfx/driver/controller/generic")
	DRIVER_H.setOutputName("drv_gfx_generic.h")
	DRIVER_H.setProjectPath(projectPath)
	DRIVER_H.setType("HEADER")
	DRIVER_H.setMarkup(True)