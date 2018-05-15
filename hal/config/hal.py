def instantiateComponent(halComponent, index):
	testInt = halComponent.createIntegerSymbol("testInt" + str(index), None)
	testInt.setLabel("instanced test integer")
	testInt.setDefaultValue(50 + index)
#	controllerCountSym = halComponent.createIntegerSymbol("controllerCount", None)
#	controllerCountSym.setLabel("Display Controller Count")
#	controllerCountSym.setDefaultValue(1)
#	controllerCountSym.setMin(1)
#	controllerCountSym.setMax(3)
#	controllerCountSym.setDependencies(onControllerCountChanged, ["controllerCount"])
	
	
#def onControllerCountChanged(controllerCountSym, event):
#	comp = controllerCountSym.getComponent()
#	
#	num = controllerCountSym.getValue()
#	
#	comp.setDependencyEnabled("gfx_display_controller_1", num >= 2)
#	comp.setDependencyEnabled("gfx_display_controller_2", num >= 3)