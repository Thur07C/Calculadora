import tkinter as tk
from tkinter import messagebox

# Função para realizar os cálculos
def calcular():
    opcao = combo_operacao.get()
    
    try:
        num1 = float(entry_num1.get())
        
        # Operação de Raiz Quadrada usa apenas 1 número
        if opcao == "Raiz Quadrada":
            if num1 >= 0:
                resultado = num1 ** 0.5
                label_resultado.config(text=f"Resultado: {resultado:.2f}")
            else:
                messagebox.showerror("Erro", "Não existe raiz real para números negativos.")
            return

        num2 = float(entry_num2.get())
        
        if opcao == "Soma":
            resultado = num1 + num2
        elif opcao == "Subtração":
            resultado = num1 - num2
        elif opcao == "Multiplicação":
            resultado = num1 * num2
        elif opcao == "Divisão":
            if num2 != 0:
                resultado = num1 / num2
            else:
                messagebox.showerror("Erro", "Divisão por zero não é permitida.")
                return
        elif opcao == "Potência":
            resultado = num1 ** num2
            
        label_resultado.config(text=f"Resultado: {resultado:.2f}")
        
    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite números válidos.")

# Criação da janela principal
janela = tk.Tk()
janela.title("Calculadora Visual")
janela.geometry("300x300")
janela.config(padding=20)

# Rótulos e Campos de Entrada
tk.Label(janela, text="1º Número:").pack(anchor="w")
entry_num1 = tk.Entry(janela)
entry_num1.pack(fill="x", pady=5)

tk.Label(janela, text="2º Número (se aplicável):").pack(anchor="w")
entry_num2 = tk.Entry(janela)
entry_num2.pack(fill="x", pady=5)

# Menu de Seleção da Operação
tk.Label(janela, text="Operação:").pack(anchor="w")
operacoes = ["Soma", "Subtração", "Multiplicação", "Divisão", "Potência", "Raiz Quadrada"]
combo_operacao = tk.StringVar(janela)
combo_operacao.set(operacoes[0]) # Valor padrão

menu_operacao = tk.OptionMenu(janela, combo_operacao, *operacoes)
menu_operacao.pack(fill="x", pady=5)

# Botão de Calcular
btn_calcular = tk.Button(janela, text="Calcular", command=calcular, bg="#4CAF50", fg="white")
btn_calcular.pack(fill="x", pady=15)

# Rótulo para Exibir o Resultado
label_resultado = tk.Label(janela, text="Resultado: ", font=("Arial", 12, "bold"))
label_resultado.pack()

# Loop principal da janela
janela.mainloop()
