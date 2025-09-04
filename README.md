# Checkout API (FastAPI)

A simple and clear checkout API built with FastAPI.  
This API demonstrates different types of discounts such as SWAG Pack, Gift Card 2-for-1, and T-Shirt bulk discount.

---

## How to Run

```bash
# 1. Create a virtual environment (optional)
python3 -m venv env
source env/bin/activate   # Windows: env\Scripts\activate

# 2. Install dependencies
pip install fastapi uvicorn pydantic

# Install dependencies from requirements.txt:
pip install -r requirements.txt

# 3. Run the server
uvicorn app.main:app --reload
```

---

## API Endpoints

### GET /products
Returns a list of all available products and their prices.

### POST /checkout
Accepts a list of item codes and returns the total price with applied discounts.