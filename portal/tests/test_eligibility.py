from portal.services.eligibility import evaluate_eligibility, load_rules
from portal.services.mapper import map_order


def test_evaluate_eligibility_flags_digital_items() -> None:
    raw = {
        "order_number": "RMA-X",
        "email": "a@b.com",
        "zip": "12345",
        "purchased_at": "2025-12-01T10:00:00Z",
        "delivered_at": "2025-12-02T10:00:00Z",
        "return_window_days": 30,
        "items": [
            {
                "sku": "DIGI-1",
                "name": "Digital",
                "category": "digital",
                "quantity": 1,
                "quantity_returned": 0,
                "price": 10.0,
                "digital": True,
                "final_sale": False,
            }
        ],
    }
    order = map_order(raw)
    rules = load_rules()
    results = evaluate_eligibility(order, rules)
    assert results[0].returnable is False
    assert results[0].flag == "digital_goods"
