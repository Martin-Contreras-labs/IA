from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class NormalizedRadiograph:
    study_id: str
    target_width: int
    target_height: int
    normalized: bool


class RadiographNormalizer:
    def apply(self, study_id: str, target_width: int, target_height: int, normalize: bool) -> NormalizedRadiograph:
        return NormalizedRadiograph(
            study_id=study_id,
            target_width=target_width,
            target_height=target_height,
            normalized=normalize,
        )


class RadiographResizer:
    def describe(self, width: int, height: int) -> str:
        return f"resize({width}x{height})"
