import axios from "axios";

const API_URL = "http://127.0.0.1:8000"; // Asegúrate de que coincida con el backend

// 🔹 Subir un archivo Excel al backend
export const uploadFile = async (file) => {
    const formData = new FormData();
    formData.append("file", file);

    const response = await axios.post(`${API_URL}/upload/`, formData, {
        headers: { "Content-Type": "multipart/form-data" },
    });

    return response.data;
};

// 🔹 Generar un gráfico con configuraciones personalizadas
export const generateGraph = async (config) => {
    const response = await axios.post(`${API_URL}/graph/`, config);
    return response.data.graph; // Devuelve la imagen en base64
};

// 🔹 Descargar un gráfico en PNG, JPG o PDF
export const downloadGraph = async (filename) => {
    const response = await axios.get(`${API_URL}/export/${filename}`, {
        responseType: "blob",
    });

    const url = window.URL.createObjectURL(new Blob([response.data]));
    const link = document.createElement("a");
    link.href = url;
    link.setAttribute("download", filename);
    document.body.appendChild(link);
    link.click();
};

// 🔹 Descargar un PDF personalizado
export const downloadCustomPDF = async (title, footer_text, orientation) => {
    const response = await axios.get(`${API_URL}/export/pdf/`, {
        params: { title, footer_text, orientation },
        responseType: "blob",
    });

    const url = window.URL.createObjectURL(new Blob([response.data]));
    const link = document.createElement("a");
    link.href = url;
    link.setAttribute("download", "grafico_personalizado.pdf");
    document.body.appendChild(link);
    link.click();
};
