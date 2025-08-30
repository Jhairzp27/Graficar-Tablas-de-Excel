// src/context/ThemeContext.js

import { createContext, useEffect, useState } from 'react';

// Creamos el contexto con un valor inicial por defecto.
export const ThemeContext = createContext({
  theme: 'light',
  toggleTheme: () => {},
});

// Creamos el proveedor del tema.
export const ThemeProvider = ({ children }) => {
  // 1. Estado para el tema. Leemos el tema guardado en localStorage
  //    o usamos 'light' si es la primera visita.
  const [theme, setTheme] = useState(() => {
    const savedTheme = localStorage.getItem('theme');
    return savedTheme || 'light';
  });

  // 2. useEffect se ejecuta cada vez que el estado 'theme' cambia.
  useEffect(() => {
    const body = document.body;
    // Limpiamos clases anteriores para evitar conflictos.
    body.classList.remove('light', 'dark');
    // Añadimos la clase del tema actual al body.
    body.classList.add(theme);
    // Guardamos la preferencia del usuario en localStorage.
    localStorage.setItem('theme', theme);
  }, [theme]); // Se vuelve a ejecutar solo si 'theme' cambia.

  // 3. Función para cambiar el tema.
  const toggleTheme = () => {
    setTheme((prevTheme) => (prevTheme === 'light' ? 'dark' : 'light'));
  };

  // 4. Pasamos el tema actual y la función para cambiarlo a todos los componentes hijos.
  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
};
