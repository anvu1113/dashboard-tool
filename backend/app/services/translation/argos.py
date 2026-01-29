from . import TranslationService
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

    def translate(self, text: str, source: str, target: str) -> str:
        try:
            # Argos Translate requires language packages to be installed.
            # We assume "en" -> "vi" and "vi" -> "en" are common.
            # This simplistic implementation trusts the library's global state.
            
            # Check if language pair is installed, if not, try to install (Be careful with this in prod)
            # For robustness, we should have a separate 'install_languages' step.
            
            return argostranslate.translate.translate(text, source, target)
        except Exception as e:
            print(f"Argos Translation Error: {e}")
            # Fallback or re-raise
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
