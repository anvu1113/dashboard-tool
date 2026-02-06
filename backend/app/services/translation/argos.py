from . import TranslationService
from app.core.exceptions import LanguageNotSupportedException
import argostranslate.package
import argostranslate.translate
import os

class ArgosService(TranslationService):
    def __init__(self):
        # Initialize or ensure models are loaded
        # Note: In a real production env, models should be pre-loaded at startup
        # to avoid concurrency issues or latency on first request.
        # For this implementation, we assume models act as a global registry in the library.
        pass

    def normalize_code(self, code: str) -> str:
        # Simple normalization: 'zh-CN' -> 'zh'
        if '-' in code:
            return code.split('-')[0]
        return code

    def translate(self, text: str, source: str, target: str) -> str:
        try:
            # Normalize codes
            source = self.normalize_code(source)
            target = self.normalize_code(target)

            # Check if language pair is installed
            installed_languages = argostranslate.translate.get_installed_languages()
            from_lang = next((x for x in installed_languages if x.code == source), None)
            to_lang = next((x for x in installed_languages if x.code == target), None)
            
            if not from_lang or not to_lang:
                 available_codes = [x.code for x in installed_languages]
                 raise LanguageNotSupportedException(f"Language pair {source}->{target} is not installed. Available: {available_codes}")

            # Try Direct Translation
            translation = from_lang.get_translation(to_lang)
            if translation:
                return translation.translate(text)
            
            # Try Pivot via English (if source/target is not English)
            if source != 'en' and target != 'en':
                en_lang = next((x for x in installed_languages if x.code == 'en'), None)
                if en_lang:
                    # Check source -> en
                    to_en = from_lang.get_translation(en_lang)
                    # Check en -> target
                    from_en = en_lang.get_translation(to_lang)
                    
                    if to_en and from_en:
                        # Perform pivot translation
                        intermediate = to_en.translate(text)
                        return from_en.translate(intermediate)

            raise LanguageNotSupportedException(f"Translation model from {source} to {target} not available (Direct or Pivot).")
        except Exception as e:
            print(f"Argos Translation Error: {e}")
            raise e

    @staticmethod
    def install_language(from_code: str, to_code: str):
        """
        Helper to install language packages dynamically.
        This updates the package index and downloads the package.
        """
        argostranslate.package.update_package_index()
        available_packages = argostranslate.package.get_available_packages()
        package_to_install = next(
            filter(
                lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
            ), None
        )
        if package_to_install:
             argostranslate.package.install_from_path(package_to_install.download())
             print(f"Installed Argos package: {from_code} -> {to_code}")
