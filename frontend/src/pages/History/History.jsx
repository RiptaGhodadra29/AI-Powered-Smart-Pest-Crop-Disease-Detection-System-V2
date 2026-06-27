import { useEffect, useState } from "react";
import { getHistory } from "../../services/historyService";

const History = () => {
  const [history, setHistory] = useState([]);

  useEffect(() => {
    let mounted = true;

    (async () => {
      try {
        const data = await getHistory(1);

        if (mounted) {
          setHistory(data.history);
        }
      } catch (error) {
        console.error(error);
      }
    })();

    return () => {
      mounted = false;
    };
  }, []);

  return (
    <div className="min-h-screen bg-gray-100 p-6 md:p-10">

      <h1 className="text-3xl font-bold mb-6">
        Prediction History
      </h1>

      <div className="bg-white rounded-xl shadow-lg overflow-x-auto">

        <table className="w-full">

          <thead className="bg-green-600 text-white">
            <tr>
              <th className="p-4 text-left">
                ID
              </th>

              <th className="p-4 text-left">
                Type
              </th>

              <th className="p-4 text-left">
                Prediction
              </th>

              <th className="p-4 text-left">
                Confidence
              </th>

              <th className="p-4 text-left">
                Model
              </th>

              <th className="p-4 text-left">
                Date
              </th>
            </tr>
          </thead>

          <tbody>
            {history.length > 0 ? (
              history.map((item) => (
                <tr
                  key={item.prediction_id}
                  className="border-b hover:bg-gray-50"
                >
                  <td className="p-4">
                    {item.prediction_id}
                  </td>

                  <td className="p-4 capitalize">
                    {item.prediction_type}
                  </td>

                  <td className="p-4">
                    {item.class_name}
                  </td>

                  <td className="p-4">
                    {item.confidence}%
                  </td>

                  <td className="p-4">
                    {item.model_name}
                  </td>

                  <td className="p-4">
                    {item.created_at
                      ? new Date(
                          item.created_at
                        ).toLocaleString()
                      : "-"}
                  </td>
                </tr>
              ))
            ) : (
              <tr>
                <td
                  colSpan="6"
                  className="p-6 text-center text-gray-500"
                >
                  No prediction history found.
                </td>
              </tr>
            )}
          </tbody>

        </table>

      </div>
    </div>
  );
};

export default History;