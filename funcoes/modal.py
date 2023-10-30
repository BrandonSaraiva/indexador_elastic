import tkinter as tk

def modal_input_infos(info):
    # Função para atualizar as informações com os valores dos campos do formulário
    def atualizar_informacoes():
        info["UrlJson"] = url_json_entry.get()
        info["IndexName"] = index_name_entry.get()
        info["ColumnName"] = column_name_entry.get()
        root.destroy()

    # Cria uma janela
    root = tk.Tk()
    root.title("Formulário de Informações")

    # Função para criar um espaço em branco
    def criar_espaco():
        tk.Label(root, text="").pack()

    # Cria rótulos e entradas para cada campo do formulário
    tk.Label(root, text="URL JSON").pack()
    url_json_entry = tk.Entry(root)
    url_json_entry.insert(0, info["UrlJson"])
    url_json_entry.pack()
    criar_espaco()

    tk.Label(root, text="Index Name").pack()
    index_name_entry = tk.Entry(root)
    index_name_entry.insert(0, info["IndexName"])
    index_name_entry.pack()
    criar_espaco()

    tk.Label(root, text="Column Name").pack()
    column_name_entry = tk.Entry(root)
    column_name_entry.insert(0, info["ColumnName"])
    column_name_entry.pack()
    criar_espaco()

    # Botão para atualizar as informações com fundo verde
    atualizar_button = tk.Button(root, text="Atualizar Informações", command=atualizar_informacoes)
    atualizar_button.configure(bg="green")  # Define a cor de fundo para verde
    atualizar_button.pack()
    criar_espaco()

    # Inicia a interface gráfica
    root.mainloop()

    # Após o usuário preencher o formulário e clicar em "Atualizar Informações", os valores serão atualizados em 'info'
    return info

# Agora o botão "Atualizar Informações" terá um fundo verde.
