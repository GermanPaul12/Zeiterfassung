from tkinter import * 
import customtkinter
from main import daterange
import datetime as dt
import pandas as pd

root = customtkinter.CTk()

root.title('Zeiterfassung')

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
root.geometry("1000x500")
root.configure(bg='black')


dates = [dtt.strftime('%Y-%m-%d') for dtt in daterange(dt.datetime.strptime(f"{dt.datetime.now().year-2}-01-01", "%Y-%m-%d"),
                                                                                             dt.datetime.strptime("2025-09-30", "%Y-%m-%d"))]

kommen = ['08:00' for i in range(len(dates))]
pause = ['0:30' for i in range(len(dates))]
gehen = ['16:30' if i % 3 != 0 else '15:30' for i in range(len(dates))]    

weekday = [dt.datetime.strptime(date, '%Y-%m-%d').weekday() for date in dates]
dict_wochentag = {0:'Montag', 1:'Dienstag', 2:'Mittwoch', 3:'Donnerstag', 4:'Freitag', 5:'Samstag', 6:'Sonntag'}
wochentag = [dict_wochentag[i] for i in weekday]

dict_data = {'Datum':dates, 'Kommen':kommen, 'Pause':pause, 'Gehen':gehen}

df = pd.DataFrame(dict_data)
df['Wochentag'] = wochentag
df['Datum'] = pd.to_datetime(df['Datum'])
df = df[df['Wochentag'] != 'Samstag']
df = df[df['Wochentag'] != 'Sonntag']

def refresh_and_save():
   table_raw = df[df['Datum']>dt.datetime.strptime(zeiterfassung_entry.get(), "%Y-%m-%d")-dt.timedelta(days=5)]
   table_clean = table_raw[table_raw['Datum']<dt.datetime.strptime(zeiterfassung_entry.get(), "%Y-%m-%d")+dt.timedelta(days=5)]
   zeiterfassung_entry_message.configure(
      text=table_clean)
   

frame = customtkinter.CTkFrame(master=root,
                               width=1000,
                               height=500,
                               corner_radius=10,
                               bg='black',
                               fg_color='black',
                               border_width=2, border_color="white")

datum_label = customtkinter.CTkLabel(root, text="Datum:", width=130,
                               height=40,
                               fg_color=("white", "#0F3D3E"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 24),
                               bg_color='black')

uhrzeit_label = customtkinter.CTkLabel(root, text="Uhrzeit:", width=130,
                               height=40,
                               fg_color=("white", "#0F3D3E"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 24),
                               bg_color='black',
                               )

zeiterfassung_entry = customtkinter.CTkEntry(root, width=140,
                               height=40,
                               corner_radius=10,
                              fg_color='#0F3D3E',
                              fg='white',
                              text_font=('Times New Roman', 20),
                              justify=CENTER,
                              bg_color='black',
                              border_width=2, border_color="white",
                              text_color='white'
                            )

zeiterfassung_message = customtkinter.CTkLabel(root, text=f"Zeiterfassungstabelle:", width=140,
                               height=40,
                               fg_color=("white", "#0F3D3E"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 24),
                               bg_color='black')


zeiterfassung_entry_times = customtkinter.CTkEntry(root, width=140,
                               height=40,
                               corner_radius=10,
                            fg_color='#0F3D3E',
                            text_font=('Times New Roman', 20),
                            justify=CENTER,
                               bg_color='black',
                               border_width=2, border_color="white",
                               text_color='white'
                            )


zeiterfassung_button = customtkinter.CTkButton(root, width=195,
                                 height=40,
                                 corner_radius=8,
                                 command=refresh_and_save,
                                 text="Refresh and Save",
                                 fg_color='#0F3D3E',
                                 text_font=('Times New Roman', 24),
                               bg_color='black',
                               hover_color='#3AB4F2',
                               border_width=2, border_color="white",
                               text_color='white'
                                 )
combobox = customtkinter.CTkOptionMenu(master=root,
                                       values=["Kommen", "Gehen", "Pause"], 
                                       width=80,
                                        height=40,
                                        fg_color=("white", "#0F3D3E"),
                                        corner_radius=8, 
                                        text_font=('Times New Roman', 24),
                                        bg_color='black',
                                        text_color='black',
                                        
                                        button_color='#0F3D3E',
                                        button_hover_color='#3AB4F2',
                                        dropdown_text_font=('Times New Roman', 24),
                                                           
                                        )

'''
datum_combobox = customtkinter.CTkOptionMenu(master=root,
                                       values=[dtt.strftime('%Y-%m-%d') for dtt in daterange(dt.datetime.strptime(f"{dt.datetime.now().year}-01-01", "%Y-%m-%d"),
                                                                                             dt.datetime.strptime("2025-09-30", "%Y-%m-%d"))], 
                                       width=80,
                                        height=40,
                                        fg_color=("white", "#0F3D3E"),
                                        corner_radius=8, 
                                        text_font=('Times New Roman', 24),
                                        bg_color='black',
                                        text_color='black',
                                        
                                        button_color='#0F3D3E',
                                        button_hover_color='#3AB4F2',
                                        dropdown_text_font=('Times New Roman', 24),
                                                           
                                        )
'''                                        
#insert default text in Entry Boxes
zeiterfassung_entry_times.insert(0, '00:00')
zeiterfassung_entry.insert(0, dt.datetime.now().strftime("%Y-%m-%d"))


zeiterfassung_entry_message = customtkinter.CTkLabel(root, 
                              text='', width=140,
                              height=40,
                              fg_color=("#0F3D3E", "white"),
                              corner_radius=8, 
                              text_font=('Times New Roman', 10),
                              bg_color='black',
                              text_color='white')

#datum_combobox.grid(row=0, column=2, sticky='ew', padx=10, columnspan=2)
#datum_combobox.set(dt.datetime.now().strftime("%Y-%m-%d"))  # set initial value
combobox.grid(row=1, column=2, sticky='ew', padx=10, columnspan=2)
combobox.set("")  # set initial value

#Packing them on the screen
frame.grid(row=0, column=0, columnspan=6, rowspan=10, sticky='news')
datum_label.grid(row=0, column=0, columnspan=2, rowspan=1, sticky='ew', padx=10)
uhrzeit_label.grid(row=1, column=0, columnspan=2, rowspan=1, sticky='ew', padx=10)
zeiterfassung_entry.grid(row=0, column=2, sticky='ew', padx=10, columnspan=4)
zeiterfassung_message.grid(row=2, column=0, sticky='ew', padx=10, columnspan=6)
zeiterfassung_entry_times.grid(row=1, column=4, padx=10, sticky='ew', columnspan=2)
zeiterfassung_entry_message.grid(row=3, column=0, padx=10, sticky='nsew', columnspan=6, rowspan=6)
zeiterfassung_button.grid(row=9, column=0, columnspan=6, sticky='ew', padx=10)


   
root.mainloop()