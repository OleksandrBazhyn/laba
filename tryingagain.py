import B_1
import tkinter as tk
from tkinter import messagebox, ttk
from sympy import symbols, diff, sympify
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()
root.title("Forming Conditions")
root.geometry("1200x800")

x1, x2, T, t = symbols('x1 x2 T t')

selected_function_str = tk.StringVar(value="x1 ** 2 + x2 ** 2 + T")  # Default function
u_function_str = tk.StringVar(value="5")  # Default for u(s)

boundary_conditions = []
boundary_conditions_entries = []

# Lists for entry widgets for easy access
boundary_condition_widgets = []
interface_condition_widgets = []

# List to store operator variables
operator_vars_boundary = []
operator_vars_interface = []


def on_closing():
    root.quit()
    root.destroy()


# Clear existing condition entry widgets
def clear_condition_widgets():
    for widget in boundary_condition_widgets + interface_condition_widgets:
        widget.destroy()
    boundary_condition_widgets.clear()
    interface_condition_widgets.clear()


root.protocol("WM_DELETE_WINDOW", on_closing)  # Bind the closing event


# Function to get values, display results, and plot graph
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

        # Display results with selected and u(s) functions
        results = f"x1 range: {x1_min} to {x1_max}\n"
        results += f"x2 range: {x2_min} to {x2_max}\n"
        results += f"T value: {T}\n"
        results += f"t value for graph: {t_graph}\n"
        results += "Selected function: x1 ** 2 + x2 ** 2 + T\n"
        results += "Defined function u(s): 5\n"
        results += f"Boundary conditions: {boundary_conditions}\n"
        results += f"Interface conditions: {boundary_conditions_entries}"
        messagebox.showinfo("Results", results)

        # Create 3D graph
        fig = Figure(figsize=(6, 4), dpi=100)
        ax = fig.add_subplot(111, projection='3d')

        # Generate sample data for plotting (replace with actual function if needed)
        X = np.linspace(x1_min, x1_max, 50)
        Y = np.linspace(x2_min, x2_max, 50)
        X, Y = np.meshgrid(X, Y)
        # Z = eval(selected_function_str.get())  # Use eval to evaluate the function dynamically
        Z = X ** 2 + Y ** 2 + T  # Example function, adjust as needed

        ax.plot_surface(X, Y, Z, cmap='viridis')

        # Display the graph in the tkinter window
        canvas = FigureCanvasTkAgg(fig, root)
        canvas.get_tk_widget().grid(row=20, column=0, columnspan=5, pady=10)  # Position under main inputs

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")
    except Exception as e:
        messagebox.showerror("Function Error", f"Error evaluating function: {e}")


# Function to dynamically enter conditions
operator_options = ["1", "похідна по t", "похідна по x1"]
operator_numbers = [1, 2, 3]  # Numeric representations


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
        # Clear existing condition entry fields
        clear_condition_widgets()

        # Get the number of boundary and interface conditions
        num_boundary_conditions = int(num_boundary_conditions_entry.get())
        num_interface_conditions = int(num_interface_conditions_entry.get())

        if num_boundary_conditions <= 0 or num_interface_conditions <= 0:
            raise ValueError("The number of conditions must be positive.")

        # Clear operator variables
        operator_vars_boundary.clear()
        operator_vars_interface.clear()

        # Create entry fields for each boundary condition
        for i in range(num_boundary_conditions):
            tk.Label(root, text=f"Boundary Condition {i + 1}:").grid(row=10 + i, column=0, sticky=tk.W)
            condition_entry = tk.Entry(root, width=30)
            condition_entry.grid(row=10 + i, column=1, columnspan=3)

            # Create OptionMenu for operator
            operator_var = tk.StringVar(value=operator_options[0])
            operator_vars_boundary.append(operator_var)  # Save operator variable
            operator_menu = tk.OptionMenu(root, operator_var, *operator_options, command=lambda x: update_condition_entry(condition_entry, operator_var, is_boundary=True))
            operator_menu.grid(row=10 + i, column=4)

            # Store widgets
            boundary_condition_widgets.extend([condition_entry, operator_menu])

        # Create entry fields for each interface condition
        for i in range(num_interface_conditions):
            tk.Label(root, text=f"Interface Condition {i + 1}:").grid(row=10 + num_boundary_conditions + i, column=0, sticky=tk.W)
            condition_entry = tk.Entry(root, width=30)
            condition_entry.grid(row=10 + num_boundary_conditions + i, column=1, columnspan=3)

            # Create OptionMenu for operator
            operator_var = tk.StringVar(value=operator_options[0])
            operator_vars_interface.append(operator_var)  # Save operator variable
            operator_menu = tk.OptionMenu(root, operator_var, *operator_options, command=lambda x: update_condition_entry(condition_entry, operator_var, is_boundary=False))
            operator_menu.grid(row=10 + num_boundary_conditions + i, column=4)

            # Store widgets
            interface_condition_widgets.extend([condition_entry, operator_menu])

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))


