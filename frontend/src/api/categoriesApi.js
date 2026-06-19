import axios from "axios";

const API = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
});

export const getCategories = () => {
  return API.get("tools/categories/");
}
