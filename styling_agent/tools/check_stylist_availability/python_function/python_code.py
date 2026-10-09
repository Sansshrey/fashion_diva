from typing import Dict, Any


def check_stylist_availability(
    stylist_id: str,
    selected_date: str,
    preferred_time: str = ""
) -> Dict[str, Any]:
    """
    Check available consultation slots for a selected Mr.Shop stylist.

    Use this before booking a consultation.
    Never claim a slot is available without checking this tool.
    """

    valid_stylists = {
        "stylist_001",
        "stylist_002",
        "stylist_003"
    }

    if not stylist_id:
        return {
            "success": False,
            "message": "A stylist must be selected before checking availability.",
            "available_slots": [],
            "count": 0
        }

    if stylist_id not in valid_stylists:
        return {
            "success": False,
            "message": "The selected stylist could not be found.",
            "available_slots": [],
            "count": 0
        }

    if not selected_date:
        return {
            "success": False,
            "message": "A consultation date is required.",
            "available_slots": [],
            "count": 0
        }

    # Prototype availability
    slots = [
        "11:00 AM",
        "2:00 PM",
        "5:00 PM"
    ]

    # Filter by preferred time when provided
    if preferred_time:
        requested_time = preferred_time.lower().strip()

        matching_slots = [
            slot
            for slot in slots
            if requested_time in slot.lower()
            or slot.lower() in requested_time
        ]

        slots = matching_slots

    return {
        "success": True,
        "stylist_id": stylist_id,
        "date": selected_date,
        "available_slots": slots,
        "count": len(slots),
        "message": (
            f"{len(slots)} consultation slot(s) are available."
            if slots
            else "No matching consultation slots are available."
        )
    }