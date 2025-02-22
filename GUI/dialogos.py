import customtkinter as ctk

def mostrar_dialogo_centrado(tipo, titulo, mensaje):
    """
    Muestra un diálogo centrado con CustomTkinter.
    :param tipo: Tipo de diálogo ('info', 'warning', 'error', 'question').
    :param titulo: Título del diálogo.
    :param mensaje: Mensaje a mostrar.
    """
    # Crear ventana de diálogo
    dialogo = ctk.CTkToplevel()
    dialogo.title(titulo)
    
    # Obtener dimensiones de la pantalla
    screen_width = dialogo.winfo_screenwidth()
    screen_height = dialogo.winfo_screenheight()
    dialog_width = 400
    dialog_height = 200
    x = (screen_width - dialog_width) // 2
    y = (screen_height - dialog_height) // 2

    # Configurar geometría para centrar el diálogo
    dialogo.geometry(f"{dialog_width}x{dialog_height}+{x}+{y}")
    dialogo.resizable(False, False)

    # Etiqueta de mensaje
    label = ctk.CTkLabel(dialogo, text=mensaje, font=("Segoe UI", 14))
    label.pack(pady=20)

    # Botón para cerrar
    if tipo in ("info", "warning", "error"):
        ctk.CTkButton(dialogo, text="Aceptar", command=dialogo.destroy).pack(pady=10)
    elif tipo == "question":
        respuesta = []
        def on_yes():
            respuesta.append(True)
            dialogo.destroy()
        def on_no():
            respuesta.append(False)
            dialogo.destroy()
        botones_frame = ctk.CTkFrame(dialogo)
        botones_frame.pack(pady=10)
        ctk.CTkButton(botones_frame, text="Sí", command=on_yes).pack(side="left", padx=10)
        ctk.CTkButton(botones_frame, text="No", command=on_no).pack(side="left", padx=10)
        dialogo.wait_window()
        return respuesta[0]

    dialogo.transient()  # Mantener sobre la ventana principal
    dialogo.grab_set()  # Bloquear interacción con la ventana principal
    dialogo.wait_window()  # Esperar a que se cierre el diálogo
