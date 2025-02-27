import React, { useState } from "react";
import ErrorMessage from "../components/ErrorMessage";
import { generateGraph, uploadFile } from "../services/api";
import "../styles/UploadPage.css";

function UploadPage() {
    const [file, setFile] = useState(null);
    const [graph, setGraph] = useState(null);
    const [errorMessage, setErrorMessage] = useState(""); 
    const [config, setConfig] = useState({
        graph_type: "barras",
        x_column: "",
        y_column: "",
        title: "Gráfico Generado",
        x_label: "",
        y_label: "",
        colors: [],
        show_legend: true,
        show_values: false,
        invert_colors: false,
        font_size: 12,
    });

    const handleFileChange = (event) => {
        const selectedFile = event.target.files[0];
    
        if (!selectedFile) {
            setErrorMessage("⚠️ No seleccionaste ningún archivo.");
            return;
        }
    
        console.log("📂 Archivo seleccionado:", selectedFile.name); // 🔹 Depuración
    
        setFile(selectedFile);
    };
    
    const handleUpload = async () => {
        if (!file) {
            setErrorMessage("⚠️ Selecciona un archivo antes de continuar.");
            return;
        }
    
        console.log("📤 Subiendo archivo:", file.name); // 🔹 Depuración
    
        const response = await uploadFile(file);
        alert(response.message);
    };
    
    const handleGenerateGraph = async () => {
        setErrorMessage("");
        setGraph(null); // Limpiar gráfico previo antes de generar uno nuevo
    
        if (!config.x_column || !config.y_column) {
            setErrorMessage("⚠️ Debes seleccionar las columnas X e Y.");
            return;
        }
    
        try {
            const response = await generateGraph(config);
            console.log("📡 Respuesta completa del backend:", response);
    
            if (response && response.graph) {
                console.log("✅ Imagen en base64 procesada:", response.graph.slice(0, 50), "...");
                setGraph(`data:image/png;base64,${response.graph}`);
            } else {
                console.error("❌ Error: La imagen en base64 es inválida.");
                setErrorMessage("⚠️ No se pudo generar la imagen del gráfico.");
            }
        } catch (error) {
            console.error("❌ Error en la solicitud:", error);
            if (error.response && error.response.data.detail) {
                setErrorMessage(error.response.data.detail);
            } else {
                setErrorMessage("⚠️ Ocurrió un error al generar el gráfico.");
            }
        }
    };
    

    return (
        <div className="upload-page">
            <h2>📊 Generador de Gráficos</h2>
            <input type="file" accept=".xlsx" onChange={handleFileChange} />
            <button onClick={handleUpload}>📤 Cargar Archivo</button>

            <h3>⚙️ Configura tu gráfico</h3>
            
            <label>📌 Tipo de Gráfico:</label>
            <select
                value={config.graph_type}
                onChange={(e) => setConfig({ ...config, graph_type: e.target.value })}
            >
                <option value="barras">📊 Barras</option>
                <option value="líneas">📈 Líneas</option>
                <option value="pastel">🥧 Pastel</option>
                <option value="dispersión">🔹 Dispersión</option>
            </select>

            <input
                type="text"
                placeholder="Columna para el eje X"
                value={config.x_column}
                onChange={(e) => setConfig({ ...config, x_column: e.target.value })}
            />
            <input
                type="text"
                placeholder="Columna para el eje Y"
                value={config.y_column}
                onChange={(e) => setConfig({ ...config, y_column: e.target.value })}
            />

            <button onClick={handleGenerateGraph}>📈 Generar Gráfico</button>

            <ErrorMessage message={errorMessage} />

            {graph && (
                    <div className="graph-container">
                        <h3>📊 Gráfico Generado</h3>
                        <img 
                            src={graph} 
                            alt="Gráfico generado"
                            onError={(e) => {
                                console.error("❌ Error al cargar la imagen en React", e);
                                setErrorMessage("⚠️ Error al cargar la imagen.");
                                setGraph(null);
                            }}
                            style={{ maxWidth: "100%", borderRadius: "10px", boxShadow: "0px 4px 10px rgba(0, 0, 0, 0.2)" }}
                        />
                    </div>
            )}

        </div>
    );
}

export default UploadPage;
