from __future__ import annotations

from rxthorax.domain.enums import StudySplit


class SplitStrategy:
    """Split determinístico simple para dejar trazada la responsabilidad del módulo."""

    def assign(self, study_id: str) -> StudySplit:
        bucket = abs(hash(study_id)) % 10
        if bucket == 0:
            return StudySplit.TEST
        if bucket == 1:
            return StudySplit.VALIDATION
        return StudySplit.TRAIN
