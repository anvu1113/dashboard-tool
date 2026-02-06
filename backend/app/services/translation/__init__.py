from abc import ABC, abstractmethod
from typing import Optional

class TranslationService(ABC):
    @abstractmethod
    def translate(self, text: str, source: str, target: str) -> str:
        """
        Translate text from source language to target language.
        
        Args:
            text: The text to translate
            source: Source language code (e.g., 'en')
            target: Target language code (e.g., 'vi')
            
        Returns:
            Translated text
        """
        pass

from .argos import ArgosService
from .google import GoogleService

def get_translation_service(engine_id: str = "argos") -> TranslationService:
    if engine_id == "argos":
        return ArgosService()
    # Placeholder for other engines
    # elif engine_id == "google":
    #     return GoogleService()
    
    # Default to Argos if unknown or fallback
    return ArgosService()
