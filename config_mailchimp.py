import configparser
config = configparser.RawConfigParser()
config.read('config.properties')

mc_list_id = config.get('mailchimp', 'mc.listid')
mc_username = config.get('mailchimp', 'mc.user')
mc_password = config.get('mailchimp', 'mc.password')
mc_url = config.get('mailchimp', 'mc.url')
mc_custom_template = config.get('mailchimp', 'mc.email.template')


def get_list_id():
    return mc_list_id


def get_credentials():
    return (mc_username, mc_password)


def get_url():
    return mc_url


def get_list_url():
    return "{}/lists/{}".format(get_url(), get_list_id())


def get_template_url():
    return "{}/templates".format(get_url())


def get_custom_email_template():
    return mc_custom_template


def get_campaign_url():
    return "{}/campaigns".format(get_url())


def get_folder_url():
    return "{}/campaign-folders".format(get_url())
