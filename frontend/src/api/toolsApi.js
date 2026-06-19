import axios from "axios";

const API = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
});

export const getTools = (
  search = "",
  sector = "",
  category = "",
  status = "",
) => {
  return API.get("/tools/", {
    params: {
      search,
      sector,
      category,
      status,
    },
  });
};

export const createTool = (toolData) => {
  return API.post("/tools/", toolData);
};

export const updateTool = (id, toolData) => {
  return API.put(`/tools/${id}/`, toolData);
};

export const deleteTool = (id) => {
  return API.delete(`/tools/${id}/`);
};