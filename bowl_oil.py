import tkinter as tk
import math
import numpy as np  # 添加 numpy 庫
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
def bowl_oil_all():
    def on_focus_in(event):
        if entry_B.get() == "端面至圓心":
            entry_B.delete(0, tk.END)  # 清除浮水印
            entry_B.config(fg='black')  # 灰色

    def on_focus_out(event):
        if entry_B.get() == "":
            entry_B.insert(0, "端面至圓心")  # 若文本框是空的會重新顯示浮水印
            entry_B.config(fg='gray')  # 灰色

    def calculate_1():
        try:
            A = float(entry_A.get())  # Y起始點（油溝圓半徑）
            B = float(entry_B.get())  # Z（球碗圓心）
            D = int(float(entry_D.get()))  # 圓鼻刀半徑
            D = int(float(entry_D.get()))  # Z（程式起點）
            X = float(entry_X.get())  # 球碗圓直徑
            Y = float(entry_Y.get())  # 油溝出尾

            # 計算球碗圓半徑
            X_radius = X / 2

            # 計算球碗圓心至油溝出尾
            if selected_value.get() == "X":
                Y_radius = B + Y
            elif selected_value.get() == "Y":
                Y_radius = Y

            # 計算油溝和圓面相交點Y
            if Y_radius < -X_radius or Y_radius > X_radius:
                raise ValueError("交點 Y 座標超出油溝圓直徑範圍")
            Y_point = math.sqrt(X_radius**2 - Y_radius**2)
            
            # 計算油溝和圓面相交點X
            if selected_value.get() == "X":
                if Y_point > A:
                    raise ValueError("交點 Y 座標超出油溝圓直徑範圍")
                X_B = math.sqrt(A**2 - Y_point**2) - Y_radius
            elif selected_value.get() == "Y":
                X_B = math.sqrt(A**2 - Y**2) - Y_point

            X_B = round(X_B, 1)  # 將 X_B 四捨五入到小數點後1位

            # 計算球碗圓心和油溝圓心之距離
            distance = abs(X_B)

            # 將結果顯示在 entry_distance 中
            entry_distance.config(state='normal')
            entry_distance.delete(0, tk.END)
            entry_distance.insert(0, str(distance))
            entry_distance.config(state='readonly')

            return A, B, D, distance, X

        except ValueError as e:
            result_label2.config(text=f"輸入錯誤: {str(e)}")
        except Exception as e:
            result_label2.config(text=f"發生錯誤: {str(e)}")

    def clear_plot():
        ax.clear()  # 清空圖表
        canvas.draw()  # 更新畫布以反映更改

    def calculate_2():
        clear_plot()  # 在繪製新圖表之前清空當前圖表
        result_label2.config(text="")  # 清空錯誤信息標籤
        try:
            # 從文本框中獲取值
            A = float(entry_A.get())
            B = float(entry_B.get())
            C = float(entry_C.get())
            D = float(entry_D.get())
            distance = float(entry_distance.get())
            X = float(entry_X.get())
            E = entry_E.get()  # 檔號
            F = entry_F.get()  # 機種
            G = entry_G.get()  # 件號
            H = entry_H.get()  # 圖號
            I = entry_I.get()  # 日期

            # 計算對邊
            Ystart = math.sqrt((A - C)**2 - (B + distance - C - D)**2)

            # 計算角度
            
            angle_A = math.acos((A**2 + distance**2 - (X/2)**2) / (2 * A * distance))
            angle_B = math.acos(((X/2)**2 + distance**2 - A**2) / (2 * (X/2) * distance))
            angle_C = math.acos(((X/2)**2 + A**2 - distance**2) / (2 * (X/2) * A))

            # 弧度轉角度
            A_deg = math.degrees(angle_A)
            B_deg = math.degrees(angle_B)
            C_deg = math.degrees(angle_C)

            oilbottom_Z = math.cos(math.radians(180-B_deg)) * (X/2)
            oilbottom_X = math.sin(math.radians(180-B_deg)) * (X/2)

            


            # 圖表只顯示1/4
            theta = np.linspace(np.pi/2, np.pi, 100)

            # 計算第一個圓的坐標
            x1 = (X/2) * np.cos(theta)
            y1 = (X/2) * np.sin(theta)

            # 計算第二個圓的坐標（考慮X軸偏移）
            x2 = distance + A * np.cos(theta)
            y2 = A * np.sin(theta)

            ax.plot(x1, y1, label='bowl')

            # 繪製第二個圓的1/4圓弧
            ax.plot(x2, y2, label='oil')

            x_origin = -B  # 垂直线的 x 位置
            ax.axvline(x=x_origin, color='r', linestyle='--', label='Z0')

            #油溝出尾點
            ax.scatter(-oilbottom_Z, oilbottom_X, color='red', label="oilbotton ")
            #油溝出尾點標籤
            result_label1.config(text=f"油溝終點: (X{oilbottom_X:.2f}, Z{-(oilbottom_Z-B):.2f})")

            # 設置軸的比例相同
            ax.axis('equal')

            # 顯示網格
            ax.grid(True)

            # 添加圖例
            ax.legend()

            # 只顯示左上角的區域
            ax.set_xlim(-X/2, distance+10)
            ax.set_ylim(0, A+10)

            # 自訂X軸標籤
            custom_xticks = [-X/2, -B, 0]  # 自訂X刻度位置
            custom_xticklabels = ['bottom', 'Z0', 'center']  # 對應標籤

            ax.set_xticks(custom_xticks)  # 設置刻度位置
            ax.set_xticklabels(custom_xticklabels)  # 設置刻度標籤

            # 更新畫布
            canvas.draw()

            # 更新 CNC 程式碼
            cnc_code = f"""
    {E}

    ({F})({G})
    ({H})({I})

    G90 G0 G53 B0
    M00
    M00
    G90 G0 G58 X0 Y{Ystart:.2f} W0
    G13 Z30 H101 S1000
    G01 Z{int(D)}. M3 F1000
    G65 P1400 Y0. Z{B + distance} M1 A118. B0.4 C16 I{A} F100
    G65 P1400 Y0. Z{B + distance} M1 A134. B0.5 C14 I{A} F100
    G65 P1400 Y0. Z{B + distance} M1 A148. B0.5 C12 I{A} F100
    G0 Z{int(D)}.

    G68 X0 Y0 I1 R120.
    G0 X0 Y{Ystart:.2f}
    G65 P1400 Y0. Z{B + distance} M1 A118. B0.4 C16 I{A} F100
    G65 P1400 Y0. Z{B + distance} M1 A134. B0.5 C14 I{A} F100
    G65 P1400 Y0. Z{B + distance} M1 A148. B0.5 C12 I{A} F100
    G0 Z{int(D)}.

    G68 X0 Y0 I1 R240.
    G0 X0 Y{Ystart:.2f}
    G65 P1400 Y0. Z{B + distance} M1 A118. B0.4 C16 I{A} F100
    G65 P1400 Y0. Z{B + distance} M1 A134. B0.5 C14 I{A} F100
    G65 P1400 Y0. Z{B + distance} M1 A148. B0.5 C12 I{A} F100
    G00 Z100. M05
    G91 G28 Z0 W0
    M11
    G90 G00 G53 B180
    M00
    M00
    %
    """
            #顯示 CNC 程式碼
            code_text.delete(1.0, tk.END)
            code_text.insert(tk.END, cnc_code)
        except ValueError:
            result_label2.config(text="請輸入有效的數值！")
        except Exception as e:
            result_label2.config(text=f"發生錯誤：{e}")
            code_text.delete(1.0, tk.END)

    def copy_to_clipboard():
        root.clipboard_clear()
        root.clipboard_append(code_text.get(1.0, tk.END))
        root.update()

    def toggle_entries():
        if checkbox_var.get():
            entry_Y.config(state='normal') 
            entry_distance.config(state='readonly')
        else:
            entry_Y.config(state='disabled') 
            entry_distance.config(state='normal')

    root = tk.Tk()
    root.title("球碗油溝計算")

    # 勾選框
    checkbox_var = tk.IntVar()
    checkbox = tk.Checkbutton(root, text="計算圓心距", variable=checkbox_var, command=toggle_entries)
    checkbox.grid(row=0, column=0, pady=5, sticky='S')

    # 選項按鈕
    selected_value = tk.StringVar(value="Y")
    tk.Radiobutton(root, text="油溝終點Z", variable=selected_value, value="X").grid(row=0, column=1, pady=5, sticky='w')
    tk.Radiobutton(root, text="油溝終點X", variable=selected_value, value="Y").grid(row=1, column=1, pady=5, sticky='w')

    # 計算按鈕1
    calculate_1_button = tk.Button(root, text="計算圓心距", command=calculate_1, width=10)
    calculate_1_button.grid(row=1, column=0, pady=5, sticky='S')

    # 球碗油溝的數值輸入
    #tk.Label(root, text="球碗油溝的數值輸入:").grid(row=2, column=0, columnspan=2, pady=5, sticky='w')

    # A (Y起始點)
    tk.Label(root, text="油溝半徑:").grid(row=3, column=0, pady=5, sticky='s')
    entry_A = tk.Entry(root, width=10)
    entry_A.grid(row=3, column=1, pady=5,sticky='W')

    # X (球碗圓直徑)
    tk.Label(root, text="球碗圓直徑:").grid(row=4, column=0, pady=5, sticky='s')
    entry_X = tk.Entry(root, width=10)
    entry_X.grid(row=4, column=1, pady=5,sticky='W')

    # B (球碗圓心)
    tk.Label(root, text="球碗圓心:").grid(row=5, column=0, pady=5, sticky='s')
    entry_B = tk.Entry(root, width=10)
    entry_B.grid(row=5, column=1, pady=5,sticky='W')
    entry_B.insert(0, "端面至圓心")  # 設定浮水印文字(要跟上面的連結同樣的內容)
    entry_B.bind("<FocusIn>", on_focus_in)  # 綁定顯示
    entry_B.bind("<FocusOut>", on_focus_out)  # 綁定消失

    # C (圓鼻刀半徑)
    tk.Label(root, text="圓鼻刀半徑:").grid(row=6, column=0, pady=5, sticky='s')
    entry_C = tk.Entry(root, width=10)
    entry_C.grid(row=6, column=1, pady=5,sticky='W')
    entry_C.insert(0, "5")  # 默認5

    # D (程式起點)
    tk.Label(root, text="程式起點:").grid(row=7, column=0, pady=5, sticky='s')
    entry_D = tk.Entry(root, width=10)
    entry_D.grid(row=7, column=1, pady=5,sticky='W')
    entry_D.insert(0, "5")  # 默認5

    # Y (油溝出尾)
    tk.Label(root, text="油溝終點:").grid(row=8, column=0, pady=5, sticky='s')
    entry_Y = tk.Entry(root, width=10)
    entry_Y.grid(row=8, column=1, pady=5,sticky='W')

    # Z（圓心距）
    tk.Label(root, text="圓心距:").grid(row=9, column=0, pady=5, sticky='s')
    entry_distance = tk.Entry(root, width=10)
    entry_distance.grid(row=9, column=1, pady=5,sticky='W')

    # 其他輸入
    tk.Label(root, text="檔號:").grid(row=10, column=0, pady=5, sticky='s')
    entry_E = tk.Entry(root, width=10)
    entry_E.grid(row=10, column=1, pady=5, sticky='w')

    tk.Label(root, text="機種:").grid(row=11, column=0, pady=5, sticky='s')
    entry_F = tk.Entry(root, width=10)
    entry_F.grid(row=11, column=1, pady=5, sticky='w')

    tk.Label(root, text="件號:").grid(row=12, column=0, pady=5, sticky='s')
    entry_G = tk.Entry(root, width=10)
    entry_G.grid(row=12, column=1, pady=5, sticky='w')

    tk.Label(root, text="圖號:").grid(row=13, column=0, pady=5, sticky='s')
    entry_H = tk.Entry(root, width=10)
    entry_H.grid(row=13, column=1, pady=5, sticky='w')

    tk.Label(root, text="日期:").grid(row=14, column=0, pady=5, sticky='s')
    entry_I = tk.Entry(root, width=10)
    entry_I.grid(row=14, column=1, pady=5, sticky='w')

    # 計算按鈕2
    calculate_2_button = tk.Button(root, text="產出CNC程式", command=calculate_2, width=10)
    calculate_2_button.grid(row=15, column=0, pady=5,sticky='s')

    # 複製按鈕
    copy_button = tk.Button(root, text="複製", command=copy_to_clipboard, width=10)
    copy_button.grid(row=15, column=1, pady=5,sticky='w')

    # CNC程式碼顯示區域
    code_text = tk.Text(root, height=13, width=45)
    code_text.grid(row=9, column=2, columnspan=1,rowspan=6, padx=20,pady=5,sticky='s')

    # 假設你有寬度 600 像素，高度 400 像素，DPI 為 100
    width_in_pixels = 320
    height_in_pixels = 220
    dpi = 100

    # 將像素轉換為英寸
    width_in_inches = width_in_pixels / dpi
    height_in_inches = height_in_pixels / dpi

    # 創建圖表
    fig = Figure(figsize=(width_in_inches, height_in_inches), dpi=dpi)
    ax = fig.add_subplot(111)
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=0, column=2, rowspan=8,padx=20,pady=5,sticky='s')

    # 錯誤信息標籤
    result_label1 = tk.Label(root, text="", fg="red")
    result_label1.grid(row=8, column=2, pady=0)

    # 錯誤信息標籤
    result_label2 = tk.Label(root, text="", fg="red")
    result_label2.grid(row=15, column=2, pady=0)

    toggle_entries()

    return root  # 返回窗口物件


