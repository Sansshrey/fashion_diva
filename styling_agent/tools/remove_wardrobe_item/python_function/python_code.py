import json
from typing import Dict, Any

def remove_wardrobe_item(
    item_name: str
) -> Dict[str, Any]:
    """
    Remove a clothing or fashion item from the user's digital wardrobe.

    Use this tool when the user explicitly asks to remove or delete
    an item from their wardrobe.
    """

    existing = get_variable("wardrobe_items")

    if existing is None or existing == "":
        wardrobe_items = []
    elif isinstance(existing, str):
        try:
            wardrobe_items = json.loads(existing)
        except Exception:
            wardrobe_items = []
    else:
        wardrobe_items = existing

    item_name_lower = item_name.lower().strip()

    matching_items = [
        item for item in wardrobe_items
        if item.get("item_name", "").lower().strip() == item_name_lower
    ]

    if not matching_items:
        return {
            "success": False,
            "message": f"I couldn't find '{item_name}' in your wardrobe.",
            "total_items": len(wardrobe_items)
        }

    removed_item = matching_items[0]

    wardrobe_items = [
        item for item in wardrobe_items
        if item.get("id") != removed_item.get("id")
    ]

    set_variable(
        "wardrobe_items",
        json.dumps(wardrobe_items)
    )

    return {
        "success": True,
        "removed_item": removed_item,
        "total_items": len(wardrobe_items),
        "message": f"{removed_item.get('item_name')} removed from your wardrobe."
    }