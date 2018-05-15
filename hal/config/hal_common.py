def instantiateComponent(halCommonComponent):
	testInt = halCommonComponent.createIntegerSymbol("testInt", None)
	testInt.setLabel("common test integer")
	testInt.setDefaultValue(5)
	
	testFile = halCommonComponent.createFileSymbol("testFile", None)
	testFile.setSourcePath("src/testfile.c.ftl")
	testFile.setOutputName("testfile.c")
	testFile.setDestPath("/")
	testFile.setProjectPath("/")
	testFile.setType("SOURCE")
	testFile.setMarkup(True)
	testFile.setOverwrite(True)