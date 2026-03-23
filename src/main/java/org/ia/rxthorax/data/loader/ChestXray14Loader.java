package org.ia.rxthorax.data.loader;

import org.ia.rxthorax.data.catalog.DatasetDescriptor;

public class ChestXray14Loader implements DatasetLoader {

    @Override
    public DatasetDescriptor describe() {
        return new DatasetDescriptor("ChestX-ray14", "multi-label");
    }

    @Override
    public String loadMetadata() {
        return "Pending metadata loader for ChestX-ray14";
    }
}
