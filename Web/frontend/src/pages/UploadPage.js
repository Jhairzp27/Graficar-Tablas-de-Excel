import React, { useState } from "react";
import "../styles/UploadPage.css";

function UploadPage() {
    const [file, setFile] = useState(null);

    const handleFileChange = (event) => {
        setFile(event.target.files[0]);
    };

    const handleUpload = () => {
        if (!file) {
            alert("Selecciona un archivo antes de continuar.");
            return;
        }
        console.log("Archivo listo para subir:", file);
    };

    return (
        <div className="upload-page">
            <h2>Sube tu archivo Excel</h2>
            <input type="file" accept=".xlsx" onChange={handleFileChange} />
            <button onClick={handleUpload}>Cargar y Configurar</button>
        </div>
    );
}

export default UploadPage;
