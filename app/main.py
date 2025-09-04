from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from app.utils import apply_discounts

app = FastAPI(
    title="Checkout API",
)

# if you want to make it more realistic, i can use uuid
products = {
    "TSHIRT": {"name": "T-Shirt", "price": 1900},
    "MUG": {"name": "Coffee Mug", "price": 700},
    "GIFT_CARD": {"name": "Gift Card", "price": 500}
}

class CartRequest(BaseModel):
    items: List[str]

@app.get("/products")
def get_products():
    """Return available products"""
    try:
        return {"products": products}
    except Exception:
        raise HTTPException(status_code=500, detail="Could not fetch products")

@app.post("/checkout")
def checkout(cart: CartRequest):
    """Apply discounts on cart items and return total"""
    try:
        if not cart.items:
            raise HTTPException(status_code=400, detail="Cart is empty")
        for item in cart.items:
            if item not in products:
                raise HTTPException(status_code=400, detail=f"Invalid product id: {item}")

        result = apply_discounts(cart.items, products)
        return {
            "cart_items": cart.items,
            "summary": result
        }
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{str(e)}")
