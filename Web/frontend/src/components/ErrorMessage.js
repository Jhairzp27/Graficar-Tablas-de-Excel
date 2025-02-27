import React from "react";
import "../styles/ErrorMessage.css"; // Importaremos estilos aquí

function ErrorMessage({ message }) {
    if (!message) return null;

    return (
        <div className="error-message">
            <p>⚠️ {message}</p>
        </div>
    );
}

export default ErrorMessage;
