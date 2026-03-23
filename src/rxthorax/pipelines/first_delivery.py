from __future__ import annotations

from pathlib import Path

from rxthorax.config.settings import ProjectSettings
from rxthorax.data.datasets import DatasetRepository
from rxthorax.data.splits import SplitStrategy
from rxthorax.domain.enums import PathologyLabel
from rxthorax.domain.records import ChestStudyRecord
from rxthorax.domain.results import ExperimentReport
from rxthorax.evaluation.metrics import MetricsEvaluator
from rxthorax.features.statistics import StatisticalFeatureExtractor
from rxthorax.models.baseline import BaselineClassifier, BaselineModelSpec
from rxthorax.preprocessing.transforms import RadiographNormalizer, RadiographResizer


class FirstDeliveryPipeline:
    def __init__(self, settings: ProjectSettings) -> None:
        self.settings = settings
        self.dataset_repository = DatasetRepository()
        self.split_strategy = SplitStrategy()
        self.normalizer = RadiographNormalizer()
        self.resizer = RadiographResizer()
        self.feature_extractor = StatisticalFeatureExtractor()
        self.classifier = BaselineClassifier(
            BaselineModelSpec(
                mode=settings.baseline.mode,
                classifier=settings.baseline.classifier,
            )
        )
        self.metrics_evaluator = MetricsEvaluator()

    @classmethod
    def from_default_config(cls) -> "FirstDeliveryPipeline":
        config_path = Path(__file__).resolve().parents[3] / "configs" / "first_delivery.json"
        settings = ProjectSettings.from_json(config_path)
        return cls(settings)

    def build_demo_record(self) -> ChestStudyRecord:
        study_id = "demo-study-001"
        split = self.split_strategy.assign(study_id)
        return ChestStudyRecord(
            study_id=study_id,
            image_path=Path("data/demo-study-001.png"),
            label=PathologyLabel.NORMAL,
            split=split,
        )

    def run_demo(self) -> ExperimentReport:
        dataset = self.dataset_repository.get(self.settings.active_dataset)
        record = self.build_demo_record()
        normalized = self.normalizer.apply(
            study_id=record.study_id,
            target_width=self.settings.images.target_width,
            target_height=self.settings.images.target_height,
            normalize=self.settings.images.normalize,
        )
        features = self.feature_extractor.extract(normalized)
        prediction = self.classifier.predict(features)
        metrics = self.metrics_evaluator.evaluate(prediction)
        resize_step = self.resizer.describe(
            self.settings.images.target_width,
            self.settings.images.target_height,
        )
        summary = (
            f"Entrega {self.settings.delivery} sobre {dataset.name}: "
            f"{self.settings.baseline.mode}, features={self.settings.baseline.feature_family}, "
            f"classifier={self.settings.baseline.classifier}, preprocessing={resize_step}, "
            f"metrics={metrics}"
        )
        return ExperimentReport(
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
