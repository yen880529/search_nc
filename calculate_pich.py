import math
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import messagebox, simpledialog, font, ttk, Button
def calculate(): # 函數名
    pich = float(pich_entry.get())
    spacing = float(spacing_entry.get())
    diameter = float(diameter_entry.get())
    angle = float(angle_entry.get())
    tool_type = tool_type_var.get()

    if tool_type == "粗車牙刀":
        lathe_tool = 0.8
    elif tool_type == "精車牙刀":
        lathe_tool = 0.4
    elif tool_type.startswith("切槽刀("):
        lathe_tool = 0.8
    elif tool_type == "切槽後粗車":
        lathe_tool = 0.8
    else:
        lathe_tool = 0

    reserve = float(reserve_entry.get())+lathe_tool
    chamfer_r = float(chamfer_r_entry.get())
    program_number = float(program_number_entry.get())
    first_mm = float(first_mm_entry.get())
    length_mm = float(length_mm_entry.get())+5
    finish = round(diameter - (((pich - spacing) / 2) / math.tan(math.radians(angle / 2)) - reserve) * 2, 2) #牙底

    chamfer_times_mm = 0.05
    chamfer_times = ((reserve + chamfer_r)/2)//chamfer_times_mm

    text_box_1.delete(1.0, tk.END)  # 清空文本框內容
    text_box_2.delete(1.0, tk.END)  # 清空文本框內容

    if (reserve > 0.8 and lathe_tool == 0.8) or (reserve == 0.4 and lathe_tool == 0.4):

        def roughing(first_mm , diameter , finish):#牙粗車
            # 初始值
            value = diameter         # 起始值
            decrement = first_mm        # 初始遞減值
            min_decrement = 0.5  # 最小遞減值

            # 儲存結果
            results = [value]
            steps = 0  # 計數器變數

            while value > finish:  # 持續減到最接近 (牙底)
                value -= decrement
                steps += 1  # 增加計數器
                results.append(max(value, 0))   # 防止 value 小於 0，雖然不太可能發生，除非輸入錯誤，用於防止輸入錯誤

                # 更新遞減值 (縮小規律)
                decrement = max(decrement * 0.9, min_decrement)  # 遞減值不能小於 min_decrement
            
            return steps, results  # 返回遞減次數和結果列表
        steps, results = roughing(first_mm , diameter , finish)#steps = 趟數 ， results = 遞減值

        n = 0
        while n < steps :

            x = round(results[n],3)
            w = round(((x - finish) / 2) * math.tan(math.radians(angle / 2)), 3)

            n += 1
            if (reserve != lathe_tool) and ((tool_type == "粗車牙刀") or (tool_type == "切槽後粗車")):
                text_box_1.insert(tk.END, f"X{x}W{w}\n")
                text_box_1.insert(tk.END, f"M98P{int(program_number)}\n")
                if (w > 4) and (tool_type != "切槽後粗車"):
                    text_box_1.insert(tk.END, f"X{x}W{round(w/1.5,3)}\n")
                    text_box_1.insert(tk.END, f"M98P{int(program_number)}\n")
                    text_box_1.insert(tk.END, f"X{x}W{round(w/3,3)}\n")
                    text_box_1.insert(tk.END, f"M98P{int(program_number)}\n")
                if (w > 2.5 and w <= 4) and (tool_type != "切槽後粗車"):
                    text_box_1.insert(tk.END, f"X{x}W{w/2}\n")
                    text_box_1.insert(tk.END, f"M98P{int(program_number)}\n")
                if w > 1 and w <= 2 :
                    text_box_1.insert(tk.END, f"X{x}W{0}\n")
                    text_box_1.insert(tk.END, f"M98P{int(program_number)}\n")
                if w > 1 and w >= 2 and tool_type != "切槽後粗車":
                        text_box_1.insert(tk.END, f"X{x}W{0}\n")
                        text_box_1.insert(tk.END, f"M98P{int(program_number)}\n")
                if (w > 2.5 and w <= 4) and (tool_type != "切槽後粗車"):
                    text_box_1.insert(tk.END, f"X{x}W-{w/2}\n")
                    text_box_1.insert(tk.END, f"M98P{int(program_number)}\n")
                if (w > 4) and (tool_type != "切槽後粗車"):
                    text_box_1.insert(tk.END, f"X{x}W-{round(w/3,3)}\n")
                    text_box_1.insert(tk.END, f"M98P{int(program_number)}\n")
                    text_box_1.insert(tk.END, f"X{x}W-{round(w/1.5,3)}\n")
                    text_box_1.insert(tk.END, f"M98P{int(program_number)}\n")
                text_box_1.insert(tk.END, f"X{x}W-{w}\n")
                text_box_1.insert(tk.END, f"M98P{int(program_number)}\n")
        if (reserve != lathe_tool) and ((tool_type == "粗車牙刀") or (tool_type == "切槽後粗車")):
            text_box_1.insert(tk.END, f"X{finish}W{0}\n")
            text_box_1.insert(tk.END, f"M98P{int(program_number)}\n")

