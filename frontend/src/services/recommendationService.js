import api from "./api";

export const regenerateRecommendation = async (
  diseaseName,
  language
) => {

  const response = await api.post(
    "/recommendation/regenerate",
    {
      disease_name: diseaseName,
      language: language
    }
  );

  return response.data;
};