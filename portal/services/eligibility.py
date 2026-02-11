from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from portal.types import EligibilityResult, ReturnRegistration


@dataclass(frozen=True)
class Rule:
    rule_id: str
    priority: int
    result: dict[str, Any]
    when: dict[str, Any]


def load_rules() -> list[Rule]:
    # Intentionally left empty: candidates define their own rules structure.
    return []


def evaluate_eligibility(
    order: ReturnRegistration, rules: list[Rule]
) -> list[EligibilityResult]:
    return [
        EligibilityResult(
            sku=item.sku,
            returnable=None,
            flag="unknown",
            reason="Eligibility not evaluated.",
            matched_rule_id=None,
        )
        for item in order.items
    ]
