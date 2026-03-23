package org.ia.rxthorax.data.catalog;

public class DatasetDescriptor {

    private final String datasetName;
    private final String labelFormat;

    public DatasetDescriptor(String datasetName, String labelFormat) {
        this.datasetName = datasetName;
        this.labelFormat = labelFormat;
    }

    public String getDatasetName() {
        return datasetName;
    }

    public String getLabelFormat() {
        return labelFormat;
    }
}
