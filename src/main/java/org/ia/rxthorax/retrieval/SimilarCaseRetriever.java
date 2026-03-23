package org.ia.rxthorax.retrieval;

import java.util.List;
import org.ia.rxthorax.domain.RetrievedCase;

public class SimilarCaseRetriever {

    public List<RetrievedCase> retrieve(String studyId, int topK) {
        return List.of(new RetrievedCase(studyId, 1.0));
    }
}
