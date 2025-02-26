import { motion } from "framer-motion";
import React, { useEffect, useState } from "react";
import "../styles/CustomCursor.css";

function CustomCursor() {
    const [position, setPosition] = useState({ x: 0, y: 0 });

    useEffect(() => {
        const updateCursor = (e) => {
            setPosition({ x: e.clientX, y: e.clientY });
        };

        window.addEventListener("mousemove", updateCursor);
        return () => window.removeEventListener("mousemove", updateCursor);
    }, []);

    return (
        <motion.div
            className="custom-cursor"
            animate={{ left: position.x, top: position.y }}
            transition={{ type: "spring", stiffness: 100, damping: 10 }}
        >
            <div className="cursor-ring"></div>
        </motion.div>
    );
}

export default CustomCursor;
