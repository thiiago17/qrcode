from flask import Flask,render_template,request,url_for,redirect 
import io
import base64
import qrcode

app=Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/generar", methods=["POST"])
def generar():
    texto=request.form["qrlink"]
    
    qr = qrcode.QRCode( #IMPORTANTE: SI EL ARCHIVO SE LLAMA qrcode.py GENERA CONFLICTO Y DA ATRIBUTE ERROR
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=4,
)

    qr.add_data(texto) 
    qr.make(fit=True)

    buf=qr.make_image(fill_color="black",back_color="white") 

    img=io.BytesIO() 
    buf.save(img,format="png") 
    img.seek(0) 

    qr_img=base64.b64encode(img.getvalue()).decode("utf-8") 

    return render_template("index.html",qr_img=qr_img)


if __name__=="__main__":
    app.run(debug=True)