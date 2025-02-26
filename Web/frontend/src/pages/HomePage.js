import React from "react";
import { useNavigate } from "react-router-dom";
import "../styles/HomePage.css"; // Importar estilos

function HomePage() {
    const navigate = useNavigate();

    return (
        <div className="homepage">
            <header className="hero">
                <h1>Bienvenido al Graficador de Excel</h1>
                <p>Sube tu archivo Excel y genera gráficos personalizables fácilmente.</p>
                <button className="cta-button" onClick={() => navigate("/upload")}>
                    Comenzar
                </button>
            </header>

            <section className="features">
                <h2>¿Cómo funciona?</h2>
                <div className="steps">
                    <div className="step">
                        <h3>1. Sube tu archivo Excel</h3>
                        <p>Selecciona un archivo con datos organizados en columnas.</p>
                    </div>
                    <div className="step">
                        <h3>2. Configura tu gráfico</h3>
                        <p>Elige el tipo de gráfico y personaliza colores y etiquetas.</p>
                    </div>
                    <div className="step">
                        <h3>3. Descarga o comparte</h3>
                        <p>Genera el gráfico y expórtalo en formato PNG o PDF.</p>
                    </div>
                </div>
            </section>
        </div>
    );
}

export default HomePage;
