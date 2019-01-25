// <editor-fold defaultstate="collapsed" desc="DRV_GFX2D Initialization Data">


/* GFX2D PLib Interface Initialization */
const DRV_GFX2D_PLIB_INTERFACE drvGfx2DPLibAPI = {

    /* GFX2D PLib Fill function */
    .fill = GFX2D_Fill,

    /* GFX2D PLib Copy function */
    .copy = GFX2D_Copy,

    /* GFX2D PLib Blend function */
    .blend = GFX2D_Blend,

    /* GFX2D PLib Status function */
    .statusGet = GFX2D_StatusGet,

    /* GF2X2D PLib Callback Register */
    .callbackRegister = GFX2D_CallbackRegister,
};

/* GFX2D Driver Initialization Data */
const DRV_GFX2D_INIT drvGfx2DInitData =
{
    /* GFX2D PLib API */
    .gfx2DPlib = &drvGfx2DPLibAPI,

    /* GFX2D IRQ */
//    .interruptGFX2D = DRV_GFX2D_INT_SRC
};

// </editor-fold>
