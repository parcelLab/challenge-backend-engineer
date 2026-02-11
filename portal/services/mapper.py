from datetime import datetime
from typing import Any

from portal.types import LineItem, ReturnRegistration


def _parse_dt(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def map_order(raw: dict[str, Any]) -> ReturnRegistration:
    items = []
    for raw_item in raw.get("items", []):
        items.append(
            LineItem(
                sku=str(raw_item["sku"]),
                name=str(raw_item["name"]),
                category=None,  # TODO: map category
                quantity=int(raw_item["quantity"]),
                quantity_returned=int(raw_item.get("quantity_returned", 0)),
                price=float(raw_item["price"]),
                is_digital=False,  # TODO: map digital flag
                is_final_sale=False,  # TODO: map final sale flag
            )
        )
    return ReturnRegistration(
        order_number=str(raw["order_number"]),
        email=str(raw["email"]),
        zip=str(raw["zip"]),
        purchased_at=_parse_dt(raw["purchased_at"]),
        delivered_at=_parse_dt(raw["delivered_at"]),
        return_window_days=int(raw["return_window_days"]),
        items=items,
    )
