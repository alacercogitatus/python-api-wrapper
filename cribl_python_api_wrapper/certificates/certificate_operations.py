from cribl_python_api_wrapper.lib.http_operations import *


def get_certificates(base_url, cribl_auth_token, verify=True):
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
        return get(base_url + "/system/certificates",
                   headers=headers, payload=payload, verify=verify)

    except Exception as e:
        raise Exception(
            "General exception raised while attempting to get system certificates from Cribl: %s" % str(e))


def create_system_certificate(base_url, cribl_auth_token, config, verify=True):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = config

    try:
        return post(base_url + "/system/certificates",
                    headers=headers, payload=payload, verify=verify)
    except Exception as e:
        raise Exception("General exception raised while attempting to create certificate: %s " % str(e))


def update_system_certificate(base_url, cribl_auth_token, config, verify=True):
    headers = {"Content-type": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    payload = config

    try:
        return patch(base_url + "/system/certificates/" + config["id"],
                     headers=headers, payload=payload, verify=verify)
    except Exception as e:
        raise Exception("General exception raised while attempting to update certificate: %s " % str(e))


def delete_system_certificate(base_url, cribl_auth_token, item_id, verify=True):
    headers = {"Content-type": "application/json",
               "Accept": "application/json",
               "Authorization": "Bearer " + cribl_auth_token}
    try:
        return delete(base_url + "/system/certificates/" + item_id,
                      headers=headers, verify=verify)

    except Exception as e:
        raise Exception("General exception raised while attempting to delete certificate %s: %s" % (id, str(e)))
