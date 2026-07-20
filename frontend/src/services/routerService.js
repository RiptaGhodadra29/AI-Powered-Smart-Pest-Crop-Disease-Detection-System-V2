import api from "./api";

export const routerPredict = async (
  imageId,
  imageType,
  language
) => {
  const response = await api.post(
    "/router/predict",
    {
      user_id: 1,
      image_id: imageId,
      image_type: imageType,
      language: language,
    }
  );

  return response.data;
};