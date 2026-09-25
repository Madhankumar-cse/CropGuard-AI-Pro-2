from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title='CropGuard AI')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get('/')
async def home():
    return {'message':'CropGuard AI API Running'}

@app.post('/predict')
async def predict(file: UploadFile = File(...)):
    return {
        'crop':'Tomato',
        'disease':'Late Blight',
        'confidence':'97.8%',
        'severity':'High',
        'treatment':'Apply Copper Fungicide immediately.',
        'prevention':'Avoid overhead watering.'
    }
