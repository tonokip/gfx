# generate code files

GFX_ILI9488_C = comp.createFileSymbol("GFX_ILI9488_C", None)
GFX_ILI9488_C.setDestPath("gfx/driver/controller/ili9488/")
GFX_ILI9488_C.setSourcePath("templates/drv_gfx_ili9488.c.ftl")
GFX_ILI9488_C.setOutputName("drv_gfx_ili9488.c")
GFX_ILI9488_C.setProjectPath("/gfx/driver/controller/ili9488/")
GFX_ILI9488_C.setType("SOURCE")
GFX_ILI9488_C.setMarkup(True)

GFX_ILI9488_DBIB_C = comp.createFileSymbol("GFX_ILI9488_DBIB_C", None)
GFX_ILI9488_DBIB_C.setDestPath("gfx/driver/controller/ili9488/")
GFX_ILI9488_DBIB_C.setSourcePath("templates/drv_gfx_ili9488_dbib.c.ftl")
GFX_ILI9488_DBIB_C.setOutputName("drv_gfx_ili9488_intf.c")
GFX_ILI9488_DBIB_C.setProjectPath("/gfx/driver/controller/ili9488/")
GFX_ILI9488_DBIB_C.setType("SOURCE")
GFX_ILI9488_DBIB_C.setEnabled(False)
GFX_ILI9488_DBIB_C.setMarkup(True)

GFX_ILI9488_SPI = comp.createFileSymbol("GFX_ILI9488_SPI", None)
GFX_ILI9488_SPI.setDestPath("gfx/driver/controller/ili9488/")
GFX_ILI9488_SPI.setSourcePath("src/drv_gfx_ili9488_spi.c")
GFX_ILI9488_SPI.setOutputName("drv_gfx_ili9488_intf.c")
GFX_ILI9488_SPI.setProjectPath("/gfx/driver/controller/ili9488/")
GFX_ILI9488_SPI.setEnabled(False)
GFX_ILI9488_SPI.setType("SOURCE")

GFX_ILI9488_H = comp.createFileSymbol("GFX_ILI9488_H", None)
GFX_ILI9488_H.setDestPath("gfx/driver/controller/ili9488/")
GFX_ILI9488_H.setSourcePath("templates/drv_gfx_ili9488.h.ftl")
GFX_ILI9488_H.setOutputName("drv_gfx_ili9488.h")
GFX_ILI9488_H.setProjectPath("/gfx/driver/controller/ili9488/")
GFX_ILI9488_H.setType("HEADER")
GFX_ILI9488_H.setMarkup(True)

GFX_ILI9488_COMMON_H = comp.createFileSymbol("GFX_ILI9488_COMMON_H", None)
GFX_ILI9488_COMMON_H.setDestPath("gfx/driver/controller/ili9488/")
GFX_ILI9488_COMMON_H.setSourcePath("inc/drv_gfx_ili9488_common.h")
GFX_ILI9488_COMMON_H.setOutputName("drv_gfx_ili9488_common.h")
GFX_ILI9488_COMMON_H.setProjectPath("/gfx/driver/controller/ili9488/")
GFX_ILI9488_COMMON_H.setType("HEADER")

GFX_ILI9488_CMD_DEFS_H = comp.createFileSymbol("GFX_ILI9488_CMD_DEFS_H", None)
GFX_ILI9488_CMD_DEFS_H.setDestPath("gfx/driver/controller/ili9488/")
GFX_ILI9488_CMD_DEFS_H.setSourcePath("inc/drv_gfx_ili9488_cmd_defs.h")
GFX_ILI9488_CMD_DEFS_H.setOutputName("drv_gfx_ili9488_cmd_defs.h")
GFX_ILI9488_CMD_DEFS_H.setProjectPath("/gfx/driver/controller/ili9488/")
GFX_ILI9488_CMD_DEFS_H.setType("HEADER")