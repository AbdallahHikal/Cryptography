import tkinter as tk
from tkinter import ttk
from fun import *
import ast

def perform_operation():

    input_text = input_field.get()
    algorithm = encryption_type.get()
    operation = operation_choice.get()

#   ---------------------------------- Not Selected ------------------------------
    if operation not in ["Encrypt", "Decrypt"]:
        result_label.config(text="⚠️ Please select an operation (Encrypt or Decrypt).")
        return
    


#   ---------------------------------- Selection Encrypt ------------------------------
    elif operation=="Encrypt":

        if(algorithm=="Caesar"):
            key=3                       # plain= decodex  , key= 3
            output=caesar_E(input_text,key)

        elif(algorithm=="Affine"):
            key1=17
            key2=20             # plain= crypto  , key1= 17 , key2= 20
            output=affine_E(input_text,key1,key2)

        elif(algorithm=="Vigener"):
            k="root"                        # k = root, p= mysection
            key= generate_key(input_text,k)
            output=vigener_E(input_text,key)
            
        elif(algorithm=="RailFence"):       # p= meetmeafterthetogaparty , key= 2
            key=2
            output=railfence_E(key,input_text)

        elif(algorithm=="OneTimePad"):
            key="key"                # p= One Time Cipher , key= key
            output=onetimepad_E(input_text,key)

        elif(algorithm=="Columnar"):       # p= hello world , key= 2314   
            key="2314"
            output= columnar_E(input_text,key)

        elif(algorithm=="DES"):           #data= DES Algorithm Implementation
            output= des_E(input_text)

        elif(algorithm=="Scytale"):       # p= HELLO WORLD , columns= 3
            columns=3
            output= scytale_E(input_text, columns)

        elif(algorithm=="Keyboard_Offset"):             # p= HELLO
            output= keyboard_offset_E(input_text)

        elif(algorithm=="RSA"):
            output= rsa_E(input_text)



#   ---------------------------------- Selection Decrypt ------------------------------
    else:

        if(algorithm=="Caesar"):  
            key=3                         # c= ghfrgh{ , k= 3
            output=caesar_D(input_text,key)

        elif(algorithm=="Affine"):
            key1=17
            key2=20                 # c= cxmpfy  , k1= 17 , k2= 20
            output= affine_D(input_text,key1,key2)

        elif(algorithm=="Vigener"):
            k="root"                    # k = root , c= dmgxthwhe
            key= generate_key(input_text,k)
            output=vigener_D(input_text,key)

        elif(algorithm=="RailFence"):       # c= mematrhtgpryetefeteoaat , key= 2
            key=2
            output=railfence_D(key,input_text)

        elif(algorithm=="OneTimePad"):
            key="key"                   # c= One Time Cipher , key= key
            output=onetimepad_D(input_text,key)

        elif(algorithm=="Columnar"):       # c= 'lwdhore llo_' , key= 2314   
            key="2314"
            output= columnar_D(input_text,key)

        elif(algorithm=="DES"):
            output= des_D(input_text)

        elif(algorithm=="Scytale"):       # c= 'HLWLEOODL R_' , columns= 3
            columns=3
            output= scytale_D(input_text, columns)

        elif(algorithm=="Keyboard_Offset"):         # c= JRZZP
            output= keyboard_offset_D(input_text)

        elif(algorithm=="RSA"):
            p=ast.literal_eval(input_text)  ## Safely convert string to list to skip error when convert
            output= rsa_D(p)



#   ---------------------------------- Display Message ------------------------------
    msg = f"{operation}ing with {algorithm}\n\nInput: {input_text}\n\nOutput: {output}"
    result_label.config(text=msg)



#   --------------------- Delete Inserted Data After Operation ----------------------
    input_field.delete(0, tk.END)



#   ---------------------------------- Set Placeholder ------------------------------
def set_placeholder(entry, placeholder_text):
    entry.insert(0, placeholder_text)
    entry.config(fg='gray')

    def on_focus_in(event):
        if entry.get() == placeholder_text:
            entry.delete(0, tk.END)
            entry.config(fg='black')

    def on_focus_out(event):
        if entry.get() == '':
            entry.insert(0, placeholder_text)
            entry.config(fg='gray')

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)



#   ---------------------------------- GUI ------------------------------
root = tk.Tk()
root.title("Encryption Tool")
root.config(bg="#01002b")
root.resizable(False, False)
root.geometry("500x400")

input_field = tk.Entry(root, width=50, font=("Arial", 12))
input_field.pack(pady=20)
set_placeholder(input_field, "Enter text")


encryption_type = tk.StringVar()
encryption_type.set("Select encryption")
encryption_options = ["Caesar", "Affine", "Vigener", "RailFence","OneTimePad", "Columnar", "RSA", "DES", "Scytale", "Keyboard_Offset"]
encryption_menu = ttk.OptionMenu(root, encryption_type, *encryption_options)
encryption_menu.config(width=40)
encryption_menu.pack(pady=20)

operation_choice = tk.StringVar(value="")
radio_frame = tk.Frame(root, bg="#01002b")
radio_frame.pack(pady=10)

encrypt_radio = tk.Radiobutton(radio_frame, text="Encrypt", variable=operation_choice, value="Encrypt", bg="#01002b", fg="white", selectcolor="#01002b", font=("Arial", 10))
encrypt_radio.pack(side=tk.LEFT, padx=10)

decrypt_radio = tk.Radiobutton(radio_frame, text="Decrypt", variable=operation_choice, value="Decrypt", bg="#01002b", fg="white", selectcolor="#01002b", font=("Arial", 10))
decrypt_radio.pack(side=tk.LEFT, padx=10)

action_button = tk.Button(root, text="Proceed", command=perform_operation, width=20, height=2, font=("Arial", 10))
action_button.pack(pady=30)

result_label = tk.Label(root, text="", bg="#01002b", fg="green", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
