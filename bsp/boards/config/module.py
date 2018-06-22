import os

def loadModule():
	print("Load Module: GFX BSP")

	#configName = Variables.get("__CONFIGURATION_NAME")

	#bspDefault = Module.CreateComponent("BSP_default", configName + " Board (BSP)", "/Board Support Packages (BSPs)/", "default/config/bsp.py")

	import xml.etree.ElementTree as ET
	bspFile = open(Variables.get("__BSP_DIR") + "/../gfx/bsp/boards/module.xml", "r")
	bspContent = ET.fromstring(bspFile.read())
	for Board in bspContent.iter("Board"):
		if Board.attrib['processor'] == Variables.get("__PROCESSOR"):
			print("BSP: Load " + Board.attrib['name'])
			print("BSP: config " + Board.attrib['config'])
			Id = Board.attrib['name'].replace(" ", "_")
			bspComponent = Module.CreateComponent("BSP_" + Id, Board.attrib['name'] + " BSP", "/Board Support Packages (BSPs)/", Board.attrib['config'] + "/config/bsp.py")
	
