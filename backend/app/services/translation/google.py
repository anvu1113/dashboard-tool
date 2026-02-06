from . import TranslationService
from deep_translator import GoogleTranslator
import time

class GoogleService(TranslationService):
    def translate(self, text: str, source: str, target: str) -> str:
        """
        Translates using Google Translate (via deep_translator).
        Normalization:
        - Argos uses 'zh' for Chinese.
        - Google often expects 'zh-CN' or 'zh-TW'.
        - deep_translator usually handles 'zh' as Simplified.
        """
        try:
            # Map common codes if necessary. 
            # 'vi' -> 'vi', 'en' -> 'en' are standard.
            # 'zh' -> 'zh-CN' for Google might be safer if 'zh' implies simplified.
            # Normalize zh codes
            if target.lower() in ['zh', 'zh-cn']:
                target = 'zh-CN'
            if source.lower() in ['zh', 'zh-cn']:
                source = 'zh-CN'
            
            # Use deep_translator
            # source='auto' is safer if unsure, but we usually know source
            translator = GoogleTranslator(source=source, target=target)
            result = translator.translate(text)
            return result
        except Exception as e:
            print(f"Google Translation Error: {e}")
            raise e
