import B_1
import tkinter as tk
from tkinter import messagebox
from sympy import symbols, diff, sympify
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()
root.title("Forming Conditions")
root.geometry("1200x800")

x1, x2, T, t = symbols('x1 x2 T t')

selected_function_str = tk.StringVar(value="cos(x1)**2 + sin(x2)**2 + T")
u_function_str = tk.StringVar(value="5")

boundary_conditions = []
boundary_conditions_entries = []

boundary_condition_widgets = []
interface_condition_widgets = []

operator_vars_boundary = []
operator_vars_interface = []


def on_closing():
    root.quit()
    root.destroy()


def clear_condition_widgets():
    for widget in boundary_condition_widgets + interface_condition_widgets:
        widget.destroy()
    boundary_condition_widgets.clear()
    interface_condition_widgets.clear()


root.protocol("WM_DELETE_WINDOW", on_closing)


def get_values():
    try:
        x1_min = float(x1_min_entry.get())
        x2_min = float(x2_min_entry.get())
        width = float(width_entry.get())
        height = float(height_entry.get())
        T = float(T_entry.get())
        t_graph = float(t_entry.get())
        x1_max = x1_min + height
        x2_max = x2_min + width

        save_all_conditions()

        results = f"x1 range: {x1_min} to {x1_max}\n"
        results += f"x2 range: {x2_min} to {x2_max}\n"
        results += f"T value: {T}\n"
        results += f"t value for graph: {t_graph}\n"
        results += f"Selected function: {selected_function_str.get()}\n"
        results += f"Defined function u(s): {u_function_str.get()}\n"
        results += f"Boundary conditions:\n"

        for condition, operator in boundary_conditions:
            results += f"  - {operator}: {condition}\n"

        results += f"Interface conditions:\n"
        for condition, operator in boundary_conditions_entries:
            results += f"  - {operator}: {condition}\n"

        messagebox.showinfo("Results", results)

        fig = Figure(figsize=(6, 4), dpi=100)
        ax = fig.add_subplot(111, projection='3d')

        X = np.linspace(x1_min, x1_max, 50)
        Y = np.linspace(x2_min, x2_max, 50)
        X, Y = np.meshgrid(X, Y)
        Z = np.cos(X) ** 2 + np.sin(Y) ** 2 + T

        for condition, operator in boundary_conditions:
            if operator == "1":
                pass
            elif operator == "похідна по t":
                pass
            elif operator == "похідна по x1":
                pass

        for condition, operator in boundary_conditions_entries:
            if operator == "1":
                pass
            elif operator == "похідна по t":
                pass
            elif operator == "похідна по x1":
                pass

        ax.plot_surface(X, Y, Z, cmap='viridis')

        canvas = FigureCanvasTkAgg(fig, root)
        canvas.get_tk_widget().grid(row=20, column=0, columnspan=5, pady=10)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")
    except Exception as e:
        messagebox.showerror("Function Error", f"Error evaluating function: {e}")


operator_options = ["1", "похідна по t", "похідна по x1"]
operator_numbers = [1, 2, 3]


def update_boundary_condition_entry(condition_entry, operator_var):
    operator = operator_var.get()
    if operator == "1":
        condition_entry.delete(0, tk.END)
        condition_entry.insert(0, selected_function_str.get())
    elif operator == "похідна по t":
        condition_entry.delete(0, tk.END)
        condition_entry.insert(0, str(diff(sympify(selected_function_str.get()), t)))
    elif operator == "похідна по x1":
        condition_entry.delete(0, tk.END)
        condition_entry.insert(0, str(diff(sympify(selected_function_str.get()), x1)))


def update_interface_condition_entry(condition_entry, operator_var):
    operator = operator_var.get()
    if operator == "1":
        condition_entry.delete(0, tk.END)
        condition_entry.insert(0, selected_function_str.get())
    elif operator == "похідна по t":
        condition_entry.delete(0, tk.END)
        condition_entry.insert(0, str(diff(sympify(selected_function_str.get()), t)))
    elif operator == "похідна по x1":
        condition_entry.delete(0, tk.END)
        condition_entry.insert(0, str(diff(sympify(selected_function_str.get()), x1)))


