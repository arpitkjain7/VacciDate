from datetime import datetime
from utils.api_call import api_setu_get_slot_by_district, api_setu_get_slot_by_pincode
from integration.api_setu import filter_results
from VacciDate_bot.send_message import send_message
import time
import argparse


today = datetime.now()
start_date = today.strftime("%d-%m-%Y")


def search_slots_with_pin_code(pincode: str, age_group: str = None, dose: str = None):
    for i in range(2):
        try:
            print(f"New job started at {datetime.now()}")
            slot_details = api_setu_get_slot_by_pincode(
                pincode=pincode, start_date=start_date
            )
            available_slots = filter_results(
                slot_details, age_group=age_group, dose=dose
            )
            if len(available_slots) > 0:
                print(f"slot available in {pincode}")
                for i in range(min(6, len(available_slots))):
                    success = send_message(text=available_slots[i])
                    if not success:
                        break
            time.sleep(30)
        except Exception as error:
            print(f"Error in main.py : {error}")
            continue


def search_slots_with_district_id(
    dist_code: str, age_group: str = None, dose: str = None
):
    for i in range(2):
        try:
            print(f"New job started at {datetime.now()}")
            slot_details = api_setu_get_slot_by_district(
                district_id=dist_code, start_date=start_date
            )
            available_slots = filter_results(
                slot_details, age_group=age_group, dose=dose
            )
            if len(available_slots) > 0:
                print(f"slot available in {dist_code}")
                for i in range(min(6, len(available_slots))):
                    success = send_message(text=available_slots[i])
                    if not success:
                        break
            time.sleep(30)
        except Exception as error:
            print(f"Error in main.py : {error}")
            continue


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "-d", "--district_id", required=True, help="provide disctrict id from the list"
    )
    ap.add_argument(
        "-p",
        "--pincode",
        required=False,
        help="provide the pincode go get notification to be filtered by Pin-code.",
    )
    ap.add_argument(
        "-a",
        "--age_group",
        required=False,
        help="provide age group you need to track for. Enter 18 for 18+ and 45 for 45+. If left blank notification will be sent for both 18+ and 45+",
    )
    ap.add_argument(
        "-dose",
        "--dose",
        required=False,
        help="which dose do you want notification for. Enter 1 if you want notification for 1st dose and 2 if you want notification for 2nd dose. If left blank notification will be for both 1st and 2nd dose",
    )
    args = vars(ap.parse_args())
    if args["district_id"] is not None:
        if args["pincode"] is not None:
            search_slots_with_pin_code(
                pincode=args["pincode"],
                age_group=args["age_group"],
                dose=args["dose"],
            )
        else:
            search_slots_with_district_id(
                dist_code=args["district_id"],
                age_group=args["age_group"],
                dose=args["dose"],
            )
