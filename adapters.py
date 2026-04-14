"""
Infrastructure Layer - Adapters wrapping external tools.
Keeps upper layers decoupled from specific tools (Git, Maven, pytest, etc.).
Depends on: domain layer only.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional
from domain.entities import CollabSession, User


class VCSAdapter(ABC):
    """Abstract adapter for version control (Git, SVN, etc.)."""

    @abstractmethod
    def initialise(self, project_path: str) -> bool:
        pass

    @abstractmethod
    def commit(self, project_path: str, message: str) -> bool:
        pass

    @abstractmethod
    def get_log(self, project_path: str) -> list[str]:
        pass

    @abstractmethod
    def revert(self, project_path: str, filename: str) -> bool:
        pass


class GitAdapter(VCSAdapter):
    """Concrete adapter wrapping Git."""

    def initialise(self, project_path: str) -> bool:
        pass

    def commit(self, project_path: str, message: str) -> bool:
        pass

    def get_log(self, project_path: str) -> list[str]:
        pass

    def revert(self, project_path: str, filename: str) -> bool:
        pass


class BuildAdapter(ABC):
    """Abstract adapter for build tools (Maven, Gradle, pip, etc.)."""

    @abstractmethod
    def build(self, project_path: str) -> tuple[bool, str]:
        pass

    @abstractmethod
    def clean(self, project_path: str) -> bool:
        pass


class PythonBuildAdapter(BuildAdapter):
    def build(self, project_path: str) -> tuple[bool, str]:
        pass

    def clean(self, project_path: str) -> bool:
        pass


class JavaBuildAdapter(BuildAdapter):
    def build(self, project_path: str) -> tuple[bool, str]:
        pass

    def clean(self, project_path: str) -> bool:
        pass


class TestAdapter(ABC):
    """Abstract adapter for test frameworks (pytest, JUnit, etc.)."""

    @abstractmethod
    def run_tests(self, project_path: str) -> tuple[bool, str]:
        pass


class PytestAdapter(TestAdapter):
    def run_tests(self, project_path: str) -> tuple[bool, str]:
        pass


class JUnitAdapter(TestAdapter):
    def run_tests(self, project_path: str) -> tuple[bool, str]:
        pass


class CollabServer:
    """
    Central server managing collaborative sessions.
    In production this would be a remote service.
    Clients connect via CollabService (assumption 2).
    """

    def __init__(self):
        self._sessions: dict[str, CollabSession] = {}

    def create_session(self, session_id: str, project_name: str) -> CollabSession:
        pass

    def get_session(self, session_id: str) -> Optional[CollabSession]:
        pass

    def end_session(self, session_id: str) -> bool:
        pass

