package org.ia.rxthorax.features;

import java.util.List;

public class StatisticalFeatureExtractor {

    public FeatureVector extract(String normalizedImageReference) {
        return new FeatureVector(List.of(0.0, 1.0, 2.0));
    }
}
