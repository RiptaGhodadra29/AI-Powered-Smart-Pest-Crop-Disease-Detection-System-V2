import { Routes, Route } from "react-router-dom";
import Login from "../pages/Login/Login";
import Register from "../pages/Register/Register";
import Dashboard from "../pages/Dashboard/Dashboard";
import Home from "../pages/Home/Home";
import Upload from "../pages/Upload/Upload";
import PredictionResult from "../pages/PredictionResult/PredictionResult";
import Recommendation from "../pages/Recommendation/Recommendation";
import ProtectedRoute from "./ProtectedRoute";
import History from "../pages/History/History";

const AppRoutes = () => {
  return (
    <Routes>
      <Route path="/" element={<Home />} />

      <Route path="/login" element={<Login />} />

      <Route path="/register" element={<Register />} />

      <Route path="/upload" element={ <ProtectedRoute> <Upload /> </ProtectedRoute> } />

      <Route path="/prediction-result" element={ <ProtectedRoute> <PredictionResult /> </ProtectedRoute> } />
     
      <Route path="/history" element={ <ProtectedRoute> <History /> </ProtectedRoute> } />

      <Route path="/recommendation" element={<Recommendation />} />

      

      <Route
        path="/dashboard"
        element={
          <ProtectedRoute>
            <Dashboard />
          </ProtectedRoute>
        }
      />
    </Routes>
  );
};

export default AppRoutes;