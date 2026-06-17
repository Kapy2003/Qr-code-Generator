import customtkinter as cck
from pathlib import Path
from PIL import Image
import backend 

app = cck.CTk()
app.title("Qr Code Generator")
app.geometry("500x560")
app.resizable(False, False)

def on_generate_click():
    error_label.configure(text="")
    
    data_entry = entry.get().strip()
    call_name = name.get().strip()
    
    if not data_entry or not call_name:
        error_label.configure(text="Error: Please fill in all fields!", text_color="#ff4444")
        return
        
    try:
        backend.generate_qr(name=call_name, entry=data_entry)
        
        img_file = call_name if call_name.endswith(".png") else Path(call_name).stem + ".png"
        full_path = Path("./qr-generated/") / img_file
        
        pil_img = Image.open(full_path)
        ctk_img = cck.CTkImage(light_image=pil_img, dark_image=pil_img, size=(160, 160))
        
        # Reveal the image inside our clean frame
        qr_preview_label.configure(image=ctk_img, text="")
        status_label.configure(text=f"Saved: {img_file}", text_color="#44ff44")
        
        entry.delete(0, 'end')
        name.delete(0, 'end')
        
    except Exception as e:
        error_label.configure(text=f"Failed to generate: {e}", text_color="#ff4444")

# --- Top Inputs Area ---
entry = cck.CTkEntry(app, width=350, height=35, placeholder_text="Enter Text or URL for QR Code")
entry.pack(pady=(25, 10))

name = cck.CTkEntry(app, width=350, height=35, placeholder_text="Enter Name for the Image File")
name.pack(pady=10)

gen_button = cck.CTkButton(app, text="Generate QR Code", command=on_generate_click, font=("Arial", 14, "bold"), height=42, width=200)
gen_button.pack(pady=15)

error_label = cck.CTkLabel(app, text="", font=("Arial", 12))
error_label.pack(pady=2)

# --- NEW: Beautiful Preview Card Frame ---
# This frame acts as a container to hold the image cleanly
preview_card = cck.CTkFrame(app, width=220, height=220, corner_radius=15, border_width=2, border_color="#3a3a3a")
preview_card.pack(pady=10)
preview_card.pack_propagate(False) # Stops the frame from shrinking around empty space

# Placeholder layout inside the card frame
qr_preview_label = cck.CTkLabel(preview_card, text="Preview will\nappear here", font=("Arial", 13, "italic"), text_color="#777777")
qr_preview_label.pack(expand=True)

# Small success status tracker under the card
status_label = cck.CTkLabel(app, text="", font=("Arial", 11))
status_label.pack(pady=5)

app.mainloop()
