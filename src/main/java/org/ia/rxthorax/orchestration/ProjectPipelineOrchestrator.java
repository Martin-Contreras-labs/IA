package org.ia.rxthorax.orchestration;

import org.ia.rxthorax.baseline.BaselineTrainingPipeline;
import org.ia.rxthorax.cnn.CnnTrainingPipeline;

public class ProjectPipelineOrchestrator {

    private final BaselineTrainingPipeline baselineTrainingPipeline;
    private final CnnTrainingPipeline cnnTrainingPipeline;

    public ProjectPipelineOrchestrator() {
        this.baselineTrainingPipeline = new BaselineTrainingPipeline();
        this.cnnTrainingPipeline = new CnnTrainingPipeline();
    }

    public String describeArchitecture() {
        return String.join(System.lineSeparator(),
                "Arquitectura inicial del proyecto RxThorax:",
                "- " + baselineTrainingPipeline.describeObjective(),
                "- " + cnnTrainingPipeline.describeObjective(),
                "- H3/OE3: explainability via heatmaps",
                "- H4/OE4: retrieval and expert validation");
    }
}
