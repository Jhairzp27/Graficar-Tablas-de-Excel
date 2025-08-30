// src/pages/HomePage.js

import { Link } from 'react-router-dom';
// Importamos los iconos que vamos a usar
import { Download, Settings, UploadCloud } from 'lucide-react';
import '../styles/HomePage.css';

const HomePage = () => {
  return (
    <div className="homepage">
      <section className="hero-section">
        <h1>Bienvenido al Graficador de Excel</h1>
        <p>
          Transforma tus datos en visualizaciones impactantes. Sube tu archivo
          Excel y genera gráficos personalizados fácilmente.
        </p>
        <Link to="/upload" className="cta-button">
          Comenzar Ahora
        </Link>
      </section>

      <section className="steps-section">
        <h2>¿Cómo funciona?</h2>
        <div className="steps-grid">
          {/* Tarjeta 1 */}
          <div className="step-card">
            <div className="step-icon">
              <UploadCloud size={48} strokeWidth={1.5} />
            </div>
            <h3>1. Sube tu archivo Excel</h3>
            <p>Selecciona un archivo con datos organizados en columnas.</p>
          </div>

          {/* Tarjeta 2 */}
          <div className="step-card">
            <div className="step-icon">
              <Settings size={48} strokeWidth={1.5} />
            </div>
            <h3>2. Configura tu gráfico</h3>
            <p>Elige el tipo de gráfico y personaliza colores y etiquetas.</p>
          </div>

          {/* Tarjeta 3 */}
          <div className="step-card">
            <div className="step-icon">
              <Download size={48} strokeWidth={1.5} />
            </div>
            <h3>3. Descarga o comparte</h3>
            <p>Genera el gráfico y expórtalo en formato PNG o PDF.</p>
          </div>
        </div>
      </section>
    </div>
  );
};

export default HomePage;
