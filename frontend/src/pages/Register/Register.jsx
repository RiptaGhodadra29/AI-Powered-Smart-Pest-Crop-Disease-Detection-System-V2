import { useState } from "react";
import { registerUser } from "../../services/authService";
import { useNavigate } from "react-router-dom";
import { toast } from "react-toastify";
const Register = () => {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    username: "",
    email: "",
    password: "",
  });

  const handleSubmit = async (e) => {
  e.preventDefault();

  try {
    await registerUser(formData);

    toast.success(
      "Registration successful!"
    );

    navigate("/login");

  } catch (error) {

    toast.error(
      "Registration failed!"
    );

    console.error(error);
  }
};

  return (
    <div className="min-h-screen flex justify-center items-center">
      <form
        onSubmit={handleSubmit}
        className="w-full max-w-md p-6 border rounded-lg shadow"
      >
        <h1 className="text-2xl font-bold mb-6">
          Register
        </h1>

        <input
          type="text"
          name="username"
          placeholder="Username"
          className="w-full border p-3 mb-4"
          onChange={handleChange}
        />

        <input
          type="email"
          name="email"
          placeholder="Email"
          className="w-full border p-3 mb-4"
          onChange={handleChange}
        />

        <input
          type="password"
          name="password"
          placeholder="Password"
          className="w-full border p-3 mb-4"
          onChange={handleChange}
        />

        <button
          className="w-full bg-green-600 text-white p-3 rounded"
        >
          Register
        </button>
      </form>
    </div>
  );
};

export default Register;