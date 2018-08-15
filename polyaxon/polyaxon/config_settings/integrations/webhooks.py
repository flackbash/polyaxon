from polyaxon.config_manager import config

INTEGRATIONS_WEBHOOKS = config.get_dict('POLYAXON_INTEGRATIONS_WEBHOOKS',
                                        is_list=True,
                                        is_optional=True,
                                        is_local=True)
