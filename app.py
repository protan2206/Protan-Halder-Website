from flask import Flask, send_file, request, render_template
import os
import qrcode
from gtts import gTTS as GT

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route("/developer", methods=['GET', 'POST'])
def Developer():
    return render_template('developer.html')


@app.route("/qr_code", methods=['GET', 'POST'])
def QR_CODE():
    if request.method == 'POST':
        QRC = request.form['QR_data']
        print(QRC)
        img = qrcode.make(QRC)
        try:
            os.remove("ProtanHalder_QR_image.png")
        except:
            pass
        finally:
            img.save('ProtanHalder_QR_image.png')
    return render_template('TextToQR.html')


@app.route("/online_profile", methods=['GET', 'POST'])
def Online_profile():
    if request.method == 'POST':
        url_type = request.form['type']
        data  = request.form['data']
        if url_type == "facebook":
            img = qrcode.make(data)
            try:
                os.remove("ProtanHalder_facebook_QR_image.png")
            except:
                pass
            finally:
                img.save('ProtanHalder_facebook_QR_image.png')
            print("facebook founded")
        elif url_type =="messenger":
            
            img = qrcode.make("https://www.messenger.com/t/"+data.split("/")[3])
            try:
                os.remove("ProtanHalder_messenger_QR_image.png")
            except:
                pass
            finally:
                img.save('ProtanHalder_messenger_QR_image.png')
            print("messgenger Founded")
        elif url_type =="whatsapp":
            img = qrcode.make("https://wa.me/"+data)
            try:
                os.remove("ProtanHalder_whatsapp_QR_image.png")
            except:
                pass
            finally:
                img.save('ProtanHalder_whatsapp_QR_image.png')
            print("Whatsapp Founded")
        elif url_type =="phone":
            img = qrcode.make("tel:"+data)
            try:
                os.remove("ProtanHalder_phone_QR_image.png")
            except:
                pass
            finally:
                img.save('ProtanHalder_phone_QR_image.png')
            print("phone Founded")
        elif url_type =="messege":
            img = qrcode.make("sms:"+data+"&body=Hi....!🥰 How are you ?")
            try:
                os.remove("ProtanHalder_Message_QR_image.png")
            except:
                pass
            finally:
                img.save('ProtanHalder_Message_QR_image.png')
            print("Messege Founded")
    return render_template('OnlineProfileToQR.html')


@app.route("/audio_maker", methods=['GET', 'POST'])
def AUDIO_MKR():
    if request.method == 'POST':
        Audio_Data = request.form['AUDIO_data']
        print(Audio_Data)
        Audio = GT(str(Audio_Data))
        try:
            os.remove("ProtanHalder_Text_To_Audo.mp3")
            print("remove audo")
        except:
            pass
        finally:
            Audio.save("ProtanHalder_Text_To_Audo.mp3")
    return render_template('TextToAudio.html')


@app.route("/fb_download", methods=['GET', 'POST'])
def download_FB_qr_file():
    return send_file("ProtanHalder_facebook_QR_image.png", as_attachment=True)

@app.route("/messenger_download", methods=['GET', 'POST'])
def download_Messenger_qr_file():
    return send_file("ProtanHalder_messenger_QR_image.png", as_attachment=True)


@app.route("/whatsapp_download", methods=['GET', 'POST'])
def download_WhatsApp_qr_file():
    return send_file("ProtanHalder_whatsapp_QR_image.png", as_attachment=True)


@app.route("/phone_download", methods=['GET', 'POST'])
def download_Phone_qr_file():
    return send_file("ProtanHalder_phone_QR_image.png", as_attachment=True)

@app.route("/message_download", methods=['GET', 'POST'])
def download_Message_qr_file():
    return send_file("ProtanHalder_Message_QR_image.png", as_attachment=True)


@app.route("/qr_download", methods=['GET', 'POST'])
def download_qr_file():
    p = "ProtanHalder_QR_image.png"
    return send_file(p, as_attachment=True)


@app.route("/audio_download", methods=['GET', 'POST'])
def download_audio_file():
    p = "ProtanHalder_Text_To_Audo.mp3"
    return send_file(p, as_attachment=True)



if __name__ == "__main__":
    app.run( host='0.0.0.0', port=4444 , debug=True)
    # app.run(debug=True)