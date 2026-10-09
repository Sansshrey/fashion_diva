from typing import Dict, Any


def get_stylists(
    stylist_type: str = "",
    consultation_type: str = ""
) -> Dict[str, Any]:

    stylists = [
        {
            "id": "stylist_001",
            "name": "Ananya",
            "type": "fashion_stylist",
            "specialty": "casual and wardrobe styling",
            "consultation_types": ["STYLING", "WARDROBE"],
            "modes": ["ONLINE", "IN_PERSON"],
            "price": 999
        },
        {
            "id": "stylist_002",
            "name": "Riya",
            "type": "fashion_stylist",
            "specialty": "occasion and personal styling",
            "consultation_types": ["STYLING", "OCCASION"],
            "modes": ["ONLINE", "IN_PERSON"],
            "price": 1299
        },
        {
            "id": "stylist_003",
            "name": "Meera",
            "type": "colour_analyst",
            "specialty": "personal colour analysis",
            "consultation_types": ["COLOUR_ANALYSIS"],
            "modes": ["ONLINE", "IN_PERSON"],
            "price": 1499
        }
    ]

    results = stylists

    # ---------------------------------------------------------
    # STYLIST TYPE
    # ---------------------------------------------------------

    requested_type = (stylist_type or "").lower().strip()

    if requested_type:

        if any(x in requested_type for x in [
            "personal stylist",
            "personal styling",
            "fashion stylist",
            "fashion styling"
        ]) or requested_type in ["stylist", "personal", "fashion"]:

            requested_type = "fashion_stylist"

        elif any(x in requested_type for x in [
            "colour analyst",
            "color analyst",
            "colour analysis",
            "color analysis"
        ]) or requested_type in ["colour", "color"]:

            requested_type = "colour_analyst"

        else:
            requested_type = ""

        # Only filter if we successfully understood the type
        if requested_type:
            results = [
                stylist
                for stylist in results
                if stylist["type"] == requested_type
            ]

    # ---------------------------------------------------------
    # CONSULTATION TYPE / MODE
    # ---------------------------------------------------------

    requested_consultation = (consultation_type or "").lower().strip()

    if requested_consultation:

        if any(x in requested_consultation for x in [
            "online",
            "virtual",
            "remote"
        ]):

            results = [
                stylist
                for stylist in results
                if "ONLINE" in stylist["modes"]
            ]

        elif any(x in requested_consultation for x in [
            "in person",
            "in-person",
            "offline"
        ]):

            results = [
                stylist
                for stylist in results
                if "IN_PERSON" in stylist["modes"]
            ]

        elif requested_consultation.upper() in [
            "STYLING",
            "WARDROBE",
            "OCCASION",
            "COLOUR_ANALYSIS"
        ]:

            results = [
                stylist
                for stylist in results
                if requested_consultation.upper()
                in stylist["consultation_types"]
            ]

        # IMPORTANT:
        # Ignore unknown consultation values instead of returning 0.
        else:
            pass

    return {
        "success": True,
        "stylists": results,
        "count": len(results),
        "message": (
            "Matching stylists found."
            if results
            else "No matching stylists found."
        )
    }