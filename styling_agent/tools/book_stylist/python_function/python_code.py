from typing import Dict, Any
import uuid

def book_stylist(
    stylist_id: str,
    consultation_type: str,
    selected_date: str,
    selected_time: str
) -> Dict[str, Any]:
    """
    Book a consultation with a Mr.Shop stylist or colour analyst.

    Use this tool only after the user has selected a stylist,
    consultation type, date, and available time slot.

    The tool returns a booking confirmation only when the
    booking is successfully created.
    """

    booking_id = "BOOK-" + str(uuid.uuid4())[:8].upper()

    booking = {
        "booking_id": booking_id,
        "stylist_id": stylist_id,
        "consultation_type": consultation_type,
        "date": selected_date,
        "time": selected_time,
        "status": "BOOKED"
    }

    set_variable("booking_status", "BOOKED")
    set_variable("booking_id", booking_id)

    return {
        "success": True,
        "booking": booking,
        "message": "Consultation booked successfully."
    }