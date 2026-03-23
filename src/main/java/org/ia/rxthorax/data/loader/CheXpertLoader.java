package org.ia.rxthorax.data.loader;

import org.ia.rxthorax.data.catalog.DatasetDescriptor;

public class CheXpertLoader implements DatasetLoader {

    @Override
    public DatasetDescriptor describe() {
        return new DatasetDescriptor("CheXpert", "uncertain multi-label");
    }

    @Override
    public String loadMetadata() {
        return "Pending metadata loader for CheXpert";
    }
}
