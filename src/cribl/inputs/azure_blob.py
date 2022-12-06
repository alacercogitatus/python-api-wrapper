from .input_operations import create_input, update_input, delete_input
from ..lib.data_validation import validate_payload
import inflection

source_type = "azure_blob"

all_fields = {
    "id": str,
    "type": str,
    "disabled": bool,
    "pipeline": str,
    "sendToRoutes": bool,
    "environment": str,
    "pqEnabled": bool,
    "streamtags": list,
    "connections": list,
    "pq": dict,
    "queueName": str,
    "fileFilter": str,
    "visibilityTimeout": int,
    "numReceivers": int,
    "maxMessages": int,
    "servicePeriodSecs": int,
    "skipOnError": bool,
    "metadata": list,
    "breakerRulesets": list,
    "staleChannelFlushMs": int,
    "parquetChunkSizeMB": int,
    "authType": str,
    "connectionString": str,
    "textSecret": str
}

required_fields = ["id", "type", "queueName", "connectionString"]


def create_azure_blob_source(base_url, cribl_auth_token, source_id, queue_name, connection_string, disabled=False,
                             pipeline=None,
                             send_to_routes=True,
                             persistent_queue_enabled=False,
                             streamtags=None,
                             environment=None,
                             connections=None,
                             pq=None,
                             breaker_rulesets=None,
                             file_filter="/.*/",
                             visibility_timeout=600,
                             num_receivers=1,
                             max_messages=1,
                             service_period_secs=5,
                             skip_on_error=False,
                             metadata=None,
                             breakerRulesets=None,
                             stale_channel_flush_ms=10000,
                             parquet_cloud_size_mb=5,
                             parquet_chunk_download_timeout=600,
                             auth_type=None,
                             text_secret=None,
                             worker_group=None
                             ):
    payload = {
        "id": source_id,
        "type": source_type
    }

    for field in all_fields.keys():
        cml_field = inflection.underscore(field)
        if cml_field in locals() and locals()[cml_field] is not None:
            payload[field] = locals()[cml_field]

    try:
        payload, missing_required_fields, incorrectly_formatted_fields = \
            validate_payload(payload, all_fields, required_fields)
        if len(missing_required_fields) != 0:
            raise Exception("Missing the following required fields for update: %s" % missing_required_fields)
        elif len(incorrectly_formatted_fields) != 0:
            raise Exception(
                "The following fields were incorrectly formatted. Check payload and try again: %s" %
                incorrectly_formatted_fields)
        else:
            return create_input(base_url, cribl_auth_token, payload, worker_group)

    except:
        raise


def update_azure_blob_source(base_url, cribl_auth_token, source_id, update_data, worker_group=None):
    update_data["id"] = source_id
    update_data["type"] = source_type

    try:
        update_data, missing_required_fields, incorrectly_formatted_fields = \
            validate_payload(update_data, all_fields, required_fields)

        if len(missing_required_fields) != 0:
            raise Exception("Missing the following required fields for update: %s" % missing_required_fields)
        elif len(incorrectly_formatted_fields) != 0:
            raise Exception(
                "The following fields were incorrectly formatted. Check payload and try again: %s" %
                incorrectly_formatted_fields)
        else:
            return update_input(base_url, cribl_auth_token, source_id, update_data, worker_group)

    except:
        raise


def delete_azure_blob_source(base_url, cribl_auth_token, source_id, worker_group=None):
    try:
        return delete_input(base_url, cribl_auth_token, source_id, worker_group)
    except:
        raise
