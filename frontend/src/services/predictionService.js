import api from "./api";

export const predictDisease = async (imageId) => {
  const response = await api.post(
    "/predict/disease",
    {
      user_id: 1,
      image_id: imageId,
    }
  );

  return response.data;
};