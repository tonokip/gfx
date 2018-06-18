#ifndef GFXU_CONFIG_H
#define GFXU_CONFIG_H

#ifndef LIB_EXPORT
#define LIB_EXPORT
#endif

#define GFX_UTIL_JPEG_DECODER_ENABLED       <#if JPEGEnable == true>1<#else>0</#if>
#define GFX_UTIL_PNG_DECODER_ENABLED       <#if PNGEnable == true>1<#else>0</#if>

#endif /* GFXU_CONFIG_H */