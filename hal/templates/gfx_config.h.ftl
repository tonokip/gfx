#ifndef GFX_CONFIG_H
#define GFX_CONFIG_H

#ifndef LIB_EXPORT
#define LIB_EXPORT
#endif

#define GFX_MAX_BUFFER_COUNT    2
#define GFX_DRIVER_COUNT        1
#define GFX_DISPLAY_COUNT       1
<#if ProcInfoFunction?? && ProcInfoFunction?hasContent>
#define GFX_PROCESSOR_COUNT     1
</#if>

/* configuration flags */
#define GFX_DRAW_PIPELINE_ENABLED     <#if DrawPipelineEnable == true>1<#else>0</#if>
#define GFX_ALPHA_BLENDING_ENABLED    <#if AlphaBlendingEnable == true>1<#else>0</#if>
#define GFX_BOUNDS_CLIPPING_ENABLED   <#if BoundsClippingEnable == true>1<#else>0</#if>
#define GFX_COLOR_CONVERSION_ENABLED  <#if ColorConversionEnable == true>1<#else>0</#if>
#define GFX_COLOR_MASKING_ENABLED     <#if ColorMaskingEnable == true>1<#else>0</#if>
#define GFX_LAYER_CLIPPING_ENABLED    <#if LayerClippingEnable == true>1<#else>0</#if>
#define GFX_ORIENTATION_ENABLED       <#if DisplayOrientationEnable == true>1<#else>0</#if>

#define GFX_DRAW_ARC_ENABLED           <#if DrawArcEnable == true>1<#else>0</#if>
#define GFX_DRAW_ELLIPSE_ENABLED       <#if DrawEllipseEnable == true>1<#else>0</#if>


#endif /* GFX_CONFIG_H */