utilsPath = "config/" + Variables.get("__CONFIGURATION_NAME") + "/gfx/third_party/"

JIDCTINT_C = component.createFileSymbol("JIDCTINT_C", None)
JIDCTINT_C.setSourcePath("third_party/decoder/jidctint/src/jidctint.c")
JIDCTINT_C.setDestPath("gfx/third_party/decoder/src/")
JIDCTINT_C.setProjectPath("config/" + Variables.get("__CONFIGURATION_NAME") + "/gfx/third_party/")
JIDCTINT_C.setType("SOURCE")
JIDCTINT_C.setEnabled(False)

LODE_PNG_DECODER_H = component.createFileSymbol("LODE_PNG_DECODER_H", None)
LODE_PNG_DECODER_H.setSourcePath("third_party/decoder/lodepng/lodepng.h")
LODE_PNG_DECODER_H.setDestPath("gfx/third_party/lodepng/")
LODE_PNG_DECODER_H.setProjectPath("config/" + Variables.get("__CONFIGURATION_NAME") + "/gfx/third_party/lodepng/")
LODE_PNG_DECODER_H.setType("HEADER")
LODE_PNG_DECODER_H.setEnabled(False)

LODE_PNG_DECODER_C = component.createFileSymbol("LODE_PNG_DECODER_C", None)
LODE_PNG_DECODER_C.setSourcePath("third_party/decoder/lodepng/lodepng.c")
LODE_PNG_DECODER_C.setDestPath("gfx/third_party/src/lodepng/")
LODE_PNG_DECODER_C.setProjectPath("config/" + Variables.get("__CONFIGURATION_NAME") + "/gfx/third_party/lodepng/")
LODE_PNG_DECODER_C.setType("SOURCE")
LODE_PNG_DECODER_C.setEnabled(False)