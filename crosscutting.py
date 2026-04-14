"""
Cross-cutting Layer - Concerns that span all layers.
No dependencies on presentation, service, or domain layers.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from enum import Enum


class Theme(Enum):
    LIGHT = "light"
    DARK = "dark"
    HIGH_CONTRAST = "high_contrast"


class AccessibilityConfig:
    """Stores and applies user accessibility preferences globally."""

    def __init__(self):
        self.theme: Theme = Theme.LIGHT
        self.font_size: int = 14
        self.screen_reader_enabled: bool = False

    def set_theme(self, theme: Theme) -> None:
        pass

    def set_font_size(self, size: int) -> None:
        pass

    def enable_screen_reader(self, enabled: bool) -> None:
        pass


class PlatformAbstraction:
    """Provides OS-independent access to platform-level operations."""

    def get_os(self) -> str:
        pass

    def get_home_directory(self) -> str:
        pass

    def open_file_dialog(self) -> str:
        pass

    def show_notification(self, message: str) -> None:
        pass


class LanguagePlugin(ABC):
    """
    Abstract base class for language support plugins.
    New languages are added by subclassing this interface.
    """

    @property
    @abstractmethod
    def language_name(self) -> str:
        pass

    @property
    @abstractmethod
    def file_extensions(self) -> list[str]:
        pass

    @abstractmethod
    def get_keywords(self) -> list[str]:
        pass

    @abstractmethod
    def get_completions(self, context: str) -> list[str]:
        pass

    @abstractmethod
    def run_linter(self, code: str) -> list[str]:
        pass


class PythonPlugin(LanguagePlugin):
    """Language plugin providing Python support."""

    @property
    def language_name(self) -> str:
        pass

    @property
    def file_extensions(self) -> list[str]:
        pass

    def get_keywords(self) -> list[str]:
        pass

    def get_completions(self, context: str) -> list[str]:
        pass

    def run_linter(self, code: str) -> list[str]:
        pass


class JavaPlugin(LanguagePlugin):
    """Language plugin providing Java support."""

    @property
    def language_name(self) -> str:
        pass

    @property
    def file_extensions(self) -> list[str]:
        pass

    def get_keywords(self) -> list[str]:
        pass

    def get_completions(self, context: str) -> list[str]:
        pass

    def run_linter(self, code: str) -> list[str]:
        pass