def save_all_conditions():
    try:
        # Clear existing boundary conditions to avoid duplicates
        boundary_conditions.clear()
        boundary_conditions_entries.clear()

        # Loop through all boundary condition widgets
        for i in range(0, len(boundary_condition_widgets), 2):
            # Get the corresponding entry and operator for each condition
            condition_entry = boundary_condition_widgets[i]
            operator_var = boundary_condition_widgets[i + 1]

            # Get the values from the entries
            condition = condition_entry.get()
            operator = operator_var.value  # Use .value instead of .get()

            # Append to the boundary_conditions
            boundary_conditions.append([condition, operator])

        # Loop through all interface condition widgets
        for i in range(0, len(interface_condition_widgets), 2):
            # Get the corresponding entry and operator for each condition
            condition_entry = interface_condition_widgets[i]
            operator_var = interface_condition_widgets[i + 1]

            # Get the values from the entries
            condition = condition_entry.get()
            operator = operator_var.value  # Use .value instead of .get()

            # Append to the boundary_conditions_entries
            boundary_conditions_entries.append([condition, operator])

        # Show message with all saved conditions
        messagebox.showinfo("Success", f"All boundary conditions saved: {boundary_conditions}\nAll interface conditions saved: {boundary_conditions_entries}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid values for all conditions.")


def clear_conditions():
    # Clear stored boundary and interface conditions
    boundary_conditions.clear()
    boundary_conditions_entries.clear()

    # Set all entry widgets related to boundary conditions to 0
    for entry_widget in boundary_condition_widgets:
        if isinstance(entry_widget, tk.Entry):
            entry_widget.delete(0, tk.END)
            entry_widget.insert(0, "0")  # Set to 0 after clearing

    # Set all entry widgets related to interface conditions to 0
    for entry_widget in interface_condition_widgets:
        if isinstance(entry_widget, tk.Entry):
            entry_widget.delete(0, tk.END)
            entry_widget.insert(0, "0")  # Set to 0 after clearing

    # Clear main parameter fields
    for entry in [x1_min_entry, x2_min_entry, width_entry, height_entry, T_entry, t_entry,
                  num_boundary_conditions_entry, num_interface_conditions_entry]:
        entry.delete(0, tk.END)
        entry.insert(0, "0")  # Set to 0 after clearing

    # Show a message indicating that all conditions have been cleared and set to 0
    messagebox.showinfo("Cleared", "All conditions have been cleared and set to 0.")


# Save function text fields
def save_function_entries():
    selected_function_str.set(selected_function_entry.get())
    u_function_str.set(u_function_entry.get())
    messagebox.showinfo("Function Saved", f"Selected function: {selected_function_str.get()}\n"
                                          f"u(s) function: {u_function_str.get()}")


tk.Label(root, text="Selected function:").grid(row=0, column=0)
selected_function_entry = tk.Entry(root, textvariable=selected_function_str, width=30)
selected_function_entry.grid(row=0, column=1, columnspan=3)
selected_function_entry.insert(0, "x1**2 + x2**2 + T")

tk.Label(root, text="Function u(s):").grid(row=1, column=0)
u_function_entry = tk.Entry(root, textvariable=u_function_str, width=30)
u_function_entry.grid(row=1, column=1, columnspan=3)
u_function_entry.insert(0, "5")

# UI Elements for input
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

# Entry for T with default value 0
tk.Label(root, text="Value of T:").grid(row=6, column=0)
T_entry = tk.Entry(root, width=10)
T_entry.grid(row=6, column=1)
T_entry.insert(0, "2")

# Entry for t value for graph with default value 0
tk.Label(root, text="t value for graph:").grid(row=7, column=0)
t_entry = tk.Entry(root, width=10)
t_entry.grid(row=7, column=1)
t_entry.insert(0, "0")

# Fields for entering the number of boundary and interface conditions
tk.Label(root, text="Number of boundary conditions:").grid(row=4, column=3)
num_boundary_conditions_entry = tk.Entry(root, width=10)
num_boundary_conditions_entry.grid(row=4, column=4)
num_boundary_conditions_entry.insert(0, "1")

tk.Label(root, text="Number of interface conditions:").grid(row=5, column=3)
num_interface_conditions_entry = tk.Entry(root, width=10)
num_interface_conditions_entry.grid(row=5, column=4)
num_interface_conditions_entry.insert(0, "1")

# Buttons to save conditions
# Button to get values and plot graph
get_values_button = tk.Button(root, text="Get Values and Plot Graph", command=get_values, bg="pale green")
get_values_button.grid(row=9, column=0, padx=15, pady=15)

enter_conditions_button = tk.Button(root, text="Enter Conditions", command=enter_conditions, bg="khaki1")
enter_conditions_button.grid(row=9, column=1)

# save_all_conditions_button = tk.Button(root, text="Save All Conditions", command=save_all_conditions, bg="burlywood1")
# save_all_conditions_button.grid(row=9, column=2)

# Button to save conditions
save_conditions_button = tk.Button(root, text="Save Conditions", command=save_all_conditions, bg="burlywood1")
save_conditions_button.grid(row=9, column=2)

# Button to clear all conditions
clear_conditions_button = tk.Button(root, text="Clear All Conditions", command=clear_conditions, bg="coral1")
clear_conditions_button.grid(row=9, column=3)

save_function_button = tk.Button(root, text="Save Functions", command=save_function_entries, bg="light blue")
save_function_button.grid(row=9, column=4, padx=15, pady=15)

root.mainloop()
