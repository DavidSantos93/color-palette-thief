import os
from colorthief import ColorThief
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import SubmitField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename
from shutil import copyfile


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "static/"

Bootstrap(app)

app.secret_key = "thievesguild"

image_path = "static/img/mountain.png"
image_to_upload = f'src="{image_path}"'


class FileForm(FlaskForm):
    photo = FileField(label="Select Image", validators=[FileRequired('File was empty!'),
                                                        FileAllowed(['png', 'jpg', 'pdf'], 'Image only!')])
    submit = SubmitField(label="Submit")


def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb


@app.route('/', methods=["GET", "POST"])
def home():
    color_thief = ColorThief(image_path)
    color_palette = color_thief.get_palette(quality=1, color_count=9)
    file_up_form = FileForm()

    if file_up_form.validate_on_submit():
        f = file_up_form.photo.data
        filename = secure_filename("mountain.png")
        f.save(os.path.join(app.instance_path, 'img', filename))
        os.remove('static/img/mountain.png')
        copyfile('instance/img/mountain.png', 'static/img/mountain.png')
        return redirect(url_for('home'))
    color0_hex = f"style=background-color:#{rgb_to_hex(color_palette[0])}"
    color1_hex = f"style=background-color:#{rgb_to_hex(color_palette[1])}"
    color2_hex = f"style=background-color:#{rgb_to_hex(color_palette[2])}"
    color3_hex = f"style=background-color:#{rgb_to_hex(color_palette[3])}"
    color4_hex = f"style=background-color:#{rgb_to_hex(color_palette[4])}"
    color5_hex = f"style=background-color:#{rgb_to_hex(color_palette[5])}"
    color6_hex = f"style=background-color:#{rgb_to_hex(color_palette[6])}"
    color7_hex = f"style=background-color:#{rgb_to_hex(color_palette[7])}"
    color0_code = f"#{rgb_to_hex(color_palette[0]).upper()}"
    color1_code = f"#{rgb_to_hex(color_palette[1]).upper()}"
    color2_code = f"#{rgb_to_hex(color_palette[2]).upper()}"
    color3_code = f"#{rgb_to_hex(color_palette[3]).upper()}"
    color4_code = f"#{rgb_to_hex(color_palette[4]).upper()}"
    color5_code = f"#{rgb_to_hex(color_palette[5]).upper()}"
    color6_code = f"#{rgb_to_hex(color_palette[6]).upper()}"
    color7_code = f"#{rgb_to_hex(color_palette[7]).upper()}"
    return render_template('index.html', form=file_up_form, color0_hex=color0_hex, color1_hex=color1_hex,
                           color2_hex=color2_hex, color3_hex=color3_hex, color4_hex=color4_hex,
                           color5_hex=color5_hex, color6_hex=color6_hex, color7_hex=color7_hex,
                           color0_code=color0_code, color1_code=color1_code, color2_code=color2_code,
                           color3_code=color3_code, color4_code=color4_code, color5_code=color5_code,
                           color6_code=color6_code, color7_code=color7_code)


if __name__ == '__main__':
    app.run(debug=True)
