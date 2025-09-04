from typing import List, Dict

def apply_discounts(cart: List[str], products: Dict):
    try:
        total = 0
        cart_copy = cart.copy()
        breakdown = []

        # Rule 1: SWAG Pack (T-Shirt + Mug + Gift Card) 
        swag_price = 2250
        swag_count = min(
            cart_copy.count("TSHIRT"),
            cart_copy.count("GIFT_CARD"),
            cart_copy.count("MUG")
        )
        if swag_count > 0:
            total += swag_count * swag_price
            breakdown.append({
                "product_name": "SWAG Pack (T-Shirt + Gift Card + Mug)",
                "quantity": swag_count,
                "normal_price": (products["TSHIRT"]["price"] +
                                products["GIFT_CARD"]["price"] +
                                products["MUG"]["price"]) * swag_count,
                "discounted_price": swag_count * swag_price
            })
            for _ in range(swag_count):
                cart_copy.remove("TSHIRT")
                cart_copy.remove("GIFT_CARD")
                cart_copy.remove("MUG")

        # Rule 2: Gift Card 2-for-1 
        gift_cards = cart_copy.count("GIFT_CARD")
        if gift_cards > 0:
            normal_price = gift_cards * products["GIFT_CARD"]["price"]
            discounted_price = (gift_cards // 2 + gift_cards % 2) * products["GIFT_CARD"]["price"]
            total += discounted_price
            breakdown.append({
                "product_name": "Gift Card",
                "quantity": gift_cards,
                "normal_price": normal_price,
                "discounted_price": discounted_price
            })
            cart_copy = [item for item in cart_copy if item != "GIFT_CARD"]


        tshirts = cart_copy.count("TSHIRT")
        if tshirts > 0:
            normal_price = tshirts * products["TSHIRT"]["price"]
            if tshirts >= 3:
                discounted_price = tshirts * 1710
                discount_type = "T-Shirt Bulk Discount"
            else:
                discounted_price = normal_price
                discount_type = "T-Shirt Normal Price"
            total += discounted_price
            breakdown.append({
                "product_name": "T-Shirt",
                "quantity": tshirts,
                "normal_price": normal_price,
                "discounted_price": discounted_price,
                "note": discount_type
            })
            cart_copy = [item for item in cart_copy if item != "TSHIRT"]

        for sku in cart_copy:
            if sku not in products:
                breakdown.append({
                    "product_name": sku,
                    "error": "Invalid product, skipped"
                })
                continue
            total += products[sku]["price"]
            breakdown.append({
                "product_name": products[sku]["name"],
                "quantity": 1,
                "normal_price": products[sku]["price"],
                "discounted_price": products[sku]["price"]
            })

        return {
            "total": total,
            "details": breakdown
        }

    except Exception as e:
        return {
            "total": 0,
            "details": [],
            "error": f"{str(e)}"
        }
