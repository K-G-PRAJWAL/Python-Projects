# import openpyxl and tkinter modules 
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import os, sys, subprocess

from LSB.Text_in_audio import tialcode as tial
from LSB.Image_in_audio import iialcode as iial
from LSB.Audio_in_audio import aialcode as aial

# globally declare  variable 
dir_path = os.path.dirname(os.path.realpath(__file__))

class GUI:

	def xor_strings(self, s):
		return "/".join(str(ord(a)^ord(b)) for a,b in zip(s,self.hash))

	def __init__(self):

		self.root = tk.Tk() 

		self.Carrier_Selection = "Audio"
		self.Carrier_Location = None
		self.Data_Selection = "Text"
		self.Data_Location = None
		self.Algo_Selection = "LSB"
		self.string_var_carrier = tk.StringVar(master=self.root)
		self.string_var_data = tk.StringVar(master=self.root)
		self.string_var_algo = tk.StringVar(master=self.root)
		self.string_btn_password = tk.StringVar(master=self.root)
		self.hash = "GBY7G7GY78HG8HNG8TJI9G3H9"

		# set the background colour of GUI window 
		self.root.configure(background='#ffc0cb') 

		# set the title of GUI window 
		self.root.title("Steganographic Transcoder") 

		# set the configuration of GUI window 
		self.root.geometry("520x350") 

		#Header row
		self.tk_Heading = tk.Label(self.root, font=("Comic Sans MS", 30), text="Tunnel Vision", bg="#ffc0cb")
		self.tk_Heading.grid(row=0, column=2, columnspan=2, sticky=tk.W+tk.E)

		#Carrier row
		self.tk_Carrier_Text = tk.Label(self.root, font=("Comic Sans MS", 25), text="Carrier:", bg="#ffc0cb") 
		self.tk_Audio_Carrier = tk.Radiobutton ( self.root, font=("Comic Sans MS", 13), text="Audio", bg="#ffc0cb", variable=self.string_var_carrier, value="Audio", command=self.carrier_select,  padx=20)
		self.tk_Carrier_File_Text = tk.Label(self.root, font=("Comic Sans MS", 15), text="Carrier Path:", bg="#ffc0cb") 
		self.tk_Carrier_File_Loc_Text = tk.Text(self.root,font="25", bg="white", width=30, height=1) 
		self.tk_Carrier_File_Button = tk.Button(self.root, font=("Comic Sans MS", 10), text="Open file", bg="#da80b1", command=self.open_carrier_file)

		self.tk_Carrier_Text.grid(row=1, column=1, sticky=tk.W)
		self.tk_Audio_Carrier.grid(row=1, column=3)
		self.tk_Carrier_File_Text.grid(row=2, column=1, sticky=tk.W)
		self.tk_Carrier_File_Loc_Text.grid(row=2, column=2, columnspan=2)
		self.tk_Carrier_File_Button.grid(row=2, column=4, rowspan=1, pady=10)

		#Data row
		self.tk_Data_Text = tk.Label(self.root, font=("Comic Sans MS", 25), text="Data:", bg="#ffc0cb") 
		self.tk_Text_Data = tk.Radiobutton ( self.root, font=("Comic Sans MS", 13), text="Text", bg="#ffc0cb", variable=self.string_var_data, value="Text", command=self.data_select,  padx=20)
		self.tk_Image_Data = tk.Radiobutton ( self.root, font=("Comic Sans MS", 13), text="Image", bg="#ffc0cb", variable=self.string_var_data, value="Image", command=self.data_select,  padx=20)
		self.tk_Audio_Data = tk.Radiobutton ( self.root, font=("Comic Sans MS", 13), text="Audio", bg="#ffc0cb", variable=self.string_var_data, value="Audio", command=self.data_select,  padx=20)
		self.tk_Data_File_Text = tk.Label(self.root, font=("Comic Sans MS", 15), text="Data Path:", bg="#ffc0cb") 
		self.tk_Data_File_Loc_Text = tk.Text(self.root,font="25", bg="white", width=30, height=1) 
		self.tk_Data_File_Button = tk.Button(self.root, font=("Comic Sans MS", 10), text="Open file", bg="#da80b1", command=self.open_data_file)

		self.tk_Data_Text.grid(row=3, column=1, sticky=tk.W)
		self.tk_Text_Data.grid(row=3, column=2)
		self.tk_Image_Data.grid(row=3, column=3)
		self.tk_Audio_Data.grid(row=3, column=4)
		self.tk_Data_File_Text.grid(row=4, column=1, sticky=tk.W)
		self.tk_Data_File_Loc_Text.grid(row=4, column=2, columnspan=2)
		self.tk_Data_File_Button.grid(row=4, column=4, rowspan=1, pady=10)

		#Algorithm row
		self.tk_Algo_Text = tk.Label(self.root, font="25", text="Algorithm:", bg="#ffc0cb") 
		self.tk_Text_Algo = tk.Radiobutton ( self.root, font="25", text="LSB", bg="#ffc0cb", variable=self.string_var_algo, value="LSB", command=self.algo_select,  padx=20)

		#Encode/Decode row:
		self.tk_Encode_Button = tk.Button(self.root, font=("Comic Sans MS", 10), text="Encode", bg="#da80b1", command=self.get_password_check_en)
		self.tk_Decode_Button = tk.Button(self.root, font=("Comic Sans MS", 10), text="Decode", bg="#da80b1", command=self.get_password_check_de)
		

		self.tk_Encode_Button.grid(row=6, column=2)
		self.tk_Decode_Button.grid(row=6, column=3)

		self.tk_main_password_btn = tk.Button(self.root, font=("Comic Sans MS", 10), textvariable=self.string_btn_password, bg="#da80b1",command=lambda: self.get_password_dialog("change password"))
		self.tk_main_password_btn.grid(row=7,column=2,columnspan=2,rowspan=1, pady=10, sticky=tk.W+tk.E)

		self.tk_Audio_Carrier.select()
		self.tk_Text_Data.select()
		self.tk_Image_Data.deselect()
		self.tk_Audio_Data.deselect()
		self.tk_Text_Algo.select()

	def carrier_select(self):
		self.Carrier_Selection = str(self.string_var_carrier.get())
		print(self.Carrier_Selection)
		if(self.Carrier_Selection=="Audio"):
			self.tk_Audio_Carrier.select()

	def open_carrier_file(self):
		if self.Carrier_Selection=="Audio":
			self.Carrier_Location = askopenfilename(initialdir = dir_path,title = "Save file as",filetypes = (("WAV files","*.wav"),("all files","*.*")))			
		self.tk_Carrier_File_Loc_Text.insert(tk.INSERT, self.Carrier_Location)

	def data_select(self):
		self.Data_Selection = str(self.string_var_data.get())
		print(self.Data_Selection)
		if self.Data_Selection=="Text":
			self.tk_Text_Data.select()
			self.tk_Image_Data.deselect()
			self.tk_Audio_Data.deselect()
		elif self.Data_Selection=="Image":
			self.tk_Text_Data.deselect()
			self.tk_Image_Data.select()
			self.tk_Audio_Data.deselect()
		else:
			self.tk_Text_Data.deselect()
			self.tk_Image_Data.deselect()
			self.tk_Audio_Data.select()

	def open_data_file(self):
		if self.Data_Selection == "Audio":
			self.Data_Location = askopenfilename(initialdir = dir_path,title = "Save file as",filetypes = (("WAV files","*.wav"),("all files","*.*")))
		elif self.Data_Selection == "Image":
			self.Data_Location = askopenfilename(initialdir = dir_path,title = "Save file as",filetypes = (("PNG files","*.png"),("all files","*.*")))
		else:
			pass
		self.tk_Data_File_Loc_Text.insert(tk.INSERT, self.Data_Location)

	def algo_select(self):
		self.Algo_Selection = str(self.string_var_algo.get())
		print(self.Algo_Selection)
		if self.Algo_Selection=="LSB":
			self.tk_Text_Algo.select()

	def encode(self):
		if self.Carrier_Selection=="Audio" and self.Data_Selection=="Text" and self.Algo_Selection=="LSB":
			print("Inside Encode(): Audio:Text:LSB")
			self.Data_Location = self.tk_Data_File_Loc_Text.get("1.0", tk.END)
			a1 = tial.Text_in_audio_lsb(self.Carrier_Location, self.Data_Location)
			a1.encode()
		elif self.Carrier_Selection=="Audio" and self.Data_Selection=="Image" and self.Algo_Selection=="LSB":
			print("Inside Encode(): Audio:Image:LSB")
			a1 = iial.Image_in_audio_lsb(self.Carrier_Location, self.Data_Location)
			a1.encode()
		elif self.Carrier_Selection=="Audio" and self.Data_Selection=="Audio" and self.Algo_Selection=="LSB":
			print("Inside Encode(): Audio:Audio:LSB")
			a1 = aial.Audio_in_audio_lsb(self.Carrier_Location, self.Data_Location)
			a1.encode()

	def decode(self):
		if self.Carrier_Selection=="Audio" and self.Data_Selection=="Text" and self.Algo_Selection=="LSB":
			print("Inside Decode(): Audio:Text:LSB")
			a1 = tial.Text_in_audio_lsb("","")
			self.print_text_box(a1.decode(self.Carrier_Location))
		elif self.Carrier_Selection=="Audio" and self.Data_Selection=="Image" and self.Algo_Selection=="LSB":
			print("Inside Decode(): Audio:Image:LSB")
			a1 = iial.Image_in_audio_lsb("","")
			a1.decode(self.Carrier_Location)
		elif self.Carrier_Selection=="Audio" and self.Data_Selection=="Audio" and self.Algo_Selection=="LSB":
			print("Inside Decode(): Audio:Audio:LSB")
			a1 = aial.Audio_in_audio_lsb("","")
			a1.decode(self.Carrier_Location)

	def print_text_box(self, string):
		self.top = tk.Toplevel(bg="#ffc0cb")
		self.top.title("Decoded text")
		self.top.geometry("275x175")
		self.tk_toplevel_text = tk.Text(self.top ,font="25", bg="white", width=25, height=7)
		self.tk_toplevel_text.grid(row=0, column=0)
		self.tk_toplevel_text.insert(tk.INSERT, string)
		self.top.mainloop()

	def check_saved_password(self):
		if os.path.exists("config.dat"):
			self.string_btn_password.set("Change password")
			with open("config.dat", "r") as myFile:
				self.saved_hash = myFile.read().split("\n")[0]
			return True
		else: 
			self.string_btn_password.set("Enter password")
			self.saved_hash = None
			return False

	def save_password_dialog(self):

		self.top_password = tk.Toplevel(bg="#ffc0cb")
		self.top_password.title("Password")
		self.top_password.geometry("500x150")

		self.top_password_heading = tk.Label(self.top_password, bg = "#ffc0cb", font="35", text="Save a password to use this tool")
		self.top_password_heading.grid(row=0, column=1)

		self.top_password_label = tk.Label(self.top_password, bg="#ffc0cb", font="25", text="Enter password:")
		self.top_password_text = tk.Text(self.top_password , font="25", bg="white", width=25, height=1)

		self.top_password_label.grid(row=1, column=0)
		self.top_password_text.grid(row=1, column=1)

		self.top_retype_label = tk.Label(self.top_password,bg="#ffc0cb", font="25", text="Re-type password", pady=10)
		self.top_retype_text = tk.Text(self.top_password,  font="25", bg="white", width=25, height=1)
		self.top_pass_submit_btn = tk.Button(self.top_password, font="25", bg="white", text="Submit", command=self.save_password_check)

		self.top_retype_label.grid(row=2, column=0)
		self.top_retype_text.grid(row=2, column=1)
		self.top_pass_submit_btn.grid(row=3, column=1)

		self.top_password.mainloop()

	def save_password_check(self):
		password = self.top_password_text.get("1.0", tk.END).split("\n")[0]
		retype = self.top_retype_text.get("1.0", tk.END).split("\n")[0]
		if password == retype:
			file = open('config.dat','w') 
			file.write(self.xor_strings(password))
			file.close()
			self.check_saved_password()
			self.top_password.destroy()

	def get_password_dialog(self, type):

		if self.check_saved_password() == False:
			self.save_password_dialog()
			return

		self.top_password = tk.Toplevel(bg="#ffc0cb")
		self.top_password.title("Password")
		self.top_password.geometry("500x150")

		self.top_password_label = tk.Label(self.top_password, bg="#ffc0cb", font="25", text="Enter password:")
		self.top_password_text = tk.Text(self.top_password , font="25", bg="white", width=25, height=1)

		self.top_password_label.grid(row=1, column=0)
		self.top_password_text.grid(row=1, column=1)

		self.top_pass_submit_btn = tk.Button(self.top_password, font="25", bg="white", text="Submit", command=lambda: self.get_password_check(type))
		self.top_pass_submit_btn.grid(row=3, column=1)

		self.top_password.mainloop()

	def get_password_check(self, type):
		password = self.top_password_text.get("1.0", tk.END).split("\n")[0]
		with open("config.dat", "r") as myFile:
			saved_hash = myFile.read().split("\n")[0]

		print(self.xor_strings(password), saved_hash)
		print(self.xor_strings(password) == saved_hash)

		if self.xor_strings(password) == saved_hash:
			self.top_password.destroy()
			if type=="encode":
				self.encode()
			elif type=="decode": 
				self.decode()
			else:
				self.save_password_dialog()
		self.top_password.destroy()

	def get_password_check_en(self):
		if self.check_saved_password():
			self.get_password_dialog("encode")
		else:
			messagebox.showerror("Error", "You have not saved a password.")

	def get_password_check_de(self):
		if self.check_saved_password():
			self.get_password_dialog("decode")
		else:
			messagebox.showerror("Error", "You have not saved a password.")

	def start_gui(self):

		self.check_saved_password()
		self.root.mainloop() 