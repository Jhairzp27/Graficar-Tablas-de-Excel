// src/components/Navbar.js

import { useContext } from 'react';
import { Link, NavLink } from 'react-router-dom';
import { ThemeContext } from '../context/ThemeContext';
import '../styles/Navbar.css';

const Navbar = () => {
  const themeContext = useContext(ThemeContext);

  if (!themeContext) {
    return null; // Evita errores si el contexto no está disponible
  }

  const { theme, toggleTheme } = themeContext;

  const getLinkClass = ({ isActive }) => (isActive ? 'navbar-link active' : 'navbar-link');

  return (
    <nav className="navbar">
      <Link to="/" className="navbar-logo">
        Graficador de Excel
      </Link>

      <div className="navbar-links">
        <NavLink to="/" className={getLinkClass}>Inicio</NavLink>
        <NavLink to="/upload" className={getLinkClass}>Subir Archivo</NavLink>
      </div>

      {/* --- INTERRUPTOR DE TEMA CON ICONOS INTERNOS ANIMADOS --- */}
      <div className="theme-switch-wrapper">
        <label className="theme-switch" htmlFor="theme-toggle-checkbox">
          <input
            type="checkbox"
            id="theme-toggle-checkbox"
            onChange={toggleTheme}
            checked={theme === 'dark'}
          />
          <div className="slider">
            {/* El pulgar que se desliza ahora contiene los iconos */}
            <div className="slider-thumb">
              <span className="sun-icon">☀️</span>
              <span className="moon-icon">🌙</span>
            </div>
          </div>
        </label>
      </div>
    </nav>
  );
};

export default Navbar;
