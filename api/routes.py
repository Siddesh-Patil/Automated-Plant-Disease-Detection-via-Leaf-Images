"""
Automated Plant Disease Detection via Leaf Images - API Routes
Flask Blueprint with core application routes.
Includes: Main Page, Disease Prediction endpoints.
"""
import os
import json
from flask import Blueprint, render_template, request, jsonify, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from flask import current_app

# Import services
from services.translation_service import TranslationService
from model.predict import predict

# Create blueprint
bp = Blueprint('main', __name__)

# Initialize services
translation_svc = TranslationService()

# Configuration from existing app
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "bmp"}

CATEGORY_LABELS = {
    "banana": ["Black Sigatoka", "Bract Mosiac Virus", "Healthy", "Insect Pest Disease", "Moko Disease", "Panama Disease", "Yellow Sigatoka"],
    "corn": ["Blight", "Common Rust", "Gray Leaf Spot", "Healthy"],
    "cotton": ["Bacterial Blight", "Curl Virus", "Fussarium Wilt", "Healthy"],
    "rice": ["Bacterial Blight", "Bacterial Leaf Blight", "Brown Spot", "Healthy", "Leaf Blast", "Leaf Scald", "Leaf Smut", "Narrow Brown Spot"],
    "wheat": ["Black Point", "Fusarium Foot Rot", "Healthy", "Leaf Blight", "Wheat Blast"]
}

TREATMENT_GUIDE = {
    "banana": {
        "Black Sigatoka": "Spray Mancozeb 0.2% or Carbendazim every 7–10 days.",
        "Bract Mosiac Virus": "Use virus-free planting material; control vectors.",
        "Healthy": "No treatment needed.",
        "Insect Pest Disease": "Apply neem-based insecticides or Imidacloprid.",
        "Moko Disease": "Remove infected plants and disinfect tools.",
        "Panama Disease": "Use resistant cultivars and improve soil drainage.",
        "Yellow Sigatoka": "Use Propiconazole-based fungicides."
    },
    "corn": {
        "Blight": "Apply fungicide containing Chlorothalonil or Mancozeb.",
        "Common Rust": "Use resistant varieties; spray Mancozeb if severe.",
        "Gray Leaf Spot": "Apply fungicides like Azoxystrobin at early symptoms.",
        "Healthy": "No treatment needed."
    },
    "cotton": {
        "Bacterial Blight": "Use copper fungicides and resistant seeds.",
        "Curl Virus": "Control whiteflies; use Imidacloprid sprays.",
        "Fussarium Wilt": "Improve drainage and avoid monoculture.",
        "Healthy": "No treatment needed."
    },
    "rice": {
        "Bacterial Blight": "Use copper-based bactericides and maintain field hygiene.",
        "Bacterial Leaf Blight": "Apply Streptocycline and maintain field sanitation.",
        "Brown Spot": "Use fungicides like Tricyclazole and apply balanced fertilization.",
        "Healthy": "No treatment needed.",
        "Leaf Blast": "Spray Tricyclazole and maintain proper plant spacing.",
        "Leaf Scald": "Use Mancozeb or Thiophanate-methyl; ensure good drainage.",
        "Leaf Smut": "No chemical control available; remove infected leaves manually.",
        "Narrow Brown Spot": "Apply Propiconazole and supplement with potassium-rich fertilizers."
    },
    "wheat": {
        "Black Point": "Avoid excessive irrigation near harvesting.",
        "Fusarium Foot Rot": "Improve drainage and crop rotation.",
        "Healthy": "No treatment needed.",
        "Leaf Blight": "Use Mancozeb or Chlorothalonil sprays.",
        "Wheat Blast": "Use tolerant varieties and seed treatment with fungicides."
    }
}

def allowed_file(filename):
    """Check if file extension is allowed."""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# ============================================================================
# MAIN PAGE ROUTE
# ============================================================================

@bp.route('/')
@bp.route('/dashboard')
def dashboard():
    """Main page."""
    lang = request.args.get('lang', 'en')
    trans = translation_svc.get_all_translations(lang)
    
    features = {
        'diseases': len(CATEGORY_LABELS),
        'crops': len(CATEGORY_LABELS)
    }
    
    return render_template('dashboard.html', 
                         lang=lang, 
                         trans=trans,
                         features=features)


# ============================================================================
# ABOUT PAGE ROUTE
# ============================================================================

@bp.route('/about')
def about():
    """About page with project info, flowchart and tech stack."""
    lang = request.args.get('lang', 'en')
    trans = translation_svc.get_all_translations(lang)
    return render_template('about.html', lang=lang, trans=trans)


# ============================================================================
# DISEASE PREDICTION
# ============================================================================

@bp.route('/predict', methods=['GET', 'POST'])
def predict_disease():
    """Predict crop disease from leaf image."""
    lang = request.args.get('lang', 'en')
    trans = translation_svc.get_all_translations(lang)
    is_ajax_request = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        category = request.form.get('category', '')
        
        if not file or not category:
            return jsonify({'error': 'Missing file or category'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'Invalid file format'}), 400
        
        try:
            filename = secure_filename(file.filename)
            filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Get prediction
            model_path = os.path.join('model', category, 'model.pt')
            class_names = CATEGORY_LABELS.get(category)
            
            if not class_names or not os.path.exists(model_path):
                return jsonify({'error': 'Model not found for category'}), 404
            
            label, confidence = predict(filepath, model_path, class_names)
            treatment = TREATMENT_GUIDE.get(category, {}).get(label, 'Consult agronomist')
            


            template_name = 'predict_result.html' if is_ajax_request else 'predict.html'
            return render_template(
                template_name,
                category=category,
                label=label,
                confidence=f"{confidence:.2f}",
                image_filename=filename,
                treatment=treatment,
                lang=lang,
                trans=trans
            )
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    return render_template('predict.html', 
                         lang=lang, 
                         trans=trans,
                         crops=CATEGORY_LABELS.keys())


@bp.route('/uploads/<filename>')
def uploaded_file(filename):
    """Serve uploaded files."""
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)


# ============================================================================
# TRANSLATION API
# ============================================================================

@bp.route('/api/translate')
def api_translate():
    """API endpoint for translations."""
    key = request.args.get('key', '')
    lang = request.args.get('lang', 'en')
    
    translation = translation_svc.get_translation(key, lang)
    
    return jsonify({
        'key': key,
        'language': lang,
        'translation': translation
    })


@bp.route('/api/translations/<lang>')
def api_translations(lang):
    """Get all translations for a language."""
    translations = translation_svc.get_all_translations(lang)
    return jsonify(translations)


# ============================================================================
# UTILITY ROUTES
# ============================================================================

@bp.route('/api/health')
def health_check():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'services': {
            'translation': 'active',
            'disease_prediction': 'active'
        }
    })


@bp.route('/api/info')
def app_info():
    """Application information endpoint."""
    return jsonify({
        'name': 'Automated Plant Disease Detection via Leaf Images',
        'version': '1.0.0',
        'description': 'AI-powered plant disease detection from leaf images',
        'crops_supported': list(CATEGORY_LABELS.keys()),
        'languages_supported': ['en', 'hi', 'mr'],
        'features': [
            'Disease Prediction'
        ]
    })


# ============================================================================
# HOME/INDEX ROUTE (Existing compatibility)
# ============================================================================

@bp.route('/index')
def index_compat():
    """Compatibility route for existing index."""
    return redirect(url_for('main.dashboard'))
