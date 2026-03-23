package org.ia.rxthorax.features;

import java.util.List;

public class FeatureVector {

    private final List<Double> values;

    public FeatureVector(List<Double> values) {
        this.values = values;
    }

    public List<Double> getValues() {
        return values;
    }
}
