import api from "./api";

export const routerPredict = async (
  imageId,
  imageType
) => {
  const response = await api.post(
    "/router/predict",
    {
      user_id: 1,
      image_id: imageId,
      image_type: imageType,
    }
  );

  return response.data;
};