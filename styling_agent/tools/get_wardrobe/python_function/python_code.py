import json
from typing import Dict, Any

def get_wardrobe() -> Dict[str, Any]:
    """
    Retrieve all clothing and fashion items stored
    in the user's digital wardrobe.
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

    return {
        "success": True,
        "total_items": len(wardrobe_items),
        "wardrobe_items": wardrobe_items
    }