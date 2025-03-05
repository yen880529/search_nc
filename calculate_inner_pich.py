import math
import tkinter as tk
import tkinter as ttk
def calculate_gui():
    def calculate():
        # 讀取用戶輸入的值
        pich = float(pich_entry.get())
        spacing = float(spacing_entry.get())
        diameter = float(diameter_entry.get())
        angle = float(angle_entry.get())
        lathe_tool = float(lathe_tool_entry.get())
        times_mm = float(times_mm_entry.get())
        reserve = float(reserve_entry.get())+lathe_tool
        chamfer_r = float(chamfer_r_entry.get())
        share_times = float(share_times_entry.get())
        program_number = float(program_number_entry.get())
        start_mm = -float(start_mm_entry.get())
        length_mm = float(length_mm_entry.get()) + abs(start_mm) + 5


        finish = round(diameter + (((pich - spacing) / 2) / math.tan(math.radians(angle / 2)) - reserve) * 2, 2) #牙底
        total = finish - diameter  #總加工深度
        times = total // times_mm #趟數

        chamfer_times_mm = 0.02
        chamfer_times = ((reserve + chamfer_r)/2)//chamfer_times_mm


        text_box_1.delete(1.0, tk.END)  # 清空文本框內容
        text_box_2.delete(1.0, tk.END)  # 清空文本框內容

        n = spacing/2
        w = round((finish - diameter) / 2) * math.tan(math.radians(angle / 2))
        finish_w = round((((finish - diameter) / 2) * math.tan(math.radians(angle / 2))) + (((reserve + chamfer_r))) * math.tan(math.radians(angle / 2)))
        while w + n > finish_w :
            x = round(diameter - (reserve-lathe_tool),3)
            w = round(((finish - diameter) / 2) * math.tan(math.radians(angle / 2)) + n,3)
            if  reserve == lathe_tool :
                x = f"{x:.1f}"
                text_box_1.insert(tk.END, f"X{x}W{w}\n")
                text_box_1.insert(tk.END, f"M98P{int(program_number)}\n")
            n -= 0.05  


        n = 0
        while n < chamfer_times :
            x = round(diameter + ((n * chamfer_times_mm)*2) - (reserve-lathe_tool),3)
            w = round((((finish - diameter) / 2) * math.tan(math.radians(angle / 2))) + (((reserve + chamfer_r))) * math.tan(math.radians(angle / 2))-(math.sqrt((reserve + chamfer_r)**2 - ((reserve + chamfer_r) - (n * chamfer_times_mm))**2)), 3) 
            if  reserve == lathe_tool :
                x = f"{x:.1f}"
                text_box_1.insert(tk.END, f"X{x}W{w}\n")
                text_box_1.insert(tk.END, f"M98P{int(program_number)}\n")
            n += 1    

        n = spacing/2
        w = round((finish - diameter) / 2) * math.tan(math.radians(angle / 2))
        finish_w = round((((finish - diameter) / 2) * math.tan(math.radians(angle / 2))) + (((reserve + chamfer_r))) * math.tan(math.radians(angle / 2)))
        while w + n > finish_w :
            x = round(diameter - (reserve-lathe_tool),3)
            w = round(((finish - diameter) / 2) * math.tan(math.radians(angle / 2)) + n,3)
            if  reserve == lathe_tool :
                x = f"{x:.1f}"
                text_box_1.insert(tk.END, f"X{x}W-{w}\n")
                text_box_1.insert(tk.END, f"M98P{int(program_number)}\n")
            n -= 0.05  


        n = 0
        while n < chamfer_times :
            x = round(diameter + ((n * chamfer_times_mm)*2) - (reserve-lathe_tool),3)
            w = round((((finish - diameter) / 2) * math.tan(math.radians(angle / 2))) + (((reserve + chamfer_r))) * math.tan(math.radians(angle / 2))-(math.sqrt((reserve + chamfer_r)**2 - ((reserve + chamfer_r) - (n * chamfer_times_mm))**2)), 3) 
            if  reserve == lathe_tool :
                x = f"{x:.1f}"
                text_box_1.insert(tk.END, f"X{x}W-{w}\n")
                text_box_1.insert(tk.END, f"M98P{int(program_number)}\n")
            n += 1    





        n = 0
        while ((diameter - (reserve - lathe_tool)) + (times_mm * (n))) < (finish - (times_mm * (share_times))) :

            x = round(((diameter - (reserve - lathe_tool)) + (times_mm * (n))), 3)
            w = round(((finish - x) / 2) * math.tan(math.radians(angle / 2)), 3)
            if x.is_integer():
                x = f"{x:.1f}"
            text_box_1.insert(tk.END, f"X{x}W{w}\n")
            text_box_1.insert(tk.END, f"M98P{int(program_number)}\n")
            n += 1

        n = 0
        while ((diameter - (reserve - lathe_tool)) + (times_mm * (n))) < (finish - (times_mm * (share_times))) :
            x = round(((diameter - (reserve - lathe_tool)) + (times_mm * (n))), 3)
            w = round(((finish - x) / 2) * math.tan(math.radians(angle / 2)), 3)
            if x.is_integer():
                x = f"{x:.1f}"
            text_box_1.insert(tk.END, f"X{x}W-{w}\n")
            text_box_1.insert(tk.END, f"M98P{int(program_number)}\n")
            n += 1

        n = share_times
        while n > 0:
            x = round((finish - (times_mm * (n))), 3)
            w = round(((finish - x) / 2) * math.tan(math.radians(angle / 2)), 3)
            if x.is_integer():
                x = f"{x:.1f}"
            text_box_1.insert(tk.END, f"X{x}W{w}\n")
            text_box_1.insert(tk.END, f"M98P{int(program_number)}\n")
            if w > 2.5 :
                text_box_1.insert(tk.END, f"X{x}W{w/2}\n")
                text_box_1.insert(tk.END, f"M98P{int(program_number)}\n")
            if w > 1 :    
                text_box_1.insert(tk.END, f"X{x}W{0}\n")
                text_box_1.insert(tk.END, f"M98P{int(program_number)}\n")
            if w > 2.5 :
                text_box_1.insert(tk.END, f"X{x}W-{w/2}\n")
                text_box_1.insert(tk.END, f"M98P{int(program_number)}\n")
            text_box_1.insert(tk.END, f"X{x}W-{w}\n")
            text_box_1.insert(tk.END, f"M98P{int(program_number)}\n")
            n -= 1

        text_box_1.insert(tk.END, f"X{finish}W{0}\n")
        text_box_1.insert(tk.END, f"M98P{int(program_number)}\n")

