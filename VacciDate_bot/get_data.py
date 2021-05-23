import json
import os
from integration.api_setu import (
    get_applicable_slots,
    get_district_id_from_file,
    get_state_id_by_state_name,
)
from utils.external_caller import APIInterface
from utils.load_config import load_configuration

config = load_configuration(config_path="data/config.yml")


def get_state_list():
    with open("data/state_code.json", "r") as f:
        data = json.load(f)
    list_state = []
    for states in data["states"]:
        list_state.append(f"{states['state_id']} : {states['state_name']}")
    state_text = "\n".join(list_state)
    return state_text


def get_all_districts(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
    list_dist = []
    for districts in data["districts"]:
        list_dist.append(f"{districts['district_id']} : {districts['district_name']}")
    dist_text = "\n".join(list_dist)
    return dist_text


def get_district_list(state_id: int):
    file_path = f"data/district_data/{state_id}.json"
    if os.path.isfile(file_path):
        dist_text = get_all_districts(
            file_path=file_path,
        )
        return dist_text
    else:
        get_district_url = config.get("COWIN").get("GET_ALL_DISTICTS")
        data = json.loads(APIInterface().get(route=f"{get_district_url}/{state_id}"))
        with open(file_path, "w") as f:
            json.dump(data, f)
        list_dist = []
        for districts in data["districts"]:
            list_dist.append(
                f"{districts['district_id']} : {districts['district_name']}"
            )
        dist_text = "\n".join(list_dist)
        return dist_text
