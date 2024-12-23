import tkinter as tk
from tkinter import messagebox
import math

def calculate_photos():
    try:
        # Get user input parameters
        W = float(entry_W.get())  # Width of the photo area (m)
        L = float(entry_L.get())  # Length of the photo area (m)
        C_L = float(entry_CL.get())  # Coverage width of one photo (m)
        x = float(entry_x.get())  # Sensor's long side dimension (m)
        f = float(entry_f.get())  # Focal length (m)
        H = float(entry_H.get())  # Flight height (m)
        R1 = float(entry_R1.get())  # Lateral overlap
        R2 = float(entry_R2.get())  # Longitudinal overlap

        def calculate_k1(L, C_L, R1):
            # Calculate the number of photos needed in the length direction considering lateral overlap
            return L / (C_L * (1 - R1))

        def calculate_k2(W, f, x, R2, H):
            # Calculate the number of photos needed in the width direction considering longitudinal overlap
            return math.ceil(W * f / (x * (1 - R2) * H))

        # Calculation process
        K1 = calculate_k1(L, C_L, R1)
        K2 = calculate_k2(W, f, x, R2, H)
        # Multiplying by 5 might be for backup or other considerations, add comments to explain
        n = 5 * K1 * K2

        # Display result
        result_label.config(text=f"Number of photos required n: {n:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

# Create main window
root = tk.Tk()
root.title("Photo Quantity Calculator")

# Create and place labels and entry fields
tk.Label(root, text="Width of the photo area (W) (m):").pack()
entry_W = tk.Entry(root)
entry_W.pack()

tk.Label(root, text="Length of the photo area (L) (m):").pack()
entry_L = tk.Entry(root)
entry_L.pack()

tk.Label(root, text="Coverage width of one photo (C_L) (m):").pack()
entry_CL = tk.Entry(root)
entry_CL.pack()

tk.Label(root, text="Sensor's long side dimension (x) (m):").pack()
entry_x = tk.Entry(root)
entry_x.pack()

tk.Label(root, text="Focal length (f) (m):").pack()
entry_f = tk.Entry(root)
entry_f.pack()

tk.Label(root, text="Flight height (H) (m):").pack()
entry_H = tk.Entry(root)
entry_H.pack()

tk.Label(root, text="Lateral overlap (R1):").pack()
entry_R1 = tk.Entry(root)
entry_R1.pack()

tk.Label(root, text="Longitudinal overlap (R2):").pack()
entry_R2 = tk.Entry(root)
entry_R2.pack()

# Create calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_photos)
calculate_button.pack()

# Create result label
result_label = tk.Label(root, text="")
result_label.pack()

# Run main loop
root.mainloop()