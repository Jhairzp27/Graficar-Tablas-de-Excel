from pydantic import BaseModel
from typing import List, Optional

class GraphConfig(BaseModel):
    graph_type: str  # Tipo de gráfico (barras, líneas, pastel, dispersión)
    x_column: str  # Columna del eje X
    y_column: str  # Columna del eje Y
    title: Optional[str] = "Gráfico Generado"
    x_label: Optional[str] = ""
    y_label: Optional[str] = ""
    colors: Optional[List[str]] = None
    highlight_bar: Optional[str] = None
    show_legend: bool = True
    show_values: bool = False
    invert_colors: bool = False
    font_size: Optional[int] = 12
