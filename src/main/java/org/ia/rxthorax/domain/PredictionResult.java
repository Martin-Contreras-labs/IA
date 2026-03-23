package org.ia.rxthorax.domain;

public class PredictionResult {

    private final String studyId;
    private final PathologyLabel predictedLabel;
    private final double confidence;

    public PredictionResult(String studyId, PathologyLabel predictedLabel, double confidence) {
        this.studyId = studyId;
        this.predictedLabel = predictedLabel;
        this.confidence = confidence;
    }

    public String getStudyId() {
        return studyId;
    }

    public PathologyLabel getPredictedLabel() {
        return predictedLabel;
    }

    public double getConfidence() {
        return confidence;
    }
}
