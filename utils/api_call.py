from integration.api_setu import (
    get_applicable_slots,
    get_district_id_from_file,
    get_state_id_by_state_name,
    get_instant_applicable_slots,
)
from utils.load_config import load_configuration
from utils.external_caller import APIInterface
import time
from VacciDate_bot.send_message import send_personal_message
import json

config = load_configuration(config_path="data/config.yml")
get_slot_by_district = config.get("COWIN").get("SLOT_BY_DISTICT")
get_slot_by_pincode = config.get("COWIN").get("SLOT_BY_PINCODE")


def api_setu_get_slot_by_district(district_id, start_date):
    try:
        slot_details = json.loads(
            APIInterface.get(
                route=get_slot_by_district,
                params={"district_id": district_id, "date": start_date},
            )
        )
        return slot_details
    except Exception as error:
        print(f"Exception in api_setu_get_slot_by_district function : {error}")
        return None


def api_setu_get_slot_by_pincode(pincode, start_date):
    try:
        slot_details = json.loads(
            APIInterface.get(
                route=get_slot_by_pincode,
                params={"pincode": pincode, "date": start_date},
            )
        )
        return slot_details
    except Exception as error:
        print(f"Exception in api_setu_get_slot_by_pincode function : {error}")
        return None


def get_details(district_id, start_date, age_group, chat_id):
    try:
        slot_details = json.loads(
            APIInterface.get(
                route=get_slot_by_district,
                params={"district_id": district_id, "date": start_date},
            )
        )
        if len(age_group) == 0:
            age_group.append(18)
        available_slots = get_applicable_slots(
            slot_details=slot_details, age_group=age_group
        )
        if len(available_slots) > 0:
            print("slot available")
            # message = "\n".join(available_slots)
            # try:
            for i in range(min(5, len(available_slots))):
                # response_status, sleep_time = send_mess(text=available_slots[i],chat_id)
                # if not response_status:
                #     print(f"sleeping for {sleep_time} seconds")
                #     time.sleep(sleep_time)
                send_personal_message(msg=available_slots[i], chat_id=chat_id)
        return True
    except Exception as error:
        print(f"Exception in get_details function : {error}")
        return False


def get_instant_details(district_id, start_date, age_group):
    slot_details = json.loads(
        APIInterface.get(
            route=get_slot_by_district,
            params={"district_id": district_id, "date": start_date},
        )
    )
    available_slots = get_instant_applicable_slots(
        slot_details=slot_details, age_group=age_group
    )
    return available_slots[:5]