ProcInfoMenu = halComponent.createMenuSymbol("ProcInfoMenu", None)
ProcInfoMenu.setLabel("Graphics Processor Information")
ProcInfoMenu.setDescription("Displays graphics processor information.")

ProcInfoFunction = halComponent.createStringSymbol("ProcInfoFunction", ProcInfoMenu)
ProcInfoFunction.setLabel("Processor Info Function Name")
ProcInfoFunction.setReadOnly(True)

ProcInitFunction = halComponent.createStringSymbol("ProcInitFunction", ProcInfoMenu)
ProcInitFunction.setLabel("Processor Init Function Name")
ProcInitFunction.setReadOnly(True)