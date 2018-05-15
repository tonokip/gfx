testfile

testInt is ${testInt}

<#list 0..1 as i>

<#assign cfgIdx = "gfx_hal_${i}.testInt${i}"?eval>

<#-- ********** Debug Code  *********** -->
${gfx_hal_0.testInt0}
${gfx_hal_0.testInt0}
${gfx_hal_1.testInt1}
${gfx_hal_1.testInt1}
<#-- ********************************* -->

var is ${"gfx_hal_${i}.testInt${i}"?eval}

<#if cfgIdx??>
cfgIdx is ${cfgIdx?eval}
testInt${i}

</#if>
</#list>
