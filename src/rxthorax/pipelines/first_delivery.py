from __future__ import annotations

from pathlib import Path

from rxthorax.config.settings import ProjectSettings
from rxthorax.data.datasets import DatasetRepository
from rxthorax.domain.enums import PathologyLabel, StudySplit
from rxthorax.domain.records import ChestStudyRecord, FeatureVector
from rxthorax.domain.results import ExperimentReport, PredictionResult
from rxthorax.evaluation.metrics import MetricsEvaluator
from rxthorax.features.statistics import StatisticalFeatureExtractor
from rxthorax.models.logreg import LogRegBaseline
from rxthorax.preprocessing.transforms import RadiographNormalizer, RadiographResizer


class FirstDeliveryPipeline:
    def __init__(self, settings: ProjectSettings) -> None:
        self.settings = settings
        self.dataset_repository = DatasetRepository()
        self.normalizer = RadiographNormalizer()
        self.resizer = RadiographResizer()
        self.feature_extractor = StatisticalFeatureExtractor()
        self.classifier = LogRegBaseline()
        self.metrics_evaluator = MetricsEvaluator()

    @classmethod
    def from_default_config(cls) -> "FirstDeliveryPipeline":
        config_path = Path(__file__).resolve().parents[3] / "configs" / "first_delivery.json"
        settings = ProjectSettings.from_json(config_path)
        return cls(settings)

    def build_synthetic_records(self) -> list[ChestStudyRecord]:
        ids_and_labels = [
            ("normal-01", PathologyLabel.NORMAL),
            ("normal-02", PathologyLabel.NORMAL),
            ("normal-03", PathologyLabel.NORMAL),
            ("normal-04", PathologyLabel.NORMAL),
            ("normal-05", PathologyLabel.NORMAL),
            ("normal-06", PathologyLabel.NORMAL),
            ("pneumonia-case-01", PathologyLabel.PNEUMONIA),
            ("pneumonia-case-02", PathologyLabel.PNEUMONIA),
            ("normal-val-01", PathologyLabel.NORMAL),
            ("pneumonia-val-01", PathologyLabel.PNEUMONIA),
            ("normal-test-01", PathologyLabel.NORMAL),
            ("pneumonia-test-01", PathologyLabel.PNEUMONIA),
        ]
        records: list[ChestStudyRecord] = []
        for index, (study_id, label) in enumerate(ids_and_labels):
            if index < 8:
                split = StudySplit.TRAIN
            elif index < 10:
                split = StudySplit.VALIDATION
            else:
                split = StudySplit.TEST
            records.append(
                ChestStudyRecord(
                    study_id=study_id,
                    image_path=Path(f"data/{study_id}.png"),
                    label=label,
                    split=split,
                )
            )
        return records

    def _record_to_features(self, record: ChestStudyRecord) -> FeatureVector:
        normalized = self.normalizer.apply(
            study_id=record.study_id,
            target_width=self.settings.images.target_width,
            target_height=self.settings.images.target_height,
            normalize=self.settings.images.normalize,
        )
        return self.feature_extractor.extract(normalized)

    def run_demo(self) -> ExperimentReport:
        if self.settings.baseline.classifier != "logreg":
            raise ValueError("First delivery pipeline currently supports classifier='logreg' only")

        dataset = self.dataset_repository.get(self.settings.active_dataset)
        records = self.build_synthetic_records()

        train_records = [record for record in records if record.split == StudySplit.TRAIN]
        validation_records = [record for record in records if record.split == StudySplit.VALIDATION]

        train_features = [self._record_to_features(record) for record in train_records]
        train_labels = [record.label for record in train_records]
        self.classifier.fit(train_features, train_labels)

        validation_features = [self._record_to_features(record) for record in validation_records]
        validation_predictions = [self.classifier.predict(features) for features in validation_features]
        avg_confidence = sum(prediction.confidence for prediction in validation_predictions) / len(
            validation_predictions
        )

        representative_prediction = validation_predictions[0]
        metrics = self.metrics_evaluator.evaluate(
            PredictionResult(
                study_id=representative_prediction.study_id,
                predicted_label=representative_prediction.predicted_label,
                confidence=avg_confidence,
            )
        )
        resize_step = self.resizer.describe(
            self.settings.images.target_width,
            self.settings.images.target_height,
        )
        summary = (
            f"Entrega {self.settings.delivery} sobre {dataset.name}: "
            f"{self.settings.baseline.mode}, features={self.settings.baseline.feature_family}, "
            f"classifier={self.settings.baseline.classifier}, train={len(train_records)}, "
            f"val={len(validation_records)}, avg_val_confidence={avg_confidence:.3f}, "
            f"preprocessing={resize_step}, metrics={metrics}"
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
