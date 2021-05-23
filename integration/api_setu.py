import json


def get_state_id_by_state_name(state_name: str):
    with open("data/state_code.json", "r") as f:
        data = json.load(f)
    not_found = False
    for state in data.get("states"):
        if state.get("state_name") == state_name:
            return state.get("state_id")
        else:
            not_found = True
            continue
    if not_found:
        return None


def get_district_id_from_file(file_path: str, district_name: str):
    with open(file_path, "r") as f:
        data = json.load(f)
    not_found = False
    for dist in data.get("districts"):
        if dist.get("district_name") == district_name:
            return dist.get("district_id")
        else:
            not_found = True
            continue
    if not_found:
        return None


def get_instant_applicable_slots(slot_details: dict, age_group: int):
    master_list = []
    for slot in slot_details.get("centers"):
        if len(slot.get("sessions")) > 0:
            for session in slot.get("sessions"):
                if (
                    session.get("min_age_limit") == age_group
                    and session.get("available_capacity") > 0
                ):
                    # booking_details = {
                    #     "Center Name": slot.get("name"),
                    #     "Address": slot.get("address"),
                    #     "Date": session.get("date"),
                    #     "Available": session.get("available_capacity"),
                    #     "Vaccine Type": session.get("vaccine"),
                    #     "Payment Type": slot.get("fee_type"),
                    #     "Time slots": session.get("slots"),
                    # }
                    booking_details = f"VACCINE AVAILABLE({session.get('min_age_limit')}+)\n{session.get('date')}\n{slot.get('district_name')}-{slot.get('state_name')}\n{slot.get('name')},{slot.get('address')}\n{session.get('available_capacity')} shots\n\nhttps://selfregistration.cowin.gov.in/"
                    master_list.append(booking_details)
    return master_list


def get_applicable_slots(slot_details: dict, age_group: list):
    master_list = []
    for slot in slot_details.get("centers"):
        if len(slot.get("sessions")) > 0:
            for session in slot.get("sessions"):
                for age in age_group:
                    if (
                        session.get("min_age_limit") == age
                        and session.get("available_capacity") > 0
                    ):
                        # booking_details = {
                        #     "Center Name": slot.get("name"),
                        #     "Address": slot.get("address"),
                        #     "Date": session.get("date"),
                        #     "Available": session.get("available_capacity"),
                        #     "Vaccine Type": session.get("vaccine"),
                        #     "Payment Type": slot.get("fee_type"),
                        #     "Time slots": session.get("slots"),
                        # }
                        booking_details = f"VACCINE AVAILABLE({session.get('min_age_limit')}+)\n{session.get('date')}\n{slot.get('district_name')}-{slot.get('state_name')}\n{slot.get('name')},{slot.get('address')}\n{session.get('available_capacity')} shots\n\nhttps://selfregistration.cowin.gov.in/"
                        master_list.append(booking_details)
    return master_list


def get_generic_slots(slot_details: dict, age_group):
    master_list = []
    # n = 0
    # m = 0
    for slot in slot_details.get("centers"):
        if len(slot.get("sessions")) > 0:
            for session in slot.get("sessions"):
                if (
                    session.get("min_age_limit") == 18
                    and session.get("available_capacity") >= 1
                    # and n < 3
                ):
                    booking_details = f"VACCINE AVAILABLE({session.get('min_age_limit')}+)\n{session.get('date')}\n{slot.get('district_name')}-{slot.get('state_name')}\n{slot.get('name')},{slot.get('address')}\nVaccine Type: {session.get('vaccine')}\n{session.get('available_capacity')} shots\n\nhttps://selfregistration.cowin.gov.in/"
                    master_list.append(booking_details)
                    if len(master_list) == 5:
                        return master_list
                    # n += 1
                # elif (
                #     session.get("min_age_limit") == 45
                #     and session.get("available_capacity") > 0
                #     and m < 3
                # ):
                #     booking_details = f"VACCINE AVAILABLE({session.get('min_age_limit')}+)\n{session.get('date')}\n{slot.get('district_name')}-{slot.get('state_name')}\n{slot.get('name')},{slot.get('address')}\n{session.get('available_capacity')} shots\n\nhttps://selfregistration.cowin.gov.in/"
                #     master_list.append(booking_details)
                #     m += 1
    return master_list


def filter_results(slot_details: dict, age_group, dose):
    master_list = []
    n = 0
    if dose is not None:
        dose_filter = f"available_capacity_dose{dose}"
    else:
        dose_filter = "available_capacity"
    for slot in slot_details.get("centers"):
        if len(slot.get("sessions")) > 0:
            for session in slot.get("sessions"):
                if age_group is None:
                    if (
                        session.get("min_age_limit") == 18
                        and session.get(dose_filter) >= 1
                        and n < 3
                    ):
                        booking_details = f"VACCINE AVAILABLE({session.get('min_age_limit')}+)\n{session.get('date')}\n{slot.get('district_name')}-{slot.get('state_name')}\n{slot.get('name')},{slot.get('address')}\nVaccine Type: {session.get('vaccine')}\n1st Dose availablility --> {session.get('available_capacity_dose1')} shots\n2nd Dose availablility --> {session.get('available_capacity_dose2')} shots\n\nRegister now from : https://selfregistration.cowin.gov.in/"
                        master_list.append(booking_details)
                        n += 1
                    elif (
                        session.get("min_age_limit") == 45
                        and session.get(dose_filter) >= 1
                        and n < 6
                    ):
                        booking_details = f"VACCINE AVAILABLE({session.get('min_age_limit')}+)\n{session.get('date')}\n{slot.get('district_name')}-{slot.get('state_name')}\n{slot.get('name')},{slot.get('address')}\nVaccine Type: {session.get('vaccine')}\n1st Dose availablility --> {session.get('available_capacity_dose1')} shots\n2nd Dose availablility --> {session.get('available_capacity_dose2')} shots\n\nRegister now from : https://selfregistration.cowin.gov.in/"
                        master_list.append(booking_details)
                        n += 1
                        if len(master_list) == 6:
                            return master_list
                else:
                    if (
                        session.get("min_age_limit") == int(age_group)
                        and session.get(dose_filter) >= 1
                    ):
                        booking_details = f"VACCINE AVAILABLE({session.get('min_age_limit')}+)\n{session.get('date')}\n{slot.get('district_name')}-{slot.get('state_name')}\n{slot.get('name')},{slot.get('address')}\nVaccine Type: {session.get('vaccine')}\n1st Dose availablility --> {session.get('available_capacity_dose1')} shots\n2nd Dose availablility --> {session.get('available_capacity_dose2')} shots\n\nRegister now from : https://selfregistration.cowin.gov.in/"
                        master_list.append(booking_details)
                        if len(master_list) == 6:
                            return master_list
    return master_list
