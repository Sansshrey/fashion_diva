from typing import Dict, Any

def search_products(
    query: str,
    color: str = "",
    max_price: str = "",
    size: str = ""
) -> Dict[str, Any]:
    """
    Search the Mr.Shop fashion product catalog.

    Use this tool when the user wants to find or purchase fashion products.
    Results are filtered using the user's query, color, budget, and size.
    """

    products = [
        {
            "id": "prod_001",
            "name": "Classic White Sneakers",
            "category": "shoes",
            "color": "white",
            "brand": "UrbanStep",
            "price": 2999,
            "sizes": ["6", "7", "8", "9", "10"],
            "style": "casual"
        },
        {
            "id": "prod_002",
            "name": "Minimal White Sneakers",
            "category": "shoes",
            "color": "white",
            "brand": "StreetForm",
            "price": 4499,
            "sizes": ["6", "7", "8", "9"],
            "style": "casual"
        },
        {
            "id": "prod_003",
            "name": "Premium White Sneakers",
            "category": "shoes",
            "color": "white",
            "brand": "ModeWalk",
            "price": 5999,
            "sizes": ["7", "8", "9", "10"],
            "style": "premium"
        },
        {
            "id": "prod_004",
            "name": "Black Casual Sneakers",
            "category": "shoes",
            "color": "black",
            "brand": "UrbanStep",
            "price": 3499,
            "sizes": ["6", "7", "8", "9", "10"],
            "style": "casual"
        },
        {
            "id": "prod_005",
            "name": "Beige Oversized Hoodie",
            "category": "tops",
            "color": "beige",
            "brand": "StreetForm",
            "price": 2499,
            "sizes": ["S", "M", "L", "XL"],
            "style": "casual"
        }
    ]

    results = products
    query_lower = query.lower()

    if query_lower:
        results = [
            product for product in results
            if (
                query_lower in product["name"].lower()
                or query_lower in product["category"].lower()
                or query_lower in product["style"].lower()
            )
        ]

    if color:
        results = [
            product for product in results
            if product["color"].lower() == color.lower()
        ]

    if max_price:
        try:
            price_limit = float(
                max_price.replace("₹", "").replace(",", "").strip()
            )

            results = [
                product for product in results
                if product["price"] <= price_limit
            ]
        except Exception:
            pass

    if size:
        results = [
            product for product in results
            if size.upper() in [s.upper() for s in product["sizes"]]
        ]

    return {
        "success": True,
        "query": query,
        "results": results,
        "count": len(results)
    }