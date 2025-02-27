import React, { useState } from "react";
import { downloadCustomPDF, downloadGraph } from "../services/api";

function DownloadOptions() {
    const [format, setFormat] = useState("png");
    const [title, setTitle] = useState("Reporte de Gráfico");
    const [footer, setFooter] = useState("© Graficador Excel");
    const [orientation, setOrientation] = useState("P");
    const [dpi, setDpi] = useState(300);
    const [bgColor, setBgColor] = useState("#ffffff");

    const handleDownload = async () => {
        if (format === "pdf") {
            await downloadCustomPDF(title, footer, orientation);
        } else {
            await downloadGraph(`grafico.${format}`);
        }
    };

    return (
        <div className="download-options">
            <h3>📥 Personaliza tu Descarga</h3>
            <label>Formato:</label>
            <select value={format} onChange={(e) => setFormat(e.target.value)}>
                <option value="png">PNG</option>
                <option value="jpg">JPG</option>
                <option value="pdf">PDF</option>
            </select>

            {format !== "pdf" && (
                <>
                    <label>Calidad (DPI):</label>
                    <input type="number" value={dpi} onChange={(e) => setDpi(e.target.value)} />

                    <label>Color de Fondo:</label>
                    <input type="color" value={bgColor} onChange={(e) => setBgColor(e.target.value)} />
                </>
            )}

            {format === "pdf" && (
                <>
                    <label>Título del PDF:</label>
                    <input type="text" value={title} onChange={(e) => setTitle(e.target.value)} />

                    <label>Pie de Página:</label>
                    <input type="text" value={footer} onChange={(e) => setFooter(e.target.value)} />

                    <label>Orientación:</label>
                    <select value={orientation} onChange={(e) => setOrientation(e.target.value)}>
                        <option value="P">Vertical</option>
                        <option value="L">Horizontal</option>
                    </select>
                </>
            )}

            <button onClick={handleDownload}>Descargar</button>
        </div>
    );
}

export default DownloadOptions;
