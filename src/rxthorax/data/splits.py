from __future__ import annotations

from enum import Enum


class StudySplit(str, Enum):
    TRAIN = "train"
    VALIDATION = "validation"
    TEST = "test"


class SplitStrategy:
    """Split determinístico simple para trazar train/val/test en H1."""

    def assign(self, study_id: str) -> StudySplit:
        bucket = abs(hash(study_id)) % 10
        if bucket == 0:
            return StudySplit.TEST
        if bucket == 1:
            return StudySplit.VALIDATION
        return StudySplit.TRAIN
