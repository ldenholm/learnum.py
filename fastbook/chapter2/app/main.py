from flask import Flask, render_template, send_from_directory, url_for
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileField, FileAllowed
from wtforms import SubmitField
from fastai.vision.all import *
import os


basedir = os.getcwd()
filename = "export.pkl"
path = os.path.join(basedir, filename)
print('debug path', path)
learn_inf = load_learner(path)
learn_inf.dls.vocab

app = Flask (__name__)
app.config['SECRET_KEY'] = "blahblahhardcodedlol"
app.config['UPLOADED_PHOTOS_DEST'] = 'uploads'

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

class UploadForm(FlaskForm):
    photo = FileField(
        validators = [
            FileAllowed(photos, 'Only images are allowed'),
            FileRequired('File field should not be empty')
        ]
    )
    submit = SubmitField('Upload')

@app.route('/uploads/<filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], filename)

@app.route('/', methods=['GET', 'POST'])
def uploadImage():
    form = UploadForm()
    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        file_url = url_for('get_file', filename=filename)
        pred, probs = on_upload_classify(filename)
    else:
        file_url = None
    return render_template('index.html', form=form, file_url=file_url, pred=pred, probs=probs)

def on_upload_classify(filename):
    img = PILImage.create(f'uploads/{filename}')
    print(f"uploads/{filename}")
    pred, pred_idx, probs = learn_inf.predict(img)
    print(pred, pred_idx, probs)
    return (pred, probs)

if __name__ == '__main__':
    app.run(debug=True)