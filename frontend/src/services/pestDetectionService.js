import api from "./api";

export const detectPests = async (imageId) => {
  const response = await api.post(
    `/detect/pest/${imageId}`
  );

  return response.data;
};