def update_condition_entry(condition_entry, operator_var, is_boundary=True):
    operator = operator_var.get()
    if operator == "1":
        condition_entry.delete(0, tk.END)
        condition_entry.insert(0, selected_function_str.get())
    elif operator == "похідна по t":
        condition_entry.delete(0, tk.END)
        condition_entry.insert(0, str(diff(sympify(selected_function_str.get()), t)))
    elif operator == "похідна по x1":
        condition_entry.delete(0, tk.END)
        condition_entry.insert(0, str(diff(sympify(selected_function_str.get()), x1)))
    else:
        condition_entry.delete(0, tk.END)
        condition_entry.insert(0, "")


def enter_conditions():
    try:
        clear_condition_widgets()

        num_boundary_conditions = int(num_boundary_conditions_entry.get())
        num_interface_conditions = int(num_interface_conditions_entry.get())

        if num_boundary_conditions <= 0 or num_interface_conditions <= 0:
            raise ValueError("The number of conditions must be positive.")

        operator_vars_boundary.clear()
        operator_vars_interface.clear()

        for i in range(num_boundary_conditions):
            tk.Label(root, text=f"Boundary Condition {i + 1}:").grid(row=10 + i, column=0, sticky=tk.W)
            condition_entry = tk.Entry(root, width=30)
            condition_entry.grid(row=10 + i, column=1, columnspan=3)

            operator_var = tk.StringVar(value=operator_options[0])
            operator_vars_boundary.append(operator_var)
            operator_menu = tk.OptionMenu(root, operator_var, *operator_options, command=lambda x: update_condition_entry(condition_entry, operator_var, is_boundary=True))
            operator_menu.grid(row=10 + i, column=4)

            boundary_condition_widgets.extend([condition_entry, operator_menu])

        for i in range(num_interface_conditions):
            tk.Label(root, text=f"Interface Condition {i + 1}:").grid(row=10 + num_boundary_conditions + i, column=0, sticky=tk.W)
            condition_entry = tk.Entry(root, width=30)
            condition_entry.grid(row=10 + num_boundary_conditions + i, column=1, columnspan=3)

            operator_var = tk.StringVar(value=operator_options[0])
            operator_vars_interface.append(operator_var)
            operator_menu = tk.OptionMenu(root, operator_var, *operator_options, command=lambda x: update_condition_entry(condition_entry, operator_var, is_boundary=False))
            operator_menu.grid(row=10 + num_boundary_conditions + i, column=4)

            interface_condition_widgets.extend([condition_entry, operator_menu])

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))


