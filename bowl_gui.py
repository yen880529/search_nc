import bowl_calculate
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
def bowl_gui_all():
    def copy_to_clipboard():
        root.clipboard_clear()
        root.clipboard_append(code_text.get(1.0, tk.END))
        root.update()  # Keeps the clipboard updated

    def calculate_all():
        try:
            # Get input values and validate
            A = 3
            B = (float(entry_B.get())/2)-1
            C = B + 1
            D = float(entry_D.get())
            E = float(entry_E.get())
            F = float(entry_F.get())
            G = float(entry_G.get())
            H = C + (G / 2)
            I = float(entry_I.get())
            J = C + I
            K = float(entry_K.get())
            L = (K / 2) + I
            M = float(entry_M.get())
            N = (float(entry_N.get()))+10

            reserved = 1
            blade_radius = 0.8

            oil_R1_Z_1,oil_R1_X_1 , oil_R2_Z_1,oil_R2_X_1 ,\
                oil_R3_Z_1,oil_R3_X_1 , oil_R4_Z_1,oil_R4_X_1 ,\
                oil_R1_Z_03,oil_R1_X_03 , oil_R2_Z_03,oil_R2_X_03 ,\
                oil_R3_Z_03,oil_R3_X_03 , oil_R4_Z_03,oil_R4_X_03 , \
                oil_R1_Z_0,oil_R1_X_0 , oil_R2_Z_0,oil_R2_X_0 , \
                oil_R3_Z_0,oil_R3_X_0 , oil_R4_Z_0,oil_R4_X_0\
                =bowl_calculate.calculate_all_1(A, B, C, D, E, reserved, blade_radius)

            oil_R5_Z_1, oil_R5_X_1, oil_R6_Z_1, oil_R6_X_1,\
                oil_R7_Z_1, oil_R7_X_1, oil_R8_Z_1, oil_R8_X_1,\
                oil_R5_Z_03, oil_R5_X_03, oil_R6_Z_03, oil_R6_X_03,\
                oil_R7_Z_03, oil_R7_X_03, oil_R8_Z_03, oil_R8_X_03, \
                oil_R5_Z_0, oil_R5_X_0, oil_R6_Z_0, oil_R6_X_0,\
                oil_R7_Z_0, oil_R7_X_0, oil_R8_Z_0, oil_R8_X_0\
                =bowl_calculate.calculate_all_2(A, B, C, D, F, reserved, blade_radius)

            starting_point_X_25,starting_point_X_10,starting_point_X_03,starting_point_X_01,starting_point_X_00,starting_point_Y,\
                R2_X_25,R2_X_10,R2_X_03,R2_X_01,R2_X_00,\
                R2_Y_25,R2_Y_10,R2_Y_03,R2_Y_01,R2_Y_00,\
                rough_X_25,rough_X_10,rough_X_03,rough_finish_Y,\
                R3_X_01,R3_X_00,R3_Y_01,R3_Y_00,\
                R4_Y_01,R4_Y_00,finish_point_X,\
                ARC_25,ARC_10,ARC_03,ARC_01,ARC_00\
                =bowl_calculate.calculate_all_3(A , B , D, C , G , H , I , J, K , L , blade_radius)
            
            cnc_code = f"""
    N103 
    G50S400
    G00T0707M42G18
    G96S100M03 
    G00{starting_point_Y:.2f}Z5.
    G01Z2.5F1.
    G2X{R2_Y_25:.2f}Z{R2_X_25:.2f}R{G+2.5+ blade_radius:.2f}F0.2 
    G3X{rough_finish_Y:.2f}Z{rough_X_25:.2f}R{ARC_25}
    G00Z5.
    X{starting_point_Y:.2f}
    G1Z1.F0.25 
    G2X{R2_Y_10:.2f}Z{R2_X_10:.2f}R{G+1+ blade_radius:.2f}
    G3X{rough_finish_Y:.2f}Z{rough_X_10:.2f}R{ARC_10}
    G00Z5.
    X{starting_point_Y:.2f}
    G1Z0.3F0.25
    G2X{R2_Y_03:.2f}Z{R2_X_03:.2f}R{G+0.3+ blade_radius:.2f}
    G3X{rough_finish_Y:.2f}Z{rough_X_03:.2f}R{ARC_03}
    G00U-0.5Z10.M09
    X250.Z400. 
    T0900M05 
    M01
    T1100
    M01


    #N104#

    N105
    G50S400
    G00T0707M42G18
    G96S160M03 
    G00X{oil_R1_X_1:.2f}Z30.M08
    G1Z-{oil_R1_Z_1:.2f}F1. 
    G02X{oil_R2_X_1:.2f}Z-{oil_R2_Z_1:.2f}R4.8F0.15 
    G03X{oil_R3_X_1:.2f}Z-{oil_R3_Z_1:.2f}R1.2
    G02X{oil_R4_X_1:.2f}Z-{oil_R4_Z_1:.2f}R4.8
    G0Z5.
    X{oil_R1_X_03:.2f}
    G01Z-{oil_R1_Z_03:.2f}F1.
    G02X{oil_R2_X_03:.2f}Z-{oil_R2_Z_03:.2f}R4.1F0.15 
    G03X{oil_R3_X_03:.2f}Z-{oil_R3_Z_03:.2f}R1.9 
    G02X{oil_R4_X_03:.2f}Z-{oil_R4_Z_03:.2f}R4.1
    G0Z5.
    X{oil_R5_X_1:.2f}
    G01Z-{oil_R5_Z_1:.2f}F1. 
    G02X{oil_R6_X_1:.2f}Z-{oil_R6_Z_1:.2f}R4.8F0.15 
    G03X{oil_R7_X_1:.2f}Z-{oil_R7_Z_1:.2f}R1.2
    G02X{oil_R8_X_1:.2f}Z-{oil_R8_Z_1:.2f}R4.8
    G0Z5.
    X{oil_R5_X_03:.2f}
    G01Z-{oil_R5_Z_03:.2f}F1.
    G02X{oil_R6_X_03:.2f}Z-{oil_R6_Z_03:.2f}R4.1F0.15 
    G03X{oil_R7_X_03:.2f}Z-{oil_R7_Z_03:.2f}R1.9
    G02X{oil_R8_X_03:.2f}Z-{oil_R8_Z_03:.2f}R4.1
    G0Z5.
    X{oil_R1_X_0:.2f}
    G01Z-{oil_R1_Z_0:.2f}F1.
    G02X{oil_R2_X_0:.2f}Z-{oil_R2_Z_0:.2f}R3.8F0.15 
    G03X{oil_R3_X_0:.2f}Z-{oil_R3_Z_0:.2f}R2.2
    G02X{oil_R4_X_0:.2f}Z-{oil_R4_Z_0:.2f}R3.8
    G0Z5.
    X{oil_R5_X_0:.2f}
    G01Z-{oil_R5_Z_0:.2f}
    G02X{oil_R6_X_0:.2f}Z-{oil_R6_Z_0:.2f}R3.8F0.15 
    G03X{oil_R7_X_0:.2f}Z-{oil_R7_Z_0:.2f}R2.2
    G02X{oil_R8_X_0:.2f}Z-{oil_R8_Z_0:.2f}R3.8
    G00Z10.
    X{starting_point_Y:.2f}
    G01Z3.F0.5 
    G1Z0.1F0.25
    G2X{R2_Y_01:.2f}Z{R2_X_01:.2f}R{G+0.1+ blade_radius:.2f}F0.15 
    G3X{R3_Y_01:.2f}Z{R3_X_01:.2f}R{ARC_01:.2f}
    G2X{R4_Y_01:.2f}Z{finish_point_X:.2f}R{I+0.1+ blade_radius:.2f}
    G01Z{D-C-M+0.1:.2f}
    X20.
    G00U-0.5Z5.
    X{starting_point_Y:.2f}
    G01Z3.F0.5 
    G1Z0.F0.25
    G2X{R2_Y_00:.2f}Z{R2_X_00:.2f}R{G+ blade_radius:.2f}F0.15 
    G3X{R3_Y_00:.2f}Z{R3_X_00:.2f}R{ARC_00:.2f}
    G2X{R4_Y_00:.2f}Z{finish_point_X:.2f}R{I+blade_radius:.2f}
    G01Z{D-C-M:.2f}
    X20.
    G00U-0.5Z5.M09 
    X300.Z450. 
    T0700M05 
    M01

    N106 
    G50S400
    G00T0707M42G18
    G96S160M03 
    G00X{N:.2f}Z30.M08
    G00Z5.
    G01Z0.F1.
    X{starting_point_Y:.2f}F0.25
    G2X{R2_Y_00:.2f}Z{R2_X_00:.2f}R{G+ blade_radius:.2f}F0.15 
    G3X{R3_Y_00:.2f}Z{R3_X_00:.2f}R{ARC_00:.2f}
    G2X{R4_Y_00:.2f}Z{finish_point_X:.2f}R{I+blade_radius:.2f}
    G01Z{D-C-M:.2f}
    G00U-0.5Z5.
    X350.Z450. 
    T0700M05 
    M00












            """

            code_text.delete(1.0, tk.END)
            code_text.insert(tk.END, cnc_code)

            messagebox.showinfo("成功", "計算完成！")

        except ValueError:
            messagebox.showerror("錯誤", "請輸入有效的數字！")

    # GUI
    root = tk.Tk()
    root.title("球碗油溝")

    # Define labels and entry fields
    tk.Label(root, text="球碗直徑:").grid(row=1, column=0, pady=5, sticky='s')
    entry_B = tk.Entry(root, width=10)
    entry_B.grid(row=1, column=1, pady=5, sticky='w')

    tk.Label(root, text="球碗圓心:").grid(row=2, column=0, pady=5, sticky='s')
    entry_D = tk.Entry(root, width=10)
    entry_D.grid(row=2, column=1, pady=5, sticky='w')

    tk.Label(root, text="第一油溝深度:").grid(row=3, column=0, pady=5, sticky='s')
    entry_E = tk.Entry(root, width=10)
    entry_E.grid(row=3, column=1, pady=5, sticky='w')

    tk.Label(root, text="第二油溝深度:").grid(row=4, column=0, pady=5, sticky='s')
    entry_F = tk.Entry(root, width=10)
    entry_F.grid(row=4, column=1, pady=5, sticky='w')

    tk.Label(root, text="球碗平面R角:").grid(row=5, column=0, pady=5, sticky='s')
    entry_G = tk.Entry(root, width=10)
    entry_G.grid(row=5, column=1, pady=5, sticky='w')

    tk.Label(root, text="球碗底部R角:").grid(row=6, column=0, pady=5, sticky='s')
    entry_I = tk.Entry(root, width=10)
    entry_I.grid(row=6, column=1, pady=5, sticky='w')

    tk.Label(root, text="吊掛孔面直徑:").grid(row=7, column=0, pady=5, sticky='s')
    entry_K = tk.Entry(root, width=10)
    entry_K.grid(row=7, column=1, pady=5, sticky='w')

    tk.Label(root, text="吊掛孔面深度:").grid(row=8, column=0, pady=5, sticky='s')
    entry_M = tk.Entry(root, width=10)
    entry_M.grid(row=8, column=1, pady=5, sticky='w')

    tk.Label(root, text="球碗外徑:").grid(row=9, column=0, pady=5, sticky='s')
    entry_N = tk.Entry(root, width=10)
    entry_N.grid(row=9, column=1, pady=5, sticky='w')  

    copy_button = tk.Button(root, text="複製", command=copy_to_clipboard, width=10)
    copy_button.grid(row=10, column=1, pady=5, sticky='w')

    code_text = tk.Text(root, height=21, width=45)
    code_text.grid(row=0, column=2, columnspan=1, rowspan=11, padx=20, pady=5, sticky='s')

    # Calculation button
    calculate_button = tk.Button(root, text="計算", command=calculate_all, width=10)
    calculate_button.grid(row=10, column=0, pady=5)

    #root.mainloop()
