from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from rxthorax.config.settings import ProjectSettings
from rxthorax.data.datasets import DatasetRepository
from rxthorax.data.splits import SplitStrategy
from rxthorax.evaluation.metrics import MetricsEvaluator
from rxthorax.features.statistics import PreparedStudy, StatisticalFeatureExtractor
from rxthorax.models.logreg import LogRegModel


@dataclass(frozen=True)
class H1Report:
    project_name: str
    delivery: str
    dataset_name: str
    summary: str


class H1Pipeline:
    def __init__(self, settings: ProjectSettings) -> None:
        self.settings = settings
        self.dataset_repository = DatasetRepository()
        self.split_strategy = SplitStrategy()
        self.feature_extractor = StatisticalFeatureExtractor()
        self.classifier = LogRegModel()
        self.metrics_evaluator = MetricsEvaluator()

    @classmethod
    def from_default_config(cls) -> "H1Pipeline":
        config_path = Path(__file__).resolve().parents[3] / "configs" / "first_delivery.json"
        settings = ProjectSettings.from_json(config_path)
        return cls(settings)

    def run_demo(self) -> H1Report:
        dataset = self.dataset_repository.get(self.settings.active_dataset)
        study_id = "demo-study-001"
        split = self.split_strategy.assign(study_id)
        prepared_study = PreparedStudy(
            study_id=study_id,
            target_width=self.settings.images.target_width,
            target_height=self.settings.images.target_height,
        )
        features = self.feature_extractor.extract(prepared_study)
        prediction = self.classifier.predict(features)
        metrics = self.metrics_evaluator.evaluate(prediction)
        summary = (
            f"Entrega {self.settings.delivery} sobre {dataset.name}: "
            f"split={split.value}, features={self.settings.baseline.feature_family}, "
            f"classifier=logreg, metrics={metrics}"
        )
        return H1Report(
            project_name=self.settings.name,
            delivery=self.settings.delivery,
            dataset_name=dataset.name,
            summary=summary,
        )

    def describe(self) -> str:
        report = self.run_demo()
        return "\n".join(
            [
                "RxThorax - Primera entrega (H1)",
                f"Proyecto: {report.project_name}",
                f"Dataset activo: {report.dataset_name}",
                f"Resumen: {report.summary}",
            ]
        )
