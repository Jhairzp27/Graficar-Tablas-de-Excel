import { motion } from "framer-motion";
import React, { useContext } from "react";
import { Link } from "react-router-dom";
import { ThemeContext } from "../context/ThemeContext";
import "../styles/Navbar.css";

function Navbar() {
    const { theme, toggleTheme } = useContext(ThemeContext);

    return (
        <motion.nav
            className="navbar"
            initial={{ opacity: 0, y: -50 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5 }}
        >
            <div className="navbar-logo">
                <h1>📊 Graficador de Excel</h1>
            </div>
            <div className="nav-links">
                <Link to="/">Inicio</Link>
                <Link to="/upload">Subir Archivo</Link>
            </div>
            <motion.button
                className="theme-button"
                onClick={toggleTheme}
                whileHover={{ scale: 1.1 }}
            >
                {theme === "light" ? "🌙 Modo Oscuro" : "☀️ Modo Claro"}
            </motion.button>
        </motion.nav>
    );
}

export default Navbar;
