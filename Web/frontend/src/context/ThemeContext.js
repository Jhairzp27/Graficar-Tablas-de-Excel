import { createContext, useEffect, useState } from "react";

// Crear el contexto del tema
export const ThemeContext = createContext();

export const ThemeProvider = ({ children }) => {
    // Estado del tema (se obtiene de localStorage si existe, sino "light" por defecto)
    const [theme, setTheme] = useState(() => {
        return localStorage.getItem("theme") || "light";
    });

    // Efecto que cambia el atributo "data-theme" y guarda en localStorage
    useEffect(() => {
        document.documentElement.setAttribute("data-theme", theme);
        localStorage.setItem("theme", theme);
    }, [theme]);

    // Función para alternar entre modos
    const toggleTheme = () => {
        setTheme((prevTheme) => (prevTheme === "light" ? "dark" : "light"));
    };

    return (
        <ThemeContext.Provider value={{ theme, toggleTheme }}>
            {children}
        </ThemeContext.Provider>
    );
};
