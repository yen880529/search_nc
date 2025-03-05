import re
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import rcParams

# 全域變數
xw_gui = None
keep_plot = None
ax = None
canvas = None
total_points = 0  # 累計點數

def parse_and_plot():
    global total_points

    #字體設定
    style = ttk.Style()

    # 設置錯誤標籤的字體顏色為紅色
    style.configure("Error.TLabel", foreground="red")

    # 設置正常標籤的字體顏色為黑色
    style.configure("Normal.TLabel", foreground="black")

    # 設置成功標籤的字體顏色為綠色
    style.configure("Success.TLabel", foreground="green")

    # 獲取主程式
    data = text_input.get("1.0", tk.END).strip()

    # 檢查 X 座標
    x_match = re.search(r'X([\d.]+)', data)
    if x_match:
        x_value = float(x_match.group(1))
    else:
        status_label.config(style="Error.TLabel", text="⚠️ 找不到 X 值，請檢查主程式！")
        return

    # 檢查 W 座標
    w_match = re.search(r'W([-?\d.]+)', data)
    if w_match:
        w_value = float(w_match.group(1))
    else:
        status_label.config(style="Error.TLabel", text="⚠️ 找不到 W 值，請檢查主程式！")
        return

    # 驗證 X 和 W 的格式
    pattern = r"X([\d.]+)W([-\d.]+)"
    matches = re.findall(pattern, data)
    if not matches:
        status_label.config(style="Error.TLabel", text="⚠️ 主程式有誤(格式不符)")
        return

    # 獲取副程式
    cnc_code = subroutine_input.get("1.0", "end-1c")

    # 檢查 Z 值
    z_value_match = re.search(r'Z-?(\d+)', cnc_code)
    if z_value_match:
        z_value = float(z_value_match.group(1))
    else:
        status_label.config(style="Error.TLabel", text="⚠️ 找不到 Z 值，請檢查副程式！")
        return

    # 檢查 F 值
    f_value_match = re.search(r'F(\d+)', cnc_code)
    if f_value_match:
        f_value = float(f_value_match.group(1))
    else:
        status_label.config(style="Error.TLabel", text="⚠️ 找不到 F 值，請檢查副程式！")
        return


    # rpm輸入驗證
    try:
        rpm_input = rpm_entry.get().strip()
        if not rpm_input:
            status_label.config(text="❌ 請輸入轉速 (RPM)！", foreground="red")
            return
        
        # 驗證是否為正數
        rpm = float(rpm_input)
        if rpm <= 0:
            status_label.config(text="⚠️ 轉速必須為正數！", foreground="red")
            return

    except ValueError:
        status_label.config(text="⛔ 轉速 (RPM) 必須是數字！", foreground="red")
        return

    try:
        # 轉換數據 (X -> Y, W -> X) (由於是車床，座標位置需轉換)
        coordinates = [(float(w), float(x)) for x, w in matches]
        
        # 獲取第一行的 X 值作為 Y 軸的原點
        y_axis_origin = float(matches[0][0])  # 第一行的 X 值
        
        # 分離 X 和 Y
        x_values = [coord[0] for coord in coordinates]  # 原 W，現在是 X
        y_values = [coord[1] for coord in coordinates]  # 原 X，保持原始值
        
        # 如果未勾選 "保留圖表"，則清除舊的圖表並重置點數量
        if not keep_plot.get():
            ax.clear()
            total_points = 0  # 重置點數

        # 更新累計點數
        total_points += len(coordinates)
        points_count_label.config(text=f"座標點的數量：{total_points}")

        # 更新加工工時
        if z_value is not None and f_value is not None:
            processing_time = (total_points * z_value) / (rpm * f_value)
            processing_time_label.config(text=f"加工工時：約{processing_time:.0f} 分鐘")


        # 設置 Matplotlib 字體為支持中文的字體
        rcParams['font.family'] = ['Microsoft JhengHei']
        rcParams['axes.unicode_minus'] = False  # 確保負號顯示正常

        # 繪製圖表
        ax.scatter(x_values, y_values, s=10, label=f"數據組 {len(ax.collections) + 1}")
        ax.axhline(y_axis_origin, color="gray", linestyle="--", linewidth=0.8)  # Y 軸原點基線
        ax.axvline(0, color="gray", linestyle="--", linewidth=0.8)  # X = 0 基線
        ax.set_aspect('equal', adjustable='datalim')
        ax.set_xlabel("W")
        ax.set_ylabel("X")
        ax.legend()
        ax.grid(True)

        # 調整 Y 軸刻度標籤，使原點顯示第一行的 X 值
        yticks = ax.get_yticks()
        ytick_labels = [f"{tick:.1f}" for tick in yticks]
        ytick_labels = [str(int(y_axis_origin)) if abs(tick - y_axis_origin) < 1e-5 else label 
                        for tick, label in zip(yticks, ytick_labels)]
        ax.set_yticks(yticks)
        ax.set_yticklabels(ytick_labels)

        # 更新圖表
        canvas.draw()
        
        status_label.config(style="Success.TLabel", text="圖表已成功繪製！", foreground="green")
    
    except ValueError as e:
        status_label.config(text=f"數據解析錯誤：{e}", fg="red")

def main_gui(root):
    global  xw_gui, control_frame, text_input, subroutine_input, rpm_entry, parse_button, keep_plot, ax, canvas, status_label, points_count_label, processing_time_label
    # 創建主窗口
    xw_gui = tk.Toplevel(root)
    xw_gui.title("車牙座標解析")

    # 使用 grid 佈局
    xw_gui.grid_rowconfigure(0, weight=1)
    xw_gui.grid_columnconfigure(0, weight=3)
    xw_gui.grid_columnconfigure(1, weight=5)

    # 左側控制面板
    control_frame = ttk.Frame(xw_gui)
    control_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    control_frame.grid_columnconfigure(1, weight=1)

    # 創建文本框輸入區域
    text_input_label = ttk.Label(control_frame, text="主程式：", font=("Microsoft JhengHei", 10))
    text_input_label.grid(row=0, column=0,  pady=5, sticky="w")
    text_input = scrolledtext.ScrolledText(control_frame, width=40, height=10, font=("Microsoft JhengHei", 10))
    text_input.grid(row=1, column=0,  sticky="nsew", pady=5)

    # 創建副程式輸入框
    subroutine_label = ttk.Label(control_frame, text="副程式：", font=("Microsoft JhengHei", 10))
    subroutine_label.grid(row=2, column=0,  pady=5, sticky="w")
    subroutine_input = scrolledtext.ScrolledText(control_frame, width=40, height=6, font=("Microsoft JhengHei", 10))
    subroutine_input.grid(row=3, column=0,  sticky="nsew", pady=5)

    # 轉速輸入框及標籤
    label = ttk.Label(control_frame, text="請輸入轉速(RPM)：", font=("Microsoft JhengHei", 10))
    label.grid(row=4, column=0,  pady=5, sticky="w")
    style = ttk.Style()
    style.configure("Custom.TEntry", padding=5, relief="groove", borderwidth=3)
    rpm_entry = ttk.Entry(control_frame, style="Custom.TEntry", font=("Microsoft JhengHei", 10))
    rpm_entry.grid(row=5, column=0, sticky="ew", pady=5)

    # 創建解析按鈕
    parse_button = ttk.Button(control_frame, text="解析座標", command=parse_and_plot)
    parse_button.grid(row=6, column=0,  pady=5)

    # 保留圖表選項
    keep_plot = tk.BooleanVar()
    keep_plot_checkbox = ttk.Checkbutton(control_frame, text="保留圖表", variable=keep_plot)
    keep_plot_checkbox.grid(row=7, column=0,  pady=5)

    # 右側圖表顯示區域
    plot_frame = ttk.Frame(xw_gui)
    plot_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
    plot_frame.grid_rowconfigure(0, weight=1)
    plot_frame.grid_columnconfigure(0, weight=1)

    # 初始化圖表
    fig, ax = plt.subplots(figsize=(5, 3), dpi=100)
    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=0, column=0, sticky="nsew")

    # 狀態欄
    status_label = ttk.Label(plot_frame, text="等待輸入 CNC 碼...", relief=tk.SUNKEN, anchor="w")
    status_label.grid(row=1, column=0, sticky="ew", pady=5)

    # 座標點數量標籤
    points_count_label = ttk.Label(plot_frame, text="座標點的數量：0", relief=tk.SUNKEN, anchor="w")
    points_count_label.grid(row=2, column=0,  sticky="ew", pady=5)

    # 加工工時標籤
    processing_time_label = ttk.Label(plot_frame, text="加工工時：0", relief=tk.SUNKEN, anchor="w")
    processing_time_label.grid(row=3, column=0,  sticky="ew", pady=5)

    def on_closing():
        if canvas:
            canvas.get_tk_widget().destroy()  # 清除 Tkinter 中的畫布
            plt.close(fig)  # 關閉 Matplotlib 圖形
        xw_gui.quit()  # 停止 Tkinter 主循環
        xw_gui.destroy()  # 關閉窗口

    # 監聽窗口關閉事件
    xw_gui.protocol("WM_DELETE_WINDOW", on_closing)

