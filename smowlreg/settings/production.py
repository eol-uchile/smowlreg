def plugin_settings(settings):
    settings.SMOWLREG_CONTROLLER_REG_BASE_URL = settings.ENV_TOKENS.get('SMOWLREG_CONTROLLER_REG_BASE_URL', '')
    settings.SMOWL_KEY = settings.ENV_TOKENS.get('SMOWL_KEY', '')
    settings.SMOWL_ENTITY = settings.ENV_TOKENS.get('SMOWL_ENTITY', '')
    settings.SMOWLREG_CONTROLLER_REG_FULL_URL = '{}?entity_Name={}&swlLicenseKey={}&type=4'.format(settings.SMOWLREG_CONTROLLER_REG_BASE_URL, settings.SMOWL_ENTITY, settings.SMOWL_KEY)
    settings.SMOWLREG_CHECKBBLINK = settings.ENV_TOKENS.get('SMOWLREG_CHECKBBLINK', '')
    settings.SMOWLREG_CHECKBBLINK_FULL_URL = '{}?entity_Name={}&lang=en&showB=false'.format(settings.SMOWLREG_CHECKBBLINK, settings.SMOWL_ENTITY)