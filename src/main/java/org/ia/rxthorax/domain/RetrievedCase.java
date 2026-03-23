package org.ia.rxthorax.domain;

public class RetrievedCase {

    private final String studyId;
    private final double similarityScore;

    public RetrievedCase(String studyId, double similarityScore) {
        this.studyId = studyId;
        this.similarityScore = similarityScore;
    }

    public String getStudyId() {
        return studyId;
    }

    public double getSimilarityScore() {
        return similarityScore;
    }
}
