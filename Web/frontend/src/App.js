// src/App.js

import { Route, BrowserRouter as Router, Routes } from 'react-router-dom';
import CustomCursor from './components/CustomCursor';
import Footer from './components/Footer';
import Navbar from './components/Navbar';
import { ThemeProvider } from './context/ThemeContext'; // Solo importamos el Provider
import HomePage from './pages/HomePage';
import UploadPage from './pages/UploadPage';

// Ya no necesitamos el componente AppContent.
// App.js ahora es mucho más limpio.
function App() {
  return (
    // 1. Envolvemos toda la aplicación en ThemeProvider.
    //    Este se encargará de aplicar el tema al <body> automáticamente.
    <ThemeProvider>
      <div className="App">
        <CustomCursor />
        <Router>
          <Navbar />
          <main>
            <Routes>
              <Route path="/" element={<HomePage />} />
              <Route path="/upload" element={<UploadPage />} />
            </Routes>
          </main>
          <Footer />
        </Router>
      </div>
    </ThemeProvider>
  );
}

export default App;
