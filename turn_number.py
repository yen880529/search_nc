import tkinter as tk
from tkinter import filedialog, messagebox, Label, Button
import os
import shutil



default_folder_path = r"M:\01_部門專區\36100_生產部\02_部門共用\06_生技課\機械課共用\機二組nc"

# 選擇檔案
def select_files():
    global selected_files
    selected_files = filedialog.askopenfilenames(title="選擇檔案")
    
    # 更新顯示選擇的檔案
    if selected_files:
        selected_files_label.config(text="選擇的檔案: " + ", ".join([os.path.basename(f) for f in selected_files]))

# 選擇資料夾
def select_folder():
    global selected_folder_path
    selected_folder_path = filedialog.askdirectory(title="選擇資料夾", initialdir=default_folder_path)
    
    # 更新顯示選擇的資料夾
    if selected_folder_path:
        selected_folder_label.config(text=f"選擇的資料夾: {selected_folder_path}")

# 將檔案插入資料夾
def copy_files_to_folder():
    if selected_files and selected_folder_path:
        # 跳出詢問對話框，確認是否要繼續操作
        user_confirmation = messagebox.askyesno("確認", "是否要複製檔案到所選資料夾？")
        
        # 如果用戶選擇 "是"，則繼續執行複製
        if user_confirmation:
            try:
                copied_files_info = []
                for file_path in selected_files:
                    file_name = os.path.basename(file_path)
                    new_file_path = os.path.join(selected_folder_path, file_name)
                    
                    # 使用 shutil.copy 進行文件複製
                    shutil.copy(file_path, new_file_path)
                    
                    # 收集檔案名稱與目標路徑
                    copied_files_info.append(f"檔案: {file_name}")

                # 成功後顯示訊息
                messagebox.showinfo("成功", f"{len(selected_files)} 個檔案已複製到資料夾: {selected_folder_path}")

                # 將選擇的檔案和資料夾資訊寫入到指定的文字文件
                log_file_path = r"M:\01_部門專區\36100_生產部\02_部門共用\06_生技課\機械課共用\機二組nc\回傳資料.txt"
                with open(log_file_path, 'a', encoding='utf-8') as log_file:
                    log_file.write("複製檔案記錄:\n")
                    for info in copied_files_info:
                        log_file.write(info + '\n')
                    log_file.write(f"目標資料夾: {selected_folder_path}\n\n")

            except Exception as e:
                messagebox.showerror("錯誤", f"檔案複製失敗: {e}")
        else:
            # 如果用戶選擇 "否"，則取消操作
            messagebox.showinfo("取消", "檔案複製操作已取消。")
    else:
        messagebox.showwarning("錯誤", "請先選擇檔案和資料夾。")

# 彈出新窗口，包含三個按鈕
def open_file_folder_window(root):
    new_window = tk.Toplevel(root)
    new_window.title("選擇檔案和資料夾")

    # 確保新窗口保持在主窗口之上
    new_window.transient(root)  # 將新窗口與主窗口關聯
    new_window.grab_set()       # 禁止與主窗口進行交互
    new_window.focus()          # 將焦點設置到新窗口

    # 按鈕: 選擇檔案
    select_file_button = Button(new_window, text="選擇程式.nc", command=select_files)
    select_file_button.grid(row=0, column=0, padx=10, pady=10)

    # 按鈕: 選擇資料夾
    select_folder_button = Button(new_window, text="選擇資料夾", command=select_folder)
    select_folder_button.grid(row=1, column=0, padx=10, pady=10)

    # 按鈕: 插入檔案到資料夾
    copy_button = Button(new_window, text="回傳", command=copy_files_to_folder)
    copy_button.grid(row=2, column=0, columnspan=1, padx=10, pady=10)

    # 顯示選擇的檔案和資料夾的標籤
    global selected_files_label, selected_folder_label
    selected_files_label = Label(new_window, text="選擇的檔案: 無")
    selected_files_label.grid(row=0, column=1, columnspan=2, padx=10, pady=5)

    selected_folder_label = Label(new_window, text="選擇的資料夾: 無")
    selected_folder_label.grid(row=1, column=1, columnspan=2, padx=10, pady=5)

