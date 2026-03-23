package org.ia.rxthorax.xai;

public class AttentionReport {

    private final String studyId;
    private final String heatmapReference;

    public AttentionReport(String studyId, String heatmapReference) {
        this.studyId = studyId;
        this.heatmapReference = heatmapReference;
    }

    public String getStudyId() {
        return studyId;
    }

    public String getHeatmapReference() {
        return heatmapReference;
    }
}
