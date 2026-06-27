import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { toast } from "react-toastify";

import { uploadImage } from "../../services/imageService";
import { routerPredict } from "../../services/routerService";

const Upload = () => {
  const navigate = useNavigate();

  const [selectedFile, setSelectedFile] =
    useState(null);

  const [preview, setPreview] =
    useState(null);

  const [uploadResult, setUploadResult] =
    useState(null);

  const [loading, setLoading] =
    useState(false);

  const [imageType, setImageType] =
    useState("disease");

  const handleFileChange = (event) => {
    const file = event.target.files[0];

    if (!file) return;

    setSelectedFile(file);

    setPreview(
      URL.createObjectURL(file)
    );
  };

  const handleUpload = async () => {
    if (!selectedFile) {
      toast.error(
        "Please select an image"
      );
      return;
    }

    try {
      setLoading(true);

      // Upload Image
      const uploadResponse =
        await uploadImage(selectedFile);

      setUploadResult(uploadResponse);

      // AI Router Prediction
      const result =
        await routerPredict(
          uploadResponse.image_id,
          imageType
        );

      toast.success(
        "Prediction completed successfully!"
      );

      navigate(
  "/prediction-result",
  {
    state: {
      ...result,
      imagePreview: preview,
    },
  }
);

    } catch (error) {

      console.error(error);

      toast.error(
        "Prediction failed!"
      );

    } finally {

      setLoading(false);

    }
  };

  return (
    <div className="min-h-screen p-10">

      <h1 className="text-3xl font-bold mb-6">
        Upload Crop Image
      </h1>

      <input
        type="file"
        accept="image/*"
        onChange={handleFileChange}
      />

      {preview && (
        <div className="mt-6">
          <img
            src={preview}
            alt="preview"
            className="w-80 rounded-lg border"
          />
        </div>
      )}

      <div className="mt-6">

        <h3 className="font-semibold mb-2">
          Select Image Type
        </h3>

        <label className="mr-4">

          <input
            type="radio"
            value="disease"
            checked={
              imageType === "disease"
            }
            onChange={(e) =>
              setImageType(
                e.target.value
              )
            }
          />

          <span className="ml-2">
            Disease
          </span>

        </label>

        <label>

          <input
            type="radio"
            value="pest"
            checked={
              imageType === "pest"
            }
            onChange={(e) =>
              setImageType(
                e.target.value
              )
            }
          />

          <span className="ml-2">
            Pest
          </span>

        </label>

      </div>

      <button
        onClick={handleUpload}
        disabled={loading}
        className="bg-green-600 text-white px-6 py-2 rounded mt-6"
      >
        {loading
          ? "Processing..."
          : "Upload & Predict"}
      </button>

      {uploadResult && (
        <div className="mt-6 border p-4 rounded">

          <h2 className="font-bold mb-2">
            Uploaded Image
          </h2>

          <p>
            Image ID:
            {" "}
            {uploadResult.image_id}
          </p>

          <p>
            Image Name:
            {" "}
            {uploadResult.image_name}
          </p>

        </div>
      )}

    </div>
  );
};

export default Upload;