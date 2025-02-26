import React from "react";
import { Route, BrowserRouter as Router, Routes } from "react-router-dom";
import CustomCursor from "./components/CustomCursor";
import Footer from "./components/Footer";
import Navbar from "./components/Navbar";
import HomePage from "./pages/HomePage";
import UploadPage from "./pages/UploadPage";

function App() {
    return (
        <Router>
            <CustomCursor />
            <Navbar />
            <Routes>
                <Route path="/" element={<HomePage />} />
                <Route path="/upload" element={<UploadPage />} />
            </Routes>
            <Footer />
        </Router>
    );
}

export default App;
