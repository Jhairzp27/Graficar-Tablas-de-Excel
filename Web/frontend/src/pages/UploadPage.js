// src/pages/UploadPage.js

import { AlertTriangle, Sigma, TrendingDown, TrendingUp } from 'lucide-react';
import { useCallback, useEffect, useMemo, useState } from 'react';
import { CartesianGrid, Legend, Line, LineChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts';
import * as XLSX from 'xlsx';
import '../styles/UploadPage.css';

// --- Componente para la Tabla (con resaltado de filas) ---
const DataTable = ({ columns, data, analysisData }) => {
  if (!columns.length || !data.length) return null;

  const identifierKey = columns[0]; // Asumimos que la primera columna es el identificador

  return (
    <div className="table-container">
      <table className="styled-table">
        <thead>
          <tr>
            {columns.map((col) => (<th key={col}>{col}</th>))}
          </tr>
        </thead>
        <tbody>
          {data.map((row, rowIndex) => {
            const rowIdentifier = row[identifierKey];
            let rowClass = '';

            // Asignamos una clase CSS basada en los resultados del análisis
            if (analysisData) {
              if (rowIdentifier === analysisData.max.identifier) {
                rowClass = 'row-max';
              } else if (rowIdentifier === analysisData.min.identifier) {
                rowClass = 'row-min';
              } else if (analysisData.toTrack.some(item => item.identifier === rowIdentifier)) {
                rowClass = 'row-track';
              }
            }

            return (
              <tr key={rowIndex} className={rowClass}>
                {columns.map((col) => (<td key={col}>{row[col]}</td>))}
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
};


// --- Componente para el Gráfico (sin cambios) ---
const DataChart = ({ data, xKey, yKey }) => {
  const processedData = useMemo(() => 
    data.map(item => ({
      ...item,
      [yKey]: Number(item[yKey])
    })).filter(item => !isNaN(item[yKey])),
    [data, yKey]
  );

  if (!data.length || !xKey || !yKey) return null;
  return (
    <ResponsiveContainer width="100%" height={400}>
      <LineChart data={processedData} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
        <CartesianGrid strokeDasharray="3 3" stroke="#ccc" />
        <XAxis dataKey={xKey} />
        <YAxis />
        <Tooltip contentStyle={{ backgroundColor: 'var(--surface-color)', border: '1px solid var(--border-color)', borderRadius: 'var(--border-radius)' }} />
        <Legend />
        <Line type="monotone" dataKey={yKey} stroke="var(--primary-color)" strokeWidth={2} activeDot={{ r: 8 }} dot={{ r: 4 }} />
      </LineChart>
    </ResponsiveContainer>
  );
};

// --- Componente para mostrar el Análisis de Datos (sin cambios) ---
const DataAnalysis = ({ analysisData }) => {
    if (!analysisData) return null;
    const { max, min, average, toTrack } = analysisData;
  
    return (
      <div className="analysis-container">
        <div className="analysis-item">
          <TrendingUp size={24} className="analysis-icon" color="#28a745" />
          <div>
            <strong>Valor Más Alto:</strong> {max.value.toLocaleString()}
            <small> (Fila: {max.identifier})</small>
          </div>
        </div>
        <div className="analysis-item">
          <TrendingDown size={24} className="analysis-icon" color="#dc3545" />
          <div>
            <strong>Valor Más Bajo:</strong> {min.value.toLocaleString()}
            <small> (Fila: {min.identifier})</small>
          </div>
        </div>
        <div className="analysis-item">
          <Sigma size={24} className="analysis-icon" color="#007bff" />
          <div>
            <strong>Promedio:</strong> {average.toLocaleString(undefined, { maximumFractionDigits: 2 })}
          </div>
        </div>
        {toTrack.length > 0 && (
          <div className="analysis-item tracking">
            <AlertTriangle size={24} className="analysis-icon" color="#ffc107" />
            <div>
              <strong>Puntos de Seguimiento ({toTrack.length}):</strong>
              <ul>
                {toTrack.map(item => (
                  <li key={item.identifier}>
                    {item.identifier}: {item.value.toLocaleString()}
                  </li>
                ))}
              </ul>
            </div>
          </div>
        )}
      </div>
    );
  };

// --- Componente Principal de la Página (Lógica Mejorada) ---
const UploadPage = () => {
  const [file, setFile] = useState(null);
  const [workbook, setWorkbook] = useState(null);
  const [sheetNames, setSheetNames] = useState([]);
  const [selectedSheet, setSelectedSheet] = useState('');
  const [headerRow, setHeaderRow] = useState(1);
  const [columns, setColumns] = useState([]);
  const [data, setData] = useState([]);
  const [selectedColumns, setSelectedColumns] = useState({ x: '', y: '' });
  const [error, setError] = useState('');
  const [analysisResults, setAnalysisResults] = useState(null);

  const processSheet = useCallback((wb, sheetName, headerRowNumber) => {
    if (!wb) return;
    const ws = wb.Sheets[sheetName];
    const aoaData = XLSX.utils.sheet_to_json(ws, { header: 1, defval: "" });
    
    if (aoaData.length > 0) {
      const headerIndex = headerRowNumber - 1;
      if (headerIndex >= aoaData.length) {
        setError(`La fila ${headerRowNumber} no existe en esta hoja.`);
        setColumns([]);
        setData([]);
        return;
      }
      
      const headers = aoaData[headerIndex].filter(h => h !== "");
      
      const rows = aoaData.slice(headerIndex + 1).map(rowArray => {
        const rowData = {};
        headers.forEach((header) => {
          const originalIndex = aoaData[headerIndex].indexOf(header);
          rowData[header] = rowArray[originalIndex];
        });
        return rowData;
      }).filter(row => Object.values(row).some(cell => cell !== ""));

      setColumns(headers);
      setData(rows);
      setSelectedColumns({ x: '', y: '' });
      setError('');
    } else {
      setColumns([]);
      setData([]);
    }
  }, []);

  useEffect(() => {
    if (data.length > 0 && selectedColumns.y && columns.length > 0) {
      const yKey = selectedColumns.y;
      const identifierKey = columns[0];

      const numericData = data
        .map(row => ({
          ...row,
          value: parseFloat(row[yKey]),
          identifier: row[identifierKey]
        }))
        .filter(row => !isNaN(row.value) && row.identifier);

      if (numericData.length > 0) {
        let max = { value: -Infinity, identifier: '' };
        let min = { value: Infinity, identifier: '' };
        let sum = 0;

        numericData.forEach(row => {
          if (row.value > max.value) max = { value: row.value, identifier: row.identifier };
          if (row.value < min.value) min = { value: row.value, identifier: row.identifier };
          sum += row.value;
        });

        const average = sum / numericData.length;
        const toTrack = numericData.filter(row => row.value > average * 1.25);

        setAnalysisResults({ max, min, average, toTrack });
      } else {
        setAnalysisResults(null);
      }
    } else {
      setAnalysisResults(null);
    }
  }, [data, selectedColumns.y, columns]);

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile) {
      setFile(selectedFile);
      setError('');
      
      const reader = new FileReader();
      reader.onload = (event) => {
        const bstr = event.target.result;
        const wb = XLSX.read(bstr, { type: 'binary' });
        
        setWorkbook(wb);
        setSheetNames(wb.SheetNames);
        const firstSheetName = wb.SheetNames[0];
        setSelectedSheet(firstSheetName);

        const ws = wb.Sheets[firstSheetName];
        const aoa = XLSX.utils.sheet_to_json(ws, { header: 1, defval: "" });
        let bestHeaderRow = 1;
        let maxNonEmpty = 0;
        aoa.slice(0, 10).forEach((row, index) => {
            const nonEmptyCount = row.filter(cell => cell !== "").length;
            if (nonEmptyCount > maxNonEmpty) {
                maxNonEmpty = nonEmptyCount;
                bestHeaderRow = index + 1;
            }
        });
        
        setHeaderRow(bestHeaderRow);
        processSheet(wb, firstSheetName, bestHeaderRow);
      };
      reader.readAsBinaryString(selectedFile);
    }
  };

  const handleSheetChange = (e) => {
    const newSheetName = e.target.value;
    setSelectedSheet(newSheetName);
    processSheet(workbook, newSheetName, headerRow);
  };
  
  const handleHeaderRowChange = (e) => {
      const newRow = parseInt(e.target.value, 10);
      if (newRow > 0) {
          setHeaderRow(newRow);
          processSheet(workbook, selectedSheet, newRow);
      }
  };

  const handleColumnChange = (e) => {
    setSelectedColumns({ ...selectedColumns, [e.target.name]: e.target.value });
  };

  const handleGeneratePDF = async () => {
    // ... (sin cambios)
  };

  return (
    <main className="upload-page-main">
      <aside className="controls-sidebar card">
        <h2>Controles</h2>
        <p>Sube tu archivo, selecciona los datos y genera tu reporte.</p>
        
        <div className="control-group">
          <label htmlFor="file-upload" className="file-input-label">
            <input id="file-upload" type="file" onChange={handleFileChange} accept=".xlsx, .xls, .csv, .xlsm, .xlsb" />
            <span>Haz clic para seleccionar un archivo</span>
          </label>
          {file && <p className="file-name">Archivo: {file.name}</p>}
        </div>

        {workbook && (
          <>
            {sheetNames.length > 1 && (
              <div className="control-group">
                <label htmlFor="sheet-select">Selecciona una Hoja</label>
                <select id="sheet-select" value={selectedSheet} onChange={handleSheetChange} className="custom-select">
                  {sheetNames.map(name => <option key={name} value={name}>{name}</option>)}
                </select>
              </div>
            )}

            <div className="control-group">
                <label htmlFor="header-row-input">Fila de Encabezado</label>
                <input 
                    type="number" 
                    id="header-row-input" 
                    value={headerRow} 
                    onChange={handleHeaderRowChange} 
                    className="custom-select"
                    min="1"
                />
            </div>
          </>
        )}

        {columns.length > 0 && (
          <>
            <div className="control-group">
              <label htmlFor="x-axis-select">Eje X (Horizontal)</label>
              <select id="x-axis-select" name="x" value={selectedColumns.x} onChange={handleColumnChange} className="custom-select">
                <option value="">-- Selecciona --</option>
                {columns.map((col) => <option key={col} value={col}>{col}</option>)}
              </select>
            </div>

            <div className="control-group">
              <label htmlFor="y-axis-select">Eje Y (Vertical)</label>
              <select id="y-axis-select" name="y" value={selectedColumns.y} onChange={handleColumnChange} className="custom-select">
                <option value="">-- Selecciona --</option>
                {columns.map((col) => <option key={col} value={col}>{col}</option>)}
              </select>
            </div>

            <button onClick={handleGeneratePDF} className="btn">Generar Reporte en PDF</button>
          </>
        )}

        {error && <p style={{ color: 'var(--error-color)' }}>{error}</p>}
      </aside>

      <section className="main-content">
        {analysisResults && (
            <div className="card">
                <h2>Análisis Rápido de "{selectedColumns.y}"</h2>
                <DataAnalysis analysisData={analysisResults} />
            </div>
        )}

        <div className="card">
          <h2>Gráfico de Datos</h2>
          {data.length > 0 && selectedColumns.x && selectedColumns.y ? (
            <DataChart data={data} xKey={selectedColumns.x} yKey={selectedColumns.y} />
          ) : (
            <div className="empty-state">
              <h3>Visualización del Gráfico</h3>
              <p>Sube un archivo y selecciona las columnas X e Y para ver el gráfico aquí.</p>
            </div>
          )}
        </div>
        <div className="card">
          <h2>Vista Previa de la Tabla</h2>
          {data.length > 0 ? (
            // Pasamos los resultados del análisis a la tabla
            <DataTable columns={columns} data={data} analysisData={analysisResults} />
          ) : (
            <div className="empty-state">
              <h3>Datos del Archivo</h3>
              <p>Sube un archivo de Excel para ver los datos aquí.</p>
            </div>
          )}
        </div>
      </section>
    </main>
  );
};

export default UploadPage;
