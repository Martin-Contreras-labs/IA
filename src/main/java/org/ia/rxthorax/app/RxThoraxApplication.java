package org.ia.rxthorax.app;

import org.ia.rxthorax.orchestration.ProjectPipelineOrchestrator;

public class RxThoraxApplication {

    public static void main(String[] args) {
        ProjectPipelineOrchestrator orchestrator = new ProjectPipelineOrchestrator();
        System.out.println(orchestrator.describeArchitecture());
    }
}
