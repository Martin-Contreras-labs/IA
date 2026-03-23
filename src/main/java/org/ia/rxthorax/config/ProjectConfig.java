package org.ia.rxthorax.config;

import java.nio.file.Path;

public class ProjectConfig {

    private final Path datasetRoot;
    private final int targetImageWidth;
    private final int targetImageHeight;

    public ProjectConfig(Path datasetRoot, int targetImageWidth, int targetImageHeight) {
        this.datasetRoot = datasetRoot;
        this.targetImageWidth = targetImageWidth;
        this.targetImageHeight = targetImageHeight;
    }

    public Path getDatasetRoot() {
        return datasetRoot;
    }

    public int getTargetImageWidth() {
        return targetImageWidth;
    }

    public int getTargetImageHeight() {
        return targetImageHeight;
    }
}
