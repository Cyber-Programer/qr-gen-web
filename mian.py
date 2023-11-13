from flask import Flask, request, render_template
from PIL import Image
import qrcode

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        data = request.form['text']
        fill_color = request.form['favcolor']
        back_color = request.form['fontcolor']
        if fill_color == back_color:
            return '2 color is same....'
        if not data:
            return 'Must input data or text....'
        qr_gen(data, fill_color, back_color)

        # Pass the image URL to the show.html template
        image_url = "static/some_file.png"
        return render_template('show.html', image_url=image_url)
    else:
        return render_template('index.html')

def qr_gen(data, fill_color, back_color):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    # Save the image
    img.save("static/some_file.png")  # Save to the 'static' folder

if __name__ == "__main__":
    app.run(debug=True)