##############副程式#############        

        text_box_2.insert(tk.END, f"O{int(program_number)}\n")
        text_box_2.insert(tk.END, f"G32Z-{int(length_mm)}.F{int(pich)}.\n")
        text_box_2.insert(tk.END, f"G00X{int(diameter-10)}.\n")
        text_box_2.insert(tk.END, f"Z{int(start_mm) + 5}.\n")
        text_box_2.insert(tk.END, f"M99\n")
        text_box_2.insert(tk.END, f"%\n")
        

    #複製主程式
    def copy_to_clipboard_1():
            root.clipboard_clear()
            root.clipboard_append(text_box_1.get(1.0, tk.END))
            root.update()

    #複製副程式
    def copy_to_clipboard_2():
            root.clipboard_clear()
            root.clipboard_append(text_box_2.get(1.0, tk.END))
            root.update()


    # 創建主窗口
    root = tk.Tk()
    root.title("衝桿螺母車牙計算")

    # 調整界面佈局
    for i in range(10):
        root.grid_rowconfigure(i, pad=2)
    root.grid_columnconfigure(0, pad=2)

    tk.Label(root, text="牙距").grid(row=0, column=0, padx=4, pady=4)
    pich_entry = tk.Entry(root, width=10)
    pich_entry.insert(0, "14")  # 預設值
    pich_entry.grid(row=0, column=1, padx=2)

    tk.Label(root, text="齒頂寬").grid(row=1, column=0, padx=4, pady=4)
    spacing_entry = tk.Entry(root, width=10)
    spacing_entry.insert(0, "3.5")
    spacing_entry.grid(row=1, column=1, padx=2)

    tk.Label(root, text="內徑").grid(row=2, column=0, padx=4, pady=4)
    diameter_entry = tk.Entry(root, width=10)
    diameter_entry.insert(0, "344.845")
    diameter_entry.grid(row=2, column=1, padx=2)

    tk.Label(root, text="牙角度").grid(row=3, column=0, padx=4, pady=4)
    angle_entry = tk.Entry(root, width=10)
    angle_entry.insert(0, "60")
    angle_entry.grid(row=3, column=1, padx=2)

    tk.Label(root, text="車刀R角").grid(row=4, column=0, padx=4, pady=4)
    lathe_tool_entry = tk.Entry(root, width=10)
    lathe_tool_entry.insert(0, "0.8")
    lathe_tool_entry.grid(row=4, column=1, padx=2)

    tk.Label(root, text="每次加工深度").grid(row=5, column=0, padx=4, pady=4)
    times_mm_entry = tk.Entry(root, width=10)
    times_mm_entry.insert(0, "0.15")
    times_mm_entry.grid(row=5, column=1, padx=2)

    tk.Label(root, text="預留量").grid(row=6, column=0, padx=4, pady=4)
    reserve_entry = tk.Entry(root, width=10)
    reserve_entry.insert(0, "0.2")
    reserve_entry.grid(row=6, column=1, padx=2)

    tk.Label(root, text="牙圓角").grid(row=7, column=0, padx=4, pady=4)
    chamfer_r_entry = tk.Entry(root, width=10)
    chamfer_r_entry.insert(0, "0.3")
    chamfer_r_entry.grid(row=7, column=1, padx=2)

    tk.Label(root, text="牙底分刀趟數").grid(row=8, column=0, padx=4, pady=4)
    share_times_entry = tk.Entry(root, width=10)
    share_times_entry.insert(0, "5")
    share_times_entry.grid(row=8, column=1, padx=2)

    tk.Label(root, text="牙起點").grid(row=9, column=0, padx=4, pady=4)
    start_mm_entry = tk.Entry(root, width=10)
    start_mm_entry.insert(0, "0")
    start_mm_entry.grid(row=9, column=1, padx=2)

    tk.Label(root, text="牙終點").grid(row=10, column=0, padx=4, pady=4)
    length_mm_entry = tk.Entry(root, width=10)
    length_mm_entry.insert(0, "430")
    length_mm_entry.grid(row=10, column=1, padx=2)

    tk.Label(root, text="副程式檔號").grid(row=11, column=0, padx=4, pady=4)
    program_number_entry = tk.Entry(root, width=10)
    program_number_entry.insert(0, "9999")
    program_number_entry.grid(row=11, column=1, padx=2)

    # 文本框(主程式)
    text_box_1 = tk.Text(root, height=20, width=35)
    text_box_1.grid(row=0,rowspan = 9 , column=2, columnspan=4, padx=4, pady=4)

    # 文本框(副程式)
    text_box_2 = tk.Text(root, height=6, width=35)
    text_box_2.grid(row=8,rowspan = 3, column=2, columnspan=4, padx=4, pady=4)

    # 計算按鈕
    button = ttk.Button(root, text="計算", command=calculate, width=10, relief= "groove")
    button.grid(row=11, column=2, columnspan=1, padx=4, pady=4)

    # 複製按鈕
    copy_button = ttk.Button(root, text="複製(主程式)", command=copy_to_clipboard_1, width=10 , relief= "groove")
    copy_button.grid(row=11, column=3, columnspan=1, padx=4, pady=4)

    # 複製按鈕
    copy_button = ttk.Button(root, text="複製(副程式)", command=copy_to_clipboard_2, width=10, relief= "groove")
    copy_button.grid(row=11, column=4, columnspan=1, padx=4, pady=4)

    # 啟動主循環
    root.mainloop()
    
#calculate_gui()