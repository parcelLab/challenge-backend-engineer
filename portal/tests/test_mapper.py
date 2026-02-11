from portal.services.mapper import map_order


def test_mapper_maps_item_flags() -> None:
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
    item = order.items[0]
    assert item.is_digital is True
    assert item.is_final_sale is False
    assert item.category == "digital"
