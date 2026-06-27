import { Link } from "react-router-dom";

const Home = () => {
  return (
    <div className="min-h-screen flex flex-col justify-center items-center text-center p-10">

      <h1 className="text-5xl font-bold mb-6">
        AI-Powered Smart Pest & Crop Disease Detection
      </h1>

      <p className="text-lg mb-8">
        Upload crop leaf images and get AI-powered disease detection with recommendations.
      </p>

      <div className="mb-10">
        <h2 className="text-2xl font-bold mb-4">
          How It Works
        </h2>

        <p>1. Upload Leaf Image</p>
        <p>2. AI Detects Disease</p>
        <p>3. Get Treatment Recommendation</p>
      </div>

      <Link
        to="/upload"
        className="bg-green-600 text-white px-8 py-3 rounded-lg"
      >
        Get Started
      </Link>

    </div>
  );
};

export default Home;