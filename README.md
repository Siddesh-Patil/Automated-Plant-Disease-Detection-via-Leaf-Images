# 🌿 Automated Plant Disease Detection via Leaf Images

An AI-powered web application that detects plant diseases from leaf images using deep learning. Upload a leaf photo, select the crop type, and get an instant disease diagnosis along with treatment recommendations — available in English, Hindi, and Marathi.

---

## 📸 Demo

| Dashboard | Disease Detection |
|-----------|------------------|
| Upload a leaf image | Get instant diagnosis + treatment |

---

## ✨ Features

- 🔬 **Disease Detection** — CNN-based (EfficientNet B3) plant disease classification using PyTorch
- 🌾 **5 Crops Supported** — Banana, Corn, Cotton, Rice, Wheat
- 💊 **Treatment Recommendations** — Actionable treatment guide for each detected disease
- 🗣️ **Multilingual UI** — Supports English, Hindi (`hi`), and Marathi (`mr`)
- 🎨 **Dark / Light Theme** — Toggle with persistent local preference
- 📱 **Responsive Design** — Works on desktop, tablet, and mobile
- ⚡ **Fast & Lightweight** — Flask backend with clean Blueprint architecture

---

## 🦠 Supported Crops & Diseases

| Crop | Diseases Detected |
|------|-------------------|
| 🍌 **Banana** | Black Sigatoka, Bract Mosaic Virus, Insect Pest Disease, Moko Disease, Panama Disease, Yellow Sigatoka, Healthy |
| 🌽 **Corn** | Blight, Common Rust, Gray Leaf Spot, Healthy |
| 🌿 **Cotton** | Bacterial Blight, Curl Virus, Fusarium Wilt, Healthy |
| 🍚 **Rice** | Bacterial Blight, Bacterial Leaf Blight, Brown Spot, Leaf Blast, Leaf Scald, Leaf Smut, Narrow Brown Spot, Healthy |
| 🌾 **Wheat** | Black Point, Fusarium Foot Rot, Leaf Blight, Wheat Blast, Healthy |

---

## 🧠 Model Information

| Property | Details |
|----------|---------|
| Architecture | EfficientNet B3 |
| Pretrained Weights | ImageNet |
| Input Size | 300 × 300 RGB |
| Framework | PyTorch |
| Output | Disease class + Confidence score |

> **Note:** Model weights (`model/*.pt`) are not included in this repository due to size. Download separately and place them in the `model/<crop>/model.pt` path.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

**1. Clone the repository:**
```bash
git clone https://github.com/Siddesh-Patil/Automated-Plant-Disease-Detection-via-Leaf-Images.git
cd Automated-Plant-Disease-Detection-via-Leaf-Images
```

**2. Create and activate a virtual environment:**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

**4. Set up environment variables:**
```bash
# Windows
copy .env.example .env

# macOS / Linux
cp .env.example .env
```

**5. Add model weights:**

Place your trained model files in:
```
model/
├── banana/model.pt
├── corn/model.pt
├── cotton/model.pt
├── rice/model.pt
└── wheat/model.pt
```

**6. Run the application:**
```bash
python app.py
```

Open your browser at: **`http://localhost:5000`**

---

## 📁 Project Structure

```
Automated-Plant-Disease-Detection-via-Leaf-Images/
│
├── app.py                        # Entry point
├── app_new.py                    # Application factory (create_app)
├── config.py                     # Configuration settings
├── requirements.txt              # Python dependencies
├── .env.example                  # Environment variable template
├── .gitignore                    # Git ignore rules
│
├── api/
│   ├── __init__.py
│   └── routes.py                 # All Flask routes (Blueprint)
│
├── services/
│   ├── __init__.py
│   └── translation_service.py   # Multilingual support (EN / HI / MR)
│
├── model/
│   ├── predict.py                # Inference logic
│   ├── train.py                  # Model training script
│   └── <crop>/model.pt          # Trained weights (not in repo)
│
├── templates/
│   ├── base.html                 # Master layout
│   ├── dashboard.html            # Home/dashboard page
│   ├── predict.html              # Upload & predict page
│   ├── predict_result.html       # Results display
│   ├── about.html                # About the project
│   ├── 404.html                  # Not found error page
│   └── 500.html                  # Server error page
│
├── static/
│   ├── css/
│   │   ├── styles.css            # Main stylesheet
│   │   └── themes.css            # Dark/light theme styles
│   └── js/
│       ├── main.js               # Core application logic
│       └── scripts.js            # Additional scripts
│
└── uploads/                      # Temporary image upload storage
```

---

## 🔌 API Endpoints

### Pages
| Method | Route | Description |
|--------|-------|-------------|
| GET | `/` | Home / Dashboard |
| GET | `/dashboard` | Dashboard |
| GET | `/about` | About page |
| GET | `/predict` | Disease prediction form |
| POST | `/predict` | Submit image for prediction |

### REST API
| Method | Route | Description |
|--------|-------|-------------|
| GET | `/api/health` | Health check |
| GET | `/api/info` | App info & supported crops |
| GET | `/api/translate?key=&lang=` | Single key translation |
| GET | `/api/translations/<lang>` | All translations for a language |
| GET | `/uploads/<filename>` | Serve uploaded image |

---

## 🌐 Multilingual Support

The app supports 3 languages selectable from the navbar or via URL:

| Language | Code | URL Example |
|----------|------|-------------|
| English | `en` | `/?lang=en` |
| Hindi | `hi` | `/?lang=hi` |
| Marathi | `mr` | `/?lang=mr` |

---

## ⚙️ Environment Variables

Create a `.env` file based on `.env.example`:

```env
# Flask
FLASK_ENV=development
FLASK_PORT=5000
DEBUG=True
SECRET_KEY=your-secret-key-here

# Upload settings
UPLOAD_FOLDER=uploads
MAX_CONTENT_LENGTH=16777216  # 16MB max upload size
```

---

## 🛠️ Troubleshooting

**Port already in use:**
```bash
FLASK_PORT=5001 python app.py
```

**Module not found:**
```bash
# Make sure virtual environment is activated, then:
pip install -r requirements.txt
```

**Model not found error:**
- Ensure `model/<crop>/model.pt` exists for the selected crop
- Model files are not included in the repo — add them manually

**Uploaded image not showing:**
- Make sure the `uploads/` directory exists (created automatically on first run)
- Clear browser cache with `Ctrl + F5`

---

## 🔮 Future Enhancements

- [ ] User authentication & prediction history
- [ ] Database integration (SQLAlchemy)
- [ ] Additional crops (Tomato, Potato, Soybean)
- [ ] REST API with JWT authentication
- [ ] Mobile app (React Native / Flutter)
- [ ] Real-time camera capture support
- [ ] Offline mode with model export (ONNX / TFLite)

---

## 🧰 Tech Stack

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.3-000000?logo=flask&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-EE4C2C?logo=pytorch&logoColor=white)
![EfficientNet](https://img.shields.io/badge/EfficientNet-B3-orange)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)

---

## 📝 License

This project is for **educational purposes** as part of an academic submission.

---

## 👤 Author

**Siddesh Patil**
🔗 [GitHub](https://github.com/Siddesh-Patil)

---

*Made with ❤️ for Smart Agriculture*
