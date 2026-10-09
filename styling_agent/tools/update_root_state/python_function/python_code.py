def update_root_state(
    active_intent: str = "",
    previous_intent: str = "",
    current_topic: str = "",
    current_wardrobe_item: str = "",
    current_product: str = "",
    selected_product: str = "",
    selected_stylist: str = "",
    preferred_style: str = "",
    preferred_color: str = "",
    budget: str = "",
    occasion: str = "",
    consultation_type: str = "",
    selected_date: str = "",
    selected_time: str = "",
    booking_status: str = ""
) -> dict:

    updates = {
        "active_intent": active_intent,
        "previous_intent": previous_intent,
        "current_topic": current_topic,
        "current_wardrobe_item": current_wardrobe_item,
        "current_product": current_product,
        "selected_product": selected_product,
        "selected_stylist": selected_stylist,
        "preferred_style": preferred_style,
        "preferred_color": preferred_color,
        "budget": budget,
        "occasion": occasion,
        "consultation_type": consultation_type,
        "selected_date": selected_date,
        "selected_time": selected_time,
        "booking_status": booking_status
    }

    saved = {}

    for name, value in updates.items():
        if value != "":
            set_variable(name, value)
            saved[name] = value

    return {
        "success": True,
        "saved": saved
    }