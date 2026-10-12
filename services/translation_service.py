"""
Translation Service - Handles multilingual support for KisanCare.
Supports: English, Hindi, Marathi
"""

# Translation dictionary with all UI strings, disease names, crops, etc.
# All values are manually curated — DO NOT replace with machine-translation API output.
TRANSLATIONS = {
    # ── Navigation & UI ────────────────────────────────────────────────────────
    'home':              {'en': 'Home',              'hi': 'होम',               'mr': 'होम'},
    'dashboard':         {'en': 'Dashboard',         'hi': 'डैशबोर्ड',         'mr': 'डॅशबोर्ड'},
    'predict_disease':   {'en': 'Disease Prediction','hi': 'रोग पहचान',        'mr': 'रोग ओळख'},
    'about':             {'en': 'About',             'hi': 'परिचय',            'mr': 'आमच्याबद्दल'},
    'features':          {'en': 'Features',          'hi': 'सुविधाएं',         'mr': 'वैशिष्ट्ये'},
    'languages_supported': {'en': 'Languages Supported', 'hi': 'समर्थित भाषाएं', 'mr': 'समर्थित भाषा'},

    # ── Common buttons & actions ───────────────────────────────────────────────
    'submit':            {'en': 'Submit',            'hi': 'जमा करें',         'mr': 'सबमिट करा'},
    'cancel':            {'en': 'Cancel',            'hi': 'रद्द करें',        'mr': 'रद्द करा'},
    'back':              {'en': 'Back',              'hi': 'वापस',             'mr': 'परत'},
    'get_started':       {'en': 'Get Started',       'hi': 'शुरू करें',        'mr': 'सुरू करा'},

    # ── Disease Prediction ─────────────────────────────────────────────────────
    'select_crop':       {'en': 'Select Crop',       'hi': 'फसल चुनें',        'mr': 'पीक निवडा'},
    'upload_image':      {'en': 'Upload Leaf Image', 'hi': 'पत्ती की छवि अपलोड करें', 'mr': 'पानाची प्रतिमा अपलोड करा'},
    'click_or_drag':     {'en': 'Click or drag image here', 'hi': 'यहाँ क्लिक करें या छवि ड्रैग करें', 'mr': 'येथे क्लिक करा किंवा प्रतिमा ड्रॅग करा'},
    'predict':           {'en': 'Predict Disease',   'hi': 'रोग की पहचान करें', 'mr': 'रोग ओळखा'},
    'prediction_result': {'en': 'Prediction Result', 'hi': 'पहचान परिणाम',     'mr': 'ओळख निकाल'},
    'crop':              {'en': 'Crop',              'hi': 'फसल',              'mr': 'पीक'},
    'disease':           {'en': 'Disease',           'hi': 'रोग',              'mr': 'रोग'},
    'confidence':        {'en': 'Confidence',        'hi': 'विश्वसनीयता',      'mr': 'आत्मविश्वास'},
    'treatment':         {'en': 'Treatment',         'hi': 'उपचार',            'mr': 'उपचार'},

    # ── Dashboard / Stats labels ───────────────────────────────────────────────
    'diseases_detected': {'en': 'Diseases Detected', 'hi': 'रोग पहचाने गए',   'mr': 'रोग ओळखले'},
    'crops_supported':   {'en': 'Crops Supported',   'hi': 'समर्थित फसलें',   'mr': 'समर्थित पिके'},
    'languages':         {'en': 'Languages',         'hi': 'भाषाएं',           'mr': 'भाषा'},
    'accuracy':          {'en': 'Model Accuracy',    'hi': 'मॉडल की सटीकता', 'mr': 'मॉडलची अचूकता'},
    'how_it_works':      {'en': 'How It Works',      'hi': 'यह कैसे काम करता है', 'mr': 'हे कसे कार्य करते'},
    'real_time':         {'en': 'Real-time',         'hi': 'रीयल-टाइम',        'mr': 'रीअल-टाइम'},

    # ── Fertilizer ────────────────────────────────────────────────────────────
    'organic':           {'en': 'Organic',           'hi': 'जैविक',            'mr': 'जैविक'},
    'chemical':          {'en': 'Chemical',          'hi': 'रासायनिक',         'mr': 'रासायनिक'},
    'dosage':            {'en': 'Dosage',            'hi': 'मात्रा',           'mr': 'मात्रा'},
    'application':       {'en': 'Application',       'hi': 'प्रयोग',           'mr': 'वापर'},

    # ── Crop names ────────────────────────────────────────────────────────────
    'banana':            {'en': 'Banana',            'hi': 'केला',             'mr': 'केळ'},
    'corn':              {'en': 'Corn',              'hi': 'मक्का',            'mr': 'मका'},
    'cotton':            {'en': 'Cotton',            'hi': 'कपास',             'mr': 'कापूस'},
    'rice':              {'en': 'Rice',              'hi': 'धान',              'mr': 'तांदूळ'},
    'wheat':             {'en': 'Wheat',             'hi': 'गेहूं',            'mr': 'गहू'},

    # ── Messages ──────────────────────────────────────────────────────────────
    'success':           {'en': 'Success',           'hi': 'सफलता',            'mr': 'यश'},
    'error':             {'en': 'Error',             'hi': 'त्रुटि',           'mr': 'त्रुटी'},
    'loading':           {'en': 'Loading...',        'hi': 'लोड हो रहा है...',  'mr': 'लोड होत आहे...'},
    'no_data':           {'en': 'No Data Available', 'hi': 'कोई डेटा उपलब्ध नहीं', 'mr': 'कोणताही डेटा उपलब्ध नाही'},
}


class TranslationService:
    """Service for managing multilingual translations."""
    
    @staticmethod
    def get_translation(key, language='en', default=None):
        """
        Get translation for a key in specified language.
        
        Args:
            key: Translation key
            language: Language code (en, hi, mr)
            default: Default value if key not found
        
        Returns:
            Translated string or default value
        """
        if key in TRANSLATIONS:
            return TRANSLATIONS[key].get(language, TRANSLATIONS[key].get('en', default or key))
        return default or key
    
    @staticmethod
    def get_all_translations(language='en'):
        """
        Get all translations for a specific language.
        
        Args:
            language: Language code (en, hi, mr)
        
        Returns:
            Dictionary of all translations for the language
        """
        result = {}
        for key, translations in TRANSLATIONS.items():
            result[key] = translations.get(language, translations.get('en', key))
        return result
    
    @staticmethod
    def translate_dict(data, language='en'):
        """
        Translate dictionary values if they are translation keys.
        
        Args:
            data: Dictionary to translate
            language: Target language
        
        Returns:
            Translated dictionary
        """
        result = {}
        for key, value in data.items():
            if isinstance(value, dict) and all(k in ['en', 'hi', 'mr'] for k in value.keys()):
                result[key] = value.get(language, value.get('en', key))
            else:
                result[key] = value
        return result
