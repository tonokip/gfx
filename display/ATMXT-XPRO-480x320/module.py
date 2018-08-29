def loadModule():
	component = Module.CreateComponent("gfx_disp_atmxt-xpro_320x480", "maXTouch Xplained Pro", "/Graphics/Displays/", "atmxt-xpro.py")
	component.setDisplayType("320x480 maXTouch Xplained Pro")
	component.addCapability("gfx_display", "Graphics Display", False)
	#component.addCapability("touch_panel", "Touch Panel", False)