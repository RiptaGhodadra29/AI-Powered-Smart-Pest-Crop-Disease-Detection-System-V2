import { useLocation } from "react-router-dom";

const Recommendation = () => {
  const location = useLocation();

  const recommendation =
    location.state ||
    JSON.parse(
      sessionStorage.getItem("recommendation")
    );

  if (!recommendation) {
    return (
      <div className="p-10 text-center">
        No recommendation available.
      </div>
    );
  }

  const severityColor =
    recommendation.severity === "High"
      ? "bg-red-100 text-red-700"
      : recommendation.severity === "Medium"
      ? "bg-yellow-100 text-yellow-700"
      : "bg-green-100 text-green-700";

  return (
    <div className="min-h-screen bg-gray-100 p-6 md:p-10">

      <h1 className="text-3xl font-bold mb-8 text-center">
        Disease Recommendation
      </h1>

      <div className="max-w-5xl mx-auto space-y-4">

        {/* Disease Name */}
        <div className="bg-white shadow rounded-xl p-6">
          <h2 className="font-bold text-lg mb-2">
            Disease Name
          </h2>

          <p className="text-xl text-green-700 font-semibold">
            {recommendation.disease_name}
          </p>
        </div>

        {/* Severity */}
        <div className="bg-white shadow rounded-xl p-6">
          <h2 className="font-bold text-lg mb-2">
            Severity
          </h2>

          <span
            className={`px-4 py-2 rounded-full font-semibold ${severityColor}`}
          >
            {recommendation.severity}
          </span>
        </div>

        {/* Description */}
        <div className="bg-white shadow rounded-xl p-6">
          <h2 className="font-bold text-lg mb-2">
            Description
          </h2>

          <p>
            {recommendation.description}
          </p>
        </div>

        {/* Treatment */}
        <div className="bg-white shadow rounded-xl p-6">
          <h2 className="font-bold text-lg mb-2">
            Treatment
          </h2>

          <p>
            {recommendation.treatment}
          </p>
        </div>

        {/* Organic Treatment */}
        <div className="bg-white shadow rounded-xl p-6">
          <h2 className="font-bold text-lg mb-2">
            Organic Treatment
          </h2>

          <p>
            {recommendation.organic_treatment}
          </p>
        </div>

        {/* Chemical Treatment */}
        <div className="bg-white shadow rounded-xl p-6">
          <h2 className="font-bold text-lg mb-2">
            Chemical Treatment
          </h2>

          <p>
            {recommendation.chemical_treatment}
          </p>
        </div>

        {/* Preventive Measures */}
        <div className="bg-white shadow rounded-xl p-6">
          <h2 className="font-bold text-lg mb-2">
            Preventive Measures
          </h2>

          <p>
            {recommendation.preventive_measures}
          </p>
        </div>

        {/* Monitoring Actions */}
        <div className="bg-white shadow rounded-xl p-6">
          <h2 className="font-bold text-lg mb-2">
            Monitoring Actions
          </h2>

          <p>
            {recommendation.monitoring_actions}
          </p>
        </div>

      </div>
    </div>
  );
};

export default Recommendation;