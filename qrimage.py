from flask import Flask,render_template,request,url_for,redirect,session,flash,jsonify,send_file #borrar las q no use
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
    error_correction=qrcode.constants.ERROR_CORRECT_L,
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
    #app.run(host="0.0.0.0", port=5000) #para q entre alguien con misma ip
    app.run(debug=True)