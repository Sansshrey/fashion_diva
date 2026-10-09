import json
from typing import Dict, Any

def update_wardrobe_item(
    item_name: str,
    new_item_name: str = "",
    category: str = "",
    color: str = "",
    brand: str = "",
    size: str = "",
    material: str = "",
    style: str = "",
    occasion: str = ""
) -> Dict[str, Any]:
    """
    Update details of an existing clothing or fashion item
    in the user's digital wardrobe.

    Use this tool when the user explicitly asks to change,
    edit, or update information about an existing wardrobe item.
    Do not invent values that the user did not provide.
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

    matching_index = None

    for index, item in enumerate(wardrobe_items):
        if item.get("item_name", "").lower().strip() == item_name_lower:
            matching_index = index
            break

    if matching_index is None:
        return {
            "success": False,
            "message": f"I couldn't find '{item_name}' in your wardrobe.",
            "total_items": len(wardrobe_items)
        }

    item = wardrobe_items[matching_index]

    updates = {
        "item_name": new_item_name,
        "category": category,
        "color": color,
        "brand": brand,
        "size": size,
        "material": material,
        "style": style,
        "occasion": occasion
    }

    changed_fields = {}

    for field, value in updates.items():
        if value != "":
            item[field] = value
            changed_fields[field] = value

    wardrobe_items[matching_index] = item

    set_variable(
        "wardrobe_items",
        json.dumps(wardrobe_items)
    )

    set_variable(
        "current_wardrobe_item",
        json.dumps(item)
    )

    return {
        "success": True,
        "updated_item": item,
        "changed_fields": changed_fields,
        "total_items": len(wardrobe_items),
        "message": f"{item.get('item_name')} has been updated in your wardrobe."
    }