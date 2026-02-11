import json
from pathlib import Path
from typing import Any

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from portal.services.eligibility import evaluate_eligibility, load_rules
from portal.services.mapper import map_order
from portal.types import EligibilityResult, ReturnRegistration

DATA_PATH = Path(__file__).resolve().parent / "data" / "orders_raw.json"


def _load_orders() -> list[dict[str, Any]]:
    payload = json.loads(DATA_PATH.read_text())
    if not isinstance(payload, dict):
        return []
    orders = payload.get("orders")
    if not isinstance(orders, list):
        return []
    return [raw for raw in orders if isinstance(raw, dict)]


def lookup(request: HttpRequest) -> HttpResponse:
    return render(request, "returns/lookup.html", {"error": None})


def submit_lookup(request: HttpRequest) -> HttpResponse:
    order_number = request.POST.get("order_number", "").strip()
    email_or_zip = request.POST.get("email_or_zip", "").strip()
    for raw in _load_orders():
        if raw["order_number"] == order_number and (
            raw["email"] == email_or_zip or raw["zip"] == email_or_zip
        ):
            return redirect("order_details", order_number=order_number)
    return render(
        request, "returns/lookup.html", {"error": "Order not found or mismatch."}
    )


def _build_view_data(
    order_number: str,
) -> dict[str, ReturnRegistration | dict[str, EligibilityResult]]:
    raw = next(o for o in _load_orders() if o["order_number"] == order_number)
    order = map_order(raw)
    rules = load_rules()
    results = evaluate_eligibility(order, rules)
    result_by_sku = {r.sku: r for r in results}
    return {"order": order, "results": result_by_sku}


def order_details(request: HttpRequest, order_number: str) -> HttpResponse:
    context = _build_view_data(order_number)
    return render(request, "returns/order.html", context)


def recompute_eligibility(request: HttpRequest, order_number: str) -> HttpResponse:
    context = _build_view_data(order_number)
    return render(request, "returns/_items.html", context)
