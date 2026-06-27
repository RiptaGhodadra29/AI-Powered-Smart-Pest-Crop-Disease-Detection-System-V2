# Recommendation Engine Pseudocode

START

Receive Prediction

IF confidence < threshold

    Return:
    Upload clearer image

ELSE

    IF prediction type = disease

        Search Disease Knowledge Base

        Retrieve Record

    ELSE IF prediction type = pest

        Search Pest Knowledge Base

        Retrieve Record

    ENDIF

Generate Recommendation

Return Recommendation

END