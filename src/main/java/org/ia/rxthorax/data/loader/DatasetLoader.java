package org.ia.rxthorax.data.loader;

import org.ia.rxthorax.data.catalog.DatasetDescriptor;

public interface DatasetLoader {

    DatasetDescriptor describe();

    String loadMetadata();
}