#########切槽刀############

        n = 0    
        if (reserve != lathe_tool) and tool_type.startswith("切槽刀"):
            while (diameter - finish) - n > 0   :
                if "(" in tool_type and "mm)" in tool_type:
                    tool_size = float(tool_type.split("(")[1].replace("mm)", ""))

                x = round(diameter-n,3)
                w = round(((x - finish) / 2) * math.tan(math.radians(angle / 2)), 3)

                if w * 2 < tool_size:   
                    break
                else:
                    n += 0.5

                text_box_1.insert(tk.END, f"X{x}W{-w}\n")
                text_box_1.insert(tk.END, f"M98P{int(program_number)}\n")
                text_box_1.insert(tk.END, f"X{x}W{round(w - tool_size, 3)}\n")
                text_box_1.insert(tk.END, f"M98P{int(program_number)}\n")
                if (w * 2) - tool_size > tool_size :
                    text_box_1.insert(tk.END, f"X{x}W{round((-w + (w - tool_size))/2, 3)}\n")
                    text_box_1.insert(tk.END, f"M98P{int(program_number)}\n")

    #############以下是牙精車############

    #車牙R角
        n = 0
        total_times_mm = 0.09
        w = (pich) / 2
        finish_w = round((((diameter - finish) / 2) * math.tan(math.radians(angle / 2))) + (((reserve + chamfer_r))) * math.tan(math.radians(angle / 2)),3)
        total_times = (w - finish_w)/total_times_mm

        while total_times > n:
            x = round(diameter , 3)
            w = round(((pich) / 2) - (total_times_mm * n),3)
            if  reserve == lathe_tool :
                text_box_1.insert(tk.END, f"X{x}W{w}\n")
                text_box_1.insert(tk.END, f"M98P{int(program_number)}\n")
            n += 1

        n = 0
        while n < chamfer_times :
            x = round(diameter - ((n * chamfer_times_mm)*2),3)
            w = round((((diameter - finish) / 2) * math.tan(math.radians(angle / 2))) + (((reserve + chamfer_r))) * math.tan(math.radians(angle / 2))-(math.sqrt((reserve + chamfer_r)**2 - ((reserve + chamfer_r) - (n * chamfer_times_mm))**2)), 3) 
            if  reserve == lathe_tool :
                text_box_1.insert(tk.END, f"X{x}W{w}\n")
                text_box_1.insert(tk.END, f"M98P{int(program_number)}\n")
            n += 1    


        n = 0
        total_times_mm = 0.09
        w = (pich) / 2
        finish_w = round((((diameter - finish) / 2) * math.tan(math.radians(angle / 2))) + (((reserve + chamfer_r))) * math.tan(math.radians(angle / 2)),3)
        total_times = (w - finish_w)/total_times_mm

        while total_times > n:
            x = round(diameter , 3)
            w = round(((pich) / 2) - (total_times_mm * n),3)
            if  reserve == lathe_tool :
                text_box_1.insert(tk.END, f"X{x}W-{w}\n")
                text_box_1.insert(tk.END, f"M98P{int(program_number)}\n")
            n += 1

        n = 0
        while n < chamfer_times :
            x = round(diameter - ((n * chamfer_times_mm)*2),3)
            w = round((((diameter - finish) / 2) * math.tan(math.radians(angle / 2))) + (((reserve + chamfer_r))) * math.tan(math.radians(angle / 2))-(math.sqrt((reserve + chamfer_r)**2 - ((reserve + chamfer_r) - (n * chamfer_times_mm))**2)), 3) 
            if  reserve == lathe_tool :
                text_box_1.insert(tk.END, f"X{x}W-{w}\n")
                text_box_1.insert(tk.END, f"M98P{int(program_number)}\n")
            n += 1   
    #牙精車
        def finishing(first_mm , diameter , finish , reserve , chamfer_r):
            value = diameter - ((reserve + chamfer_r))        # 起始值
            decrement = first_mm        # 初始遞減值
            min_decrement = 0.5  # 最小遞減值

            # 儲存結果
            results = [value]
            steps = 0  # 計數器變數

            while value > finish:  # 持續減到最接近 (牙底)
                value -= decrement
                steps += 1  # 計數
                results.append(max(value, 0))  # 確保不會小於 0

                # 更新遞減值 (縮小規律)
                decrement = max(decrement * 0.9, min_decrement)  # 遞減值不能小於 min_decrement
        
            return steps, results  # 返回遞減次數和結果列表
        steps, results = finishing(first_mm , diameter , finish , reserve , chamfer_r)#steps = 趟數 ， results = 遞減值
    
        n = 0
        while n < steps :

            x = round(results[n],3)
            w = round(((x - finish) / 2) * math.tan(math.radians(angle / 2)), 3)

            n += 1

            if reserve == lathe_tool:
                text_box_1.insert(tk.END, f"X{x}W{w}\n")
                text_box_1.insert(tk.END, f"M98P{int(program_number)}\n")
                text_box_1.insert(tk.END, f"X{x}W-{w}\n")
                text_box_1.insert(tk.END, f"M98P{int(program_number)}\n")
        if reserve == lathe_tool:
            text_box_1.insert(tk.END, f"X{finish}W{0}\n")
            text_box_1.insert(tk.END, f"M98P{int(program_number)}\n")

#################副程式##################            


        text_box_2.insert(tk.END, f"O{int(program_number)}\n")
        text_box_2.insert(tk.END, f"G32Z-{int(length_mm)}.F{int(pich)}.\n")
        text_box_2.insert(tk.END, f"G00X{int(diameter+20)}.\n")
        text_box_2.insert(tk.END, f"Z10.\n")
        text_box_2.insert(tk.END, f"M99\n")
        text_box_2.insert(tk.END, f"%\n")
    else:
        messagebox.showinfo('showinfo', '刀具和預留量不匹配') # 清空文本框內容



#複製主程式
def copy_to_clipboard_1():
        main_window.clipboard_clear()
        main_window.clipboard_append(text_box_1.get(1.0, tk.END))
        main_window.update()
        if text_box_1.get(1.0, tk.END).strip() == "":
            messagebox.showinfo("複製", "主程式無內容")
        else:
            messagebox.showinfo("複製", "主程式已複製到剪貼簿")


#複製副程式
def copy_to_clipboard_2():
        main_window.clipboard_clear()
        main_window.clipboard_append(text_box_2.get(1.0, tk.END))
        main_window.update()
        if text_box_2.get(1.0, tk.END).strip() == "":
            messagebox.showinfo("複製", "主程式無內容")
        else:
            messagebox.showinfo("複製", "主程式已複製到剪貼簿")


def main_gui(root):
    global main_window ,pich_entry, spacing_entry, diameter_entry, angle_entry, tool_type_var, first_mm_entry, reserve_entry, chamfer_r_entry, length_mm_entry, program_number_entry, text_box_1, text_box_2
    main_window = tk.Toplevel(root)
    main_window.title("牙球車牙計算")

    # 使用內建字體
    default_font = font.Font(family="Microsoft JhengHei", size=10)

    # Label 和 Entry 設置字體
    tk.Label(main_window, text="牙距", font=default_font).grid(row=0, column=0, padx=10, pady=8, sticky="e")
    pich_entry = tk.Entry(main_window, width=10, font=default_font)
    pich_entry.insert(0, "14")  # 預設值
    pich_entry.grid(row=0, column=1, padx=10, pady=8)

    tk.Label(main_window, text="齒頂寬", font=default_font).grid(row=1, column=0, padx=10, pady=8, sticky="e")
    spacing_entry = tk.Entry(main_window, width=10, font=default_font)
    spacing_entry.insert(0, "1.75")
    spacing_entry.grid(row=1, column=1, padx=10, pady=8)

    tk.Label(main_window, text="外徑", font=default_font).grid(row=2, column=0, padx=10, pady=8, sticky="e")
    diameter_entry = tk.Entry(main_window, width=10, font=default_font)
    diameter_entry.insert(0, "360")
    diameter_entry.grid(row=2, column=1, padx=10, pady=8)

    tk.Label(main_window, text="牙角度", font=default_font).grid(row=3, column=0, padx=10, pady=8, sticky="e")
    angle_entry = tk.Entry(main_window, width=10, font=default_font)
    angle_entry.insert(0, "60")
    angle_entry.grid(row=3, column=1, padx=10, pady=8)

    # 搜尋條件下拉菜單
    tk.Label(main_window, text="刀具種類", font=default_font).grid(row=4, column=0, padx=10, pady=8, sticky="e")
    tool_type_var = tk.StringVar(value="粗車牙刀")  # 默認選項
    lathe_tool_option_menu = ttk.Combobox(
        main_window,
        textvariable=tool_type_var,
        values=["粗車牙刀", "精車牙刀", "切槽刀(6mm)", "切槽刀(5mm)", "切槽刀(4mm)", "切槽後粗車"],
        font=default_font,
        width=8,
        state="readonly"  # 設置為只讀模式
    )
    lathe_tool_option_menu.grid(row=4, column=1, padx=10, pady=8)

    tk.Label(main_window, text="起始加工深度", font=default_font).grid(row=5, column=0, padx=10, pady=8, sticky="e")
    first_mm_entry = tk.Entry(main_window, width=10, font=default_font)
    first_mm_entry.insert(0, "1")
    first_mm_entry.grid(row=5, column=1, padx=10, pady=8)

    tk.Label(main_window, text="預留量", font=default_font).grid(row=6, column=0, padx=10, pady=8, sticky="e")
    reserve_entry = tk.Entry(main_window, width=10, font=default_font)
    reserve_entry.insert(0, "0.2")
    reserve_entry.grid(row=6, column=1, padx=10, pady=8)

    tk.Label(main_window, text="牙圓角", font=default_font).grid(row=7, column=0, padx=10, pady=8, sticky="e")
    chamfer_r_entry = tk.Entry(main_window, width=10, font=default_font)
    chamfer_r_entry.insert(0, "0.3")
    chamfer_r_entry.grid(row=7, column=1, padx=10, pady=8)

    tk.Label(main_window, text="加工總長度", font=default_font).grid(row=8, column=0, padx=10, pady=8, sticky="e")
    length_mm_entry = tk.Entry(main_window, width=10, font=default_font)
    length_mm_entry.insert(0, "796")
    length_mm_entry.grid(row=8, column=1, padx=10, pady=8)

    tk.Label(main_window, text="副程式檔號", font=default_font).grid(row=9, column=0, padx=10, pady=8, sticky="e")
    program_number_entry = tk.Entry(main_window, width=10, font=default_font)
    program_number_entry.insert(0, "9999")
    program_number_entry.grid(row=9, column=1, padx=10, pady=8)

    # 創建文本框(主程式)
    text_box_1 = tk.Text(main_window, height=16, width=35, font=default_font)
    text_box_1.grid(row=0, rowspan=7, column=2, columnspan=4, padx=10, pady=8)

    # 創建文本框(副程式)
    text_box_2 = tk.Text(main_window, height=6, width=35, font=default_font)
    text_box_2.grid(row=6, rowspan=3, column=2, columnspan=4, padx=10, pady=8)

    # 創建按鈕來觸發計算
    button = ttk.Button(main_window, text="計算", command=calculate, width=10, style="TButton")
    button.grid(row=9, column=2, columnspan=1, padx=10, pady=8)

    # 複製按鈕，使用 ttk.Button
    copy_button = ttk.Button(main_window, text="複製(主程式)", command=copy_to_clipboard_1, width=10, style="TButton")
    copy_button.grid(row=9, column=3, columnspan=1, padx=10, pady=8)

    # 複製按鈕，使用 ttk.Button
    copy_button = ttk.Button(main_window, text="複製(副程式)", command=copy_to_clipboard_2, width=10, style="TButton")
    copy_button.grid(row=9, column=4, columnspan=1, padx=10, pady=8)

    main_window.mainloop()



