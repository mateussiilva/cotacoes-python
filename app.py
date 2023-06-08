import customtkinter as ctk 


class WindowMain():
    def __init__(self, titulo):
        self.__root = ctk.CTk()
        self.__root.title(titulo)
        
        self.__root.mainloop()

    @staticmethod
    def container():
        root  = WindowMain().__root
        frame = ctk.CTkFrame(root,bg_color="red")
        frame.pack()
        
        
        
if __name__ == "__main__":
    window = WindowMain("Cotação")
    window.container()
