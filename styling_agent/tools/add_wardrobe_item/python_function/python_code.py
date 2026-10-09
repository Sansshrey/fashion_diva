import json
import uuid
from datetime import datetime
from typing import Dict, Any

def add_wardrobe_item(
    item_name: str,
    category: str,
    color: str = "",
    brand: str = "",
    size: str = "",
    material: str = "",
    style: str = "",
    occasion: str = "",
    image_url: str = ""
) -> Dict[str, Any]:
    """
    Add a new clothing or fashion item to the user's digital wardrobe.

    Use this tool when the user uploads or describes a new wardrobe item.
    Store only information provided by the user. Do not invent missing attributes.
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

    item = {
        "id": str(uuid.uuid4()),
        "item_name": item_name,
        "category": category,
        "color": color,
        "brand": brand,
        "size": size,
        "material": material,
        "style": style,
        "occasion": occasion,
        "image_url": image_url,
        "added_at": datetime.utcnow().isoformat()
    }

    wardrobe_items.append(item)

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
        "item": item,
        "total_items": len(wardrobe_items),
        "message": f"{item_name} added to your wardrobe."
    }