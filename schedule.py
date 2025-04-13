import tkinter as tk

class Schedule () :

    def __init__ (self, root) :
        self.size = 0
        self.items = []

        self.window = root
        self.window.title("일정표")
        self.window.geometry("800x600")
        self.window.resizable(width=False, height=False)


        # 일정 추가     
        date_label = tk.Label(self.window, text = "년도/월/날짜 순으로 입력하세요")
        date_label.grid(row = 0, column = 0, sticky = tk.N)
        
        self.date_entry = tk.Entry(self.window, width = 30)
        self.date_entry.grid(row = 1, column = 0, sticky = tk.N)

        schedule_label = tk.Label(self.window, text = "일정을 입력하세요")
        schedule_label.grid(row = 2, column = 0, sticky = tk.N)
        
        self.schedule_entry = tk.Entry(self.window, width = 30)
        self.schedule_entry.grid(row = 3, column = 0, sticky = tk.N)

        detail_label = tk.Label(self.window, text = "세부사항을 입력하세요")
        detail_label.grid(row = 4, column = 0, sticky = tk.N)
        
        self.detail_entry = tk.Entry(self.window, width = 30)
        self.detail_entry.grid(row = 5, column = 0, sticky = tk.N)

        add_button = tk.Button(self.window, width = 20, height = 2, text = '추가하기', command = self.add_schedule)
        add_button.grid(row = 6, column = 0, sticky = tk.N) 


        # 일정 삭제
        remove_label = tk.Label(self.window, text = "삭제하고 싶은 줄을 입력하세요(1)")
        remove_label.grid(row = 7, column = 0, sticky = tk.N)

        self.remove_entry = tk.Entry(self.window)
        self.remove_entry.grid(row = 8, column = 0, sticky = tk.N)
        
        remove_button = tk.Button(self.window, width = 20, height = 2, text = '삭제하기', command = self.remove_schedule)
        remove_button.grid(row = 9, column = 0, sticky = tk.N)


        # 일정표 프레임
        self.schedule_frame = tk.Frame(self.window)
        self.schedule_frame.grid(row = 0, column = 1, columnspan = 400, rowspan = 400, sticky = tk.N)

        schedule_date_label = tk.Label(self.schedule_frame, text = "날짜", bg = '#FFBF00')
        schedule_date_label.grid(row = 0, column = 0, padx = 30, sticky = tk.N)

        schedule_schedule_label = tk.Label(self.schedule_frame, text = "일정")
        schedule_schedule_label.grid(row = 0, column = 1, padx = 40, sticky = tk.N)

        schedule_detail_label = tk.Label(self.schedule_frame, text = "세부사항")
        schedule_detail_label.grid(row = 0, column = 2, padx = 60, sticky = tk.N)

        
    def add_schedule (self) :
        
        date_input = self.date_entry.get() # "1.0", END
        schedule_input = self.schedule_entry.get() #
        detail_input = self.detail_entry.get() # 

        self.size += 1
        self.items.append([date_input, schedule_input, detail_input])

        item_date_label = tk.Label(self.schedule_frame, text = date_input)
        item_date_label.grid(row = self.size, column = 0, padx = 5, sticky = tk.N)

        item_schedule_label = tk.Label(self.schedule_frame, text = schedule_input)
        item_schedule_label.grid(row = self.size, column = 1, padx = 5, sticky = tk.N)

        item_detail_label = tk.Label(self.schedule_frame, text = detail_input)
        item_detail_label.grid(row = self.size, column = 2, padx = 5, sticky = tk.N)

        self.date_entry.delete(0, tk.END) # 
        self.schedule_entry.delete(0, tk.END) #
        self.detail_entry.delete(0, tk.END) #

        
    def remove_schedule (self) :
        index = int(self.remove_entry.get())

        self.reset_schedule()
    
        self.size -= 1
        self.items.remove(self.items[index-1])

        self.update_schedule()
        

    def reset_schedule (self) :
        
        all_items = self.schedule_frame.grid_slaves()
        for i in range (3 * self.size -1 , -1, -1) :
            all_items[i].destroy()

    def update_schedule (self) :

        for i in range (self.size) :
            item_date_label = tk.Label(self.schedule_frame, text = self.items[i][0])
            item_date_label.grid(row = (i+1), column = 0, padx = 5, sticky = tk.N)

            item_schedule_label = tk.Label(self.schedule_frame, text = self.items[i][1])
            item_schedule_label.grid(row = (i+1), column = 1, padx = 5, sticky = tk.N)

            item_detail_label = tk.Label(self.schedule_frame, text = self.items[i][2])
            item_detail_label.grid(row = (i+1), column = 2, padx = 5, sticky = tk.N)


root = tk.Tk()
scheduler = Schedule(root)
root.mainloop()
