from pyscript import display, document

def calculate_total(e):
    document.getElementById("receipt").innerHTML = ""

    shoyu_ramen = document.getElementById("shoyu_ramen").checked
    miso_ramen = document.getElementById("miso_ramen").checked
    tonkotsu_ramen = document.getElementById("tonkotsu_ramen").checked
    spicy_ramen = document.getElementById("spicy_ramen").checked

    subtotal = (shoyu_ramen * 180) + (miso_ramen * 200) + (tonkotsu_ramen * 220) + (spicy_ramen * 190)

    tax = subtotal * 0.12
    total = subtotal + tax

    display("=RECIEPT=", target="receipt")
    display(f"Subtotal: ₱{subtotal:f}", target="receipt")
    display(f"VAT (12%): ₱{tax:f}", target="receipt")
    display(f"Total: ₱{total:f}", target="receipt")
