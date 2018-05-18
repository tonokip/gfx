DrawPipelineEnable = halComponent.createBooleanSymbol("DrawPipelineEnable", None)
DrawPipelineEnable.setLabel("Draw Pipeline Configuration")
DrawPipelineEnable.setDefaultValue(True)
DrawPipelineEnable.setDescription("<html>Disables the entire draw pipeline.<br>Disable this if the HAL native rasterizer is not needed.</html>")

DrawPipelineStagesMenu = halComponent.createMenuSymbol("DrawPipelineStages", DrawPipelineEnable)
DrawPipelineStagesMenu.setLabel("Draw Pipeline Stages")
DrawPipelineStagesMenu.setDescription("Configure individual pixel pipeline stages.")
DrawPipelineStagesMenu.setDependencies(onDrawPipelineEnableChanged, ["DrawPipelineEnable"])

AlphaBlendingEnable = halComponent.createBooleanSymbol("AlphaBlendingEnable", DrawPipelineStagesMenu)
AlphaBlendingEnable.setLabel("Alpha Blending")
AlphaBlendingEnable.setDescription("<html>Enables the alpha blending stage.<br>Any form of pixel color blending support requires this stage.</html>")
AlphaBlendingEnable.setDefaultValue(True)

BoundsClippingEnable = halComponent.createBooleanSymbol("BoundsClippingEnable", DrawPipelineStagesMenu)
BoundsClippingEnable.setLabel("Bounds Clipping")
BoundsClippingEnable.setDescription("<html>Enables discrete boundary area clipping.<br>Draw operations may render outside of boundary<br>limitations if this stage is disabled.</html>")
BoundsClippingEnable.setDefaultValue(True)

LayerClippingEnable = halComponent.createBooleanSymbol("LayerClippingEnable", DrawPipelineStagesMenu)
LayerClippingEnable.setLabel("Layer Clipping")
LayerClippingEnable.setDescription("<html>Enables discrete layer bounds clipping.<br>Draw operations may render outside of the memoryarea of a<br>frame buffer and cause undefined application behavior.</html>")
LayerClippingEnable.setDefaultValue(True)

ColorConversionEnable = halComponent.createBooleanSymbol("ColorConversionEnable", DrawPipelineStagesMenu)
ColorConversionEnable.setLabel("Color Format Conversion")
ColorConversionEnable.setDescription("<html>Enables per-pixel color format conversion.<br>This is not needed if all draw operations use the same<br>color format as the target frame buffer.</html>")
ColorConversionEnable.setDefaultValue(True)

ColorMaskingEnable = halComponent.createBooleanSymbol("ColorMaskingEnable", DrawPipelineStagesMenu)
ColorMaskingEnable.setLabel("Color Masking")
ColorMaskingEnable.setDescription("<html>Enables per-pixel color discard stage.<br>Color masking involves discarding all pixels of<br>a certain color to achieve a form of transparency.</html>")
ColorMaskingEnable.setDefaultValue(True)

DisplayOrienetationEnable = halComponent.createBooleanSymbol("DisplayOrientationEnable", DrawPipelineStagesMenu)
DisplayOrienetationEnable.setLabel("Display Orientation")
DisplayOrienetationEnable.setDescription("<html>Enables per-pixel orientation transformation stage.<br>This stage allows displays to be orthogonally rotated.</html>")
DisplayOrienetationEnable.setDefaultValue(True)

DisplayMirroringEnable = halComponent.createBooleanSymbol("DisplayMirroringEnable", DrawPipelineStagesMenu)
DisplayMirroringEnable.setLabel("Display Mirroring")
DisplayMirroringEnable.setDescription("<html>Enables per-pixel mirror transformation stage.<br>This stage allows displays to be mirrored.</html>")
DisplayMirroringEnable.setDefaultValue(True)

PrimitiveInterfacesMenu = halComponent.createMenuSymbol("PrimitiveInterfacesMenu", DrawPipelineEnable)
PrimitiveInterfacesMenu.setLabel("Primitive Interface Configuration")
PrimitiveInterfacesMenu.setDescription("Configure individual primitive drawing interfaces.")
PrimitiveInterfacesMenu.setDependencies(onDrawPipelineEnableChanged, ["DrawPipelineEnable"])

DrawArcEnable = halComponent.createBooleanSymbol("DrawArcEnable", PrimitiveInterfacesMenu)
DrawArcEnable.setLabel("Arc")
DrawArcEnable.setDescription("Enables Arc primitive drawing interface.")
DrawArcEnable.setDefaultValue(True)

DrawEllipseEnable = halComponent.createBooleanSymbol("DrawEllipseEnable", PrimitiveInterfacesMenu)
DrawEllipseEnable.setLabel("Ellipse")
DrawEllipseEnable.setDescription("Enables Ellipse primitive drawing interface.")
DrawEllipseEnable.setDefaultValue(True)

ImageDecodersMenu = halComponent.createMenuSymbol("ImageDecoderMenu", DrawPipelineEnable)
ImageDecodersMenu.setLabel("Image Decoder Configuration")
ImageDecodersMenu.setDescription("Configure image decoder systems.")
ImageDecodersMenu.setDependencies(onDrawPipelineEnableChanged, ["DrawPipelineEnable"])

JPEGEnable = halComponent.createBooleanSymbol("JPEGEnable", ImageDecodersMenu)
JPEGEnable.setLabel("JPEG")
JPEGEnable.setDescription("Enables software JPEG image decoder.")
JPEGEnable.setDefaultValue(True)

PNGEnable = halComponent.createBooleanSymbol("PNGEnable", ImageDecodersMenu)
PNGEnable.setLabel("PNG")
PNGEnable.setDescription("Enables software PNG image decoder.")
PNGEnable.setDefaultValue(True)




