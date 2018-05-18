def instantiateComponent(comp):
	Width = comp.createIntegerSymbol("Width", None)
	Width.setLabel("Width")
	Width.setDescription("The width of the touch surface in pixels.")
	Width.setDefaultValue(480)
	
	Height = comp.createIntegerSymbol("Height", None)
	Height.setLabel("Height")
	Height.setDescription("The height of the touch surface in pixels.")
	Height.setDefaultValue(272)

def onDependentComponentAdded(component, dependencyID, dependencyComponent):
	if dependencyID == "gfx_display":
		component.setSymbolValue("Width", dependencyComponent.getSymbolValue("Width"), 1)
		component.setSymbolValue("Height", dependencyComponent.getSymbolValue("Height"), 1)
	
def onDependentComponentRemoved(component, dependencyID, dependencyComponent):
	if dependencyID == "gfx_display":
		component.clearSymbolValue("Width")
		component.clearSymbolValue("Height")