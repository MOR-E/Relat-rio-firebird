import tkinter as tk
from tkinter import filedialog, messagebox
from tkcalendar import DateEntry
import pandas as pd
import fdb

def run_query():
    data_inicio = entry_data_inicio.get_date().strftime("%Y-%m-%d")  # banco espera YYYY-MM-DD
    data_fim = entry_data_fim.get_date().strftime("%Y-%m-%d")
    cliente_id = entry_cliente.get().strip()
    placa = entry_placa.get().strip()

    # Lê a query base
    with open("query.sql", "r", encoding="utf-8") as f:
        query_base = f.read()

    conditions = []
    params = []

    if cliente_id:
        conditions.append("r.CLIENTES_ID = ?")
        params.append(int(cliente_id))

    if placa:
        conditions.append("s.SAIDA_PLACA_VEICULO = ?")
        params.append(placa)

    if data_inicio and data_fim:
        conditions.append("r.SAIDA_DATA_SAIDA BETWEEN ? AND ?")
        params.append(data_inicio)
        params.append(data_fim)

    query_final = query_base
    if conditions:
        query_final += " WHERE " + " AND ".join(conditions)

    query_final += " ORDER BY r.CLIENTE_NOME1, r.PRODUTO_NOME"

    try:
        with open("connection.txt", "r", encoding="utf-8") as f:
            conn_params = {}
            for line in f:
                if "=" in line:
                    k, v = line.strip().split("=", 1)
                    conn_params[k.strip()] = v.strip()

        conn = fdb.connect(
            dsn=conn_params.get("dsn"),
            user=conn_params.get("user"),
            password=conn_params.get("password"),
            charset=conn_params.get("charset", "UTF8")
        )

        df = pd.read_sql(query_final, conn, params=tuple(params))

        # Formatar datas para padrão brasileiro
        if "Data da Saída" in df.columns:
            df["Data da Saída"] = pd.to_datetime(df["Data da Saída"]).dt.strftime("%d/%m/%Y")

        # Nome padrão para salvar
        default_name = "Relatório"
        if cliente_id:
            default_name += f"_cliente{cliente_id}"
        if placa:
            default_name += f"_placa{placa}"

        file_path = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Excel files", "*.xlsx")],
            initialfile=default_name
        )

        if file_path:
            df.to_excel(file_path, index=False)
            messagebox.showinfo("Sucesso", f"Relatório salvo em:\n{file_path}")
        else:
            messagebox.showwarning("Cancelado", "O salvamento foi cancelado.")

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao executar a consulta:\n{e}")

    finally:
        if 'conn' in locals():
            conn.close()

# ==== INTERFACE TKINTER + TKCALENDAR ====
root = tk.Tk()
root.title("Gerador de Relatórios Firebird")

tk.Label(root, text="Data início:").grid(row=0, column=0, padx=5, pady=5)
entry_data_inicio = DateEntry(
    root,
    width=12,
    background='darkblue',
    foreground='white',
    borderwidth=2,
    date_pattern="dd/mm/yyyy",
    locale="pt_BR"
)
entry_data_inicio.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Data fim:").grid(row=1, column=0, padx=5, pady=5)
entry_data_fim = DateEntry(
    root,
    width=12,
    background='darkblue',
    foreground='white',
    borderwidth=2,
    date_pattern="dd/mm/yyyy",
    locale="pt_BR"
)
entry_data_fim.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="ID Cliente(opcional):").grid(row=2, column=0, padx=5, pady=5)
entry_cliente = tk.Entry(root)
entry_cliente.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Placa do veículo(opcional):").grid(row=3, column=0, padx=5, pady=5)
entry_placa = tk.Entry(root)
entry_placa.grid(row=3, column=1, padx=5, pady=5)

btn_run = tk.Button(root, text="Gerar Relatório", command=run_query)
btn_run.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
