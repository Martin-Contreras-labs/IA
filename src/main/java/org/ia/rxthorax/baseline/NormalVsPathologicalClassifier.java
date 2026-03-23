package org.ia.rxthorax.baseline;

import org.ia.rxthorax.domain.PathologyLabel;
import org.ia.rxthorax.domain.PredictionResult;
import org.ia.rxthorax.features.FeatureVector;

public class NormalVsPathologicalClassifier {

    public PredictionResult predict(String studyId, FeatureVector featureVector) {
        return new PredictionResult(studyId, PathologyLabel.NORMAL, 0.50);
    }
}
