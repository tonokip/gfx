def instantiateComponent(comp):
	Width = comp.createIntegerSymbol("Width", None)
	Width.setLabel("Width")
	Width.setDescription("The width of the touch panel in pixels.")
	Width.setDefaultValue(480)
	
	Height = comp.createIntegerSymbol("Height", None)
	Height.setLabel("Height")
	Height.setDescription("The height of the touch panel in pixels.")
	Height.setDefaultValue(272)
	
def onDependentComponentAdded(component, dependencyID, dependencyComponent):
	if dependencyID == "touch_panel":
		component.setSymbolValue("Width", dependencyComponent.getSymbolValue("TouchWidth"), 1)
		component.setSymbolValue("Height", dependencyComponent.getSymbolValue("TouchHeight"), 1)
	
def onDependentComponentRemoved(component, dependencyID, dependencyComponent):
	if dependencyID == "touch_panel":
		component.clearSymbolValue("Width")
		component.clearSymbolValue("Height")