import { Link } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";
import { useLanguage } from "../../context/LanguageContext";

const Navbar = () => {
  const { logout, isAuthenticated } = useAuth();

  const { language, setLanguage } = useLanguage();

  return (
    <nav className="bg-green-700 text-white px-6 py-4 flex justify-between items-center">
      <h1 className="font-bold text-xl">
        Crop Disease AI
      </h1>

      <div className="flex items-center gap-4">

        <Link to="/">Home</Link>

        {isAuthenticated && (
          <>
            <Link to="/upload">Upload</Link>

            <Link to="/history">History</Link>

            <Link to="/dashboard">Dashboard</Link>

            <button
              onClick={logout}
              className="bg-red-500 px-3 py-1 rounded"
            >
              Logout
            </button>
          </>
        )}

        <select
          value={language}
          onChange={(e) =>
            setLanguage(e.target.value)
          }
          className="text-black px-2 py-1 rounded"
        >
          <option value="en">
            English
          </option>

          <option value="hi">
            हिन्दी
          </option>

          <option value="gu">
            ગુજરાતી
          </option>
        </select>

      </div>
    </nav>
  );
};

export default Navbar;