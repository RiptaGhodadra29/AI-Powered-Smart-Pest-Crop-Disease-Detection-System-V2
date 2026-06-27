import { useLocation } from "react-router-dom";

const PredictionResult = () => {
  const location = useLocation();

  const pageData = location.state;

  if (!pageData) {
    return (
      <div className="p-10">
        No prediction result available.
      </div>
    );
  }

  const imageType =
    pageData.prediction_type;

  const imagePreview =
    pageData.imagePreview;

  const recommendation =
    pageData.recommendation;

  return (
    <div className="min-h-screen p-10 bg-gray-100">
      <h1 className="text-3xl font-bold mb-6">
        Prediction Result
      </h1>

      <div className="bg-white p-6 rounded shadow">

        {imagePreview && (
          <img
            src={imagePreview}
            alt="uploaded"
            className="w-80 rounded border mb-4"
          />
        )}

        <p className="mb-6">
          <strong>Image Type:</strong>{" "}
          {imageType}
        </p>

        {/* Prediction Section */}

        <div className="mb-8">

          <h2 className="text-2xl font-bold mb-4">

            {imageType === "pest"
              ? "Pest Detection"
              : "Disease Prediction"}

          </h2>

          <p className="mb-2">
            <strong>
              {imageType === "pest"
                ? "Pest"
                : "Disease"}
              :
            </strong>{" "}
            {pageData.prediction_name}
          </p>

          <p className="mb-2">
            <strong>Confidence:</strong>{" "}
            {pageData.confidence}%
          </p>

          {pageData.confidence_level && (
            <p className="mb-2">
              <strong>
                Confidence Level:
              </strong>{" "}
              {pageData.confidence_level}
            </p>
          )}

          {pageData.model_name && (
            <p className="mb-2">
              <strong>Model:</strong>{" "}
              {pageData.model_name}
            </p>
          )}

        </div>

        {/* Recommendation Section */}

        {recommendation && (

          <div className="mb-8">

            <h2 className="text-2xl font-bold mb-4">
              Recommendation
            </h2>

            <p className="mb-2">
              <strong>
                {imageType === "pest"
                  ? "Pest"
                  : "Disease"}
                :
              </strong>{" "}
              {
                recommendation.pest_name ||
                recommendation.disease_name
              }
            </p>

            <p className="mb-2">
              <strong>Severity:</strong>{" "}
              {
                recommendation.damage_severity ||
                recommendation.severity
              }
            </p>

            <p className="mb-2">
              <strong>Description:</strong>{" "}
              {recommendation.description}
            </p>

            <p className="mb-2">
              <strong>Treatment:</strong>{" "}
              {
                recommendation.treatment ||
                recommendation.organic_control
              }
            </p>

            {recommendation.organic_treatment && (
              <p className="mb-2">
                <strong>
                  Organic Treatment:
                </strong>{" "}
                {
                  recommendation.organic_treatment
                }
              </p>
            )}

            {recommendation.chemical_treatment && (
              <p className="mb-2">
                <strong>
                  Chemical Treatment:
                </strong>{" "}
                {
                  recommendation.chemical_treatment
                }
              </p>
            )}

            {recommendation.preventive_measures && (
              <p className="mb-2">
                <strong>
                  Preventive Measures:
                </strong>{" "}
                {
                  recommendation.preventive_measures
                }
              </p>
            )}

            {recommendation.monitoring_actions && (
              <p className="mb-2">
                <strong>
                  Monitoring Actions:
                </strong>{" "}
                {
                  recommendation.monitoring_actions
                }
              </p>
            )}

          </div>

        )}

      </div>
    </div>
  );
};

export default PredictionResult;