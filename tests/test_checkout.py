import pytest
from app.main import products
from app.utils import apply_discounts 


def test_empty_cart():
    result = apply_discounts([], products)
    assert result["total"] == 0
    assert result["details"] == []


def test_single_tshirt_no_discount():
    cart = ["TSHIRT"]
    result = apply_discounts(cart, products)
    assert result["total"] == 1900
    assert len(result["details"]) == 1
    assert result["details"][0]["discounted_price"] == 1900


def test_tshirt_bulk_discount():
    cart = ["TSHIRT", "TSHIRT", "TSHIRT"]
    result = apply_discounts(cart, products)
    assert result["total"] == 5130
    assert result["details"][0]["discounted_price"] == 5130
    assert result["details"][0]["note"] == "T-Shirt Bulk Discount"


def test_giftcard_offer():
    cart = ["GIFT_CARD", "GIFT_CARD"]
    result = apply_discounts(cart, products)
    assert result["total"] == 500
    assert result["details"][0]["discounted_price"] == 500


def test_swag_pack_discount():
    cart = ["TSHIRT", "MUG", "GIFT_CARD"]
    result = apply_discounts(cart, products)
    assert result["total"] == 2250
    assert result["details"][0]["product_name"].startswith("SWAG Pack")
    assert result["details"][0]["discounted_price"] == 2250


def test_mixed_cart():
    cart = ["TSHIRT", "TSHIRT", "MUG", "GIFT_CARD", "TSHIRT", "GIFT_CARD"]
    result = apply_discounts(cart, products)
    expected_total = 2250 + 3420 + 0  
    assert result["total"] == expected_total

    assert any(item["product_name"].startswith("SWAG Pack") for item in result["details"])
    assert any(item["product_name"] == "T-Shirt" for item in result["details"])


def test_invalid_product():
    cart = ["INVALID_ITEM", "TSHIRT"]
    result = apply_discounts(cart, products)

    assert result["total"] == 1900  
    assert any("error" in item for item in result["details"])
