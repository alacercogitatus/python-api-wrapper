from cribl_python_api_wrapper.lib.http_operations import *


def get_system_secrets(base_url, cribl_auth_token, verify=True):
    """
    Deprecated - use individual endpoints
    :param base_url:
    :param cribl_auth_token:
    :param verify:
    :return:
    """
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = None

    try:
        return get(base_url + "/system/secrets",
                   headers=headers, payload=payload, verify=verify)

    except Exception as e:
        raise Exception(
            "General exception raised while attempting to get system secrets from Cribl: %s" % str(e))


def create_system_secret(base_url, cribl_auth_token, config, verify=True):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = config

    try:
        return post(base_url + "/system/secrets",
                    headers=headers, payload=payload, verify=verify)
    except Exception as e:
        raise Exception("General exception raised while attempting to create secret: %s " % str(e))


def update_system_secret(base_url, cribl_auth_token, config, verify=True):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = config

    try:
        return patch(base_url + "/system/secrets/" + config["id"],
                     headers=headers, payload=payload, verify=verify)
    except Exception as e:
        raise Exception("General exception raised while attempting to update secret: %s " % str(e))


def delete_system_secret(base_url, cribl_auth_token, item_id, verify=True):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    try:
        return delete(base_url + "/system/secrets/" + item_id,
                      headers=headers, verify=verify)

    except Exception as e:
        raise Exception("General exception raised while attempting to delete secret %s: %s" % (id, str(e)))