def save_all_conditions():
    try:
        boundary_conditions.clear()
        boundary_conditions_entries.clear()

        for i in range(0, len(boundary_condition_widgets), 2):
            condition_entry = boundary_condition_widgets[i]
            operator_var = operator_vars_boundary[i//2]

            condition = condition_entry.get()
            operator = operator_var.get()

            boundary_conditions.append([condition, operator])

        for i in range(0, len(interface_condition_widgets), 2):
            condition_entry = interface_condition_widgets[i]
            operator_var = operator_vars_interface[i//2]

            condition = condition_entry.get()
            operator = operator_var.get()

            boundary_conditions_entries.append([condition, operator])

        messagebox.showinfo("Success", f"All boundary conditions saved: {boundary_conditions}\nAll interface conditions saved: {boundary_conditions_entries}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid values for all conditions.")


def clear_conditions():
    boundary_conditions.clear()
    boundary_conditions_entries.clear()

    for entry_widget in boundary_condition_widgets:
        if isinstance(entry_widget, tk.Entry):
            entry_widget.delete(0, tk.END)
            entry_widget.insert(0, "0")

    for entry_widget in interface_condition_widgets:
        if isinstance(entry_widget, tk.Entry):
            entry_widget.delete(0, tk.END)
            entry_widget.insert(0, "0")

    for entry in [x1_min_entry, x2_min_entry, width_entry, height_entry, T_entry, t_entry,
                  num_boundary_conditions_entry, num_interface_conditions_entry]:
        entry.delete(0, tk.END)
        entry.insert(0, "0")

    messagebox.showinfo("Cleared", "All conditions have been cleared and set to 0.")


def save_function_entries():
    selected_function_str.set(selected_function_entry.get())
    u_function_str.set(u_function_entry.get())
    messagebox.showinfo("Function Saved", f"Selected function: {selected_function_str.get()}\n"
                                          f"u(s) function: {u_function_str.get()}")


tk.Label(root, text="Selected function:").grid(row=0, column=0)
selected_function_entry = tk.Entry(root, textvariable=selected_function_str, width=30)
selected_function_entry.grid(row=0, column=1, columnspan=3)
selected_function_entry.insert(0, "cos(x1)**2 + sin(x2)**2 + T")

tk.Label(root, text="Function u(s):").grid(row=1, column=0)
u_function_entry = tk.Entry(root, textvariable=u_function_str, width=30)
u_function_entry.grid(row=1, column=1, columnspan=3)
u_function_entry.insert(0, "5")

tk.Label(root, text="Minimum value of x1:").grid(row=2, column=0)
x1_min_entry = tk.Entry(root, width=10)
x1_min_entry.grid(row=2, column=1)
x1_min_entry.insert(0, "0")

tk.Label(root, text="Minimum value of x2:").grid(row=3, column=0)
x2_min_entry = tk.Entry(root, width=10)
x2_min_entry.grid(row=3, column=1)
x2_min_entry.insert(0, "0")

tk.Label(root, text="Width (for x1):").grid(row=4, column=0)
width_entry = tk.Entry(root, width=10)
width_entry.grid(row=4, column=1)
width_entry.insert(0, "2")

tk.Label(root, text="Height (for x2):").grid(row=5, column=0)
height_entry = tk.Entry(root, width=10)
height_entry.grid(row=5, column=1)
height_entry.insert(0, "2")

tk.Label(root, text="Value of T:").grid(row=6, column=0)
T_entry = tk.Entry(root, width=10)
T_entry.grid(row=6, column=1)
T_entry.insert(0, "2")

tk.Label(root, text="t value for graph:").grid(row=7, column=0)
t_entry = tk.Entry(root, width=10)
t_entry.grid(row=7, column=1)
t_entry.insert(0, "0")

tk.Label(root, text="Number of boundary conditions:").grid(row=4, column=3)
num_boundary_conditions_entry = tk.Entry(root, width=10)
num_boundary_conditions_entry.grid(row=4, column=4)
num_boundary_conditions_entry.insert(0, "1")

tk.Label(root, text="Number of interface conditions:").grid(row=5, column=3)
num_interface_conditions_entry = tk.Entry(root, width=10)
num_interface_conditions_entry.grid(row=5, column=4)
num_interface_conditions_entry.insert(0, "1")

get_values_button = tk.Button(root, text="Get Values and Plot Graph", command=get_values, bg="pale green")
get_values_button.grid(row=9, column=0, padx=15, pady=15)

enter_conditions_button = tk.Button(root, text="Enter Conditions", command=enter_conditions, bg="burlywood1")
enter_conditions_button.grid(row=9, column=1)

clear_conditions_button = tk.Button(root, text="Clear All Conditions", command=clear_conditions, bg="coral1")
clear_conditions_button.grid(row=9, column=3)

save_function_button = tk.Button(root, text="Save Functions", command=save_function_entries, bg="light blue")
save_function_button.grid(row=9, column=4, padx=15, pady=15)

root.mainloop()
