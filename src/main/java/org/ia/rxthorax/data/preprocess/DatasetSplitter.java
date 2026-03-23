package org.ia.rxthorax.data.preprocess;

import org.ia.rxthorax.domain.StudySplit;

public class DatasetSplitter {

    public StudySplit assignSplit(String studyId) {
        return studyId.hashCode() % 10 == 0 ? StudySplit.TEST : StudySplit.TRAIN;
    }
}
