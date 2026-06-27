import { useEffect, useState } from "react";
import { getDashboardData } from "../../services/dashboardService";

const Dashboard = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    let mounted = true;

    (async () => {
      try {
        const result = await getDashboardData(1);
        if (mounted) setData(result);
      } catch (error) {
        console.error(error);
      }
    })();

    return () => {
      mounted = false;
    };
  }, []);

  if (!data) {
    return (
      <div className="p-10">
        Loading Dashboard...
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-100 p-8">

      <h1 className="text-4xl font-bold mb-8">
        Analytics Dashboard
      </h1>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">

        <div className="bg-white shadow-lg rounded-xl p-6">
          <h2 className="text-gray-500">
            Total Predictions
          </h2>

          <p className="text-4xl font-bold mt-2">
            {data.total_predictions}
          </p>
        </div>

        <div className="bg-white shadow-lg rounded-xl p-6">
          <h2 className="text-gray-500">
            Most Detected Disease
          </h2>

          <p className="text-xl font-semibold mt-2">
            {data.most_detected_disease}
          </p>
        </div>

        <div className="bg-white shadow-lg rounded-xl p-6">
          <h2 className="text-gray-500">
            Average Confidence
          </h2>

          <p className="text-4xl font-bold mt-2">
            {data.average_confidence}%
          </p>
        </div>

      </div>
    </div>
  );
};

export default Dashboard;