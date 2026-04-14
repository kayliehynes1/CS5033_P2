"""
Service Layer - Business logic coordinators.
Depends on: domain layer, infrastructure layer, crosscutting layer.
No direct access to presentation layer.
"""

from __future__ import annotations
from typing import Optional
from domain.entities import (
    Project, SourceFile, DesignDoc, DiagnosticResult,
    CollabSession, User, Language
)
from infrastructure.adapters import (
    BuildAdapter, TestAdapter, CollabServer
)
from crosscutting.crosscutting import LanguagePlugin


class FileService:
    """Opens, saves, and organises project files on the local filesystem."""

    def load_project(self, root_path: str) -> Project:
        pass

    def save_file(self, project: Project, filename: str) -> bool:
        pass

    def create_file(self, project: Project, filename: str, language: Language) -> SourceFile:
        pass

    def delete_file(self, project: Project, filename: str) -> bool:
        pass

    def list_project_files(self, project: Project) -> list[str]:
        pass


class CodeService:
    """Provides syntax highlighting and code completion for open files."""

    def __init__(self, plugins: list[LanguagePlugin]):
        self._plugins: dict[str, LanguagePlugin] = {}
        # maps file extension -> plugin

    def get_keywords(self, filename: str) -> list[str]:
        pass

    def get_completions(self, filename: str, context: str) -> list[str]:
        pass

    def highlight(self, source_file: SourceFile) -> dict[int, list[str]]:
        """Returns a line-by-line token map for the editor to render."""
        pass


class BuildRunService:
    """
    Coordinates build, run, test, and debug operations.
    Stops at build and test — no deployment (assumption 7).
    """

    def __init__(
        self,
        build_adapters: dict[Language, BuildAdapter],
        test_adapters: dict[Language, TestAdapter],
    ):
        self._build_adapters = build_adapters
        self._test_adapters = test_adapters

    def build(self, project: Project) -> tuple[bool, str]:
        pass

    def run(self, project: Project, entry_point: str) -> tuple[bool, str]:
        pass

    def run_tests(self, project: Project) -> tuple[bool, str]:
        pass

    def debug(self, project: Project, entry_point: str, breakpoints: list[int]) -> None:
        pass


class AnalysisService:
    """Runs static and dynamic analysis over source files."""

    def __init__(self, plugins: list[LanguagePlugin]):
        self._plugins: dict[str, LanguagePlugin] = {}

    def run_static_analysis(self, source_file: SourceFile) -> list[DiagnosticResult]:
        pass

    def run_dynamic_analysis(self, source_file: SourceFile) -> list[DiagnosticResult]:
        pass

    def analyse_design_doc(self, doc: DesignDoc, project: Project) -> list[str]:
        """Check a design document for consistency with source files."""
        pass


class DesignDocService:
    """Creates, updates, and traces design documents within a project."""

    def __init__(self, file_service: FileService):
        self._file_service = file_service

    def create_doc(self, project: Project, filename: str) -> DesignDoc:
        pass

    def update_doc(self, project: Project, filename: str, new_content: str) -> bool:
        pass

    def get_doc(self, project: Project, filename: str) -> Optional[DesignDoc]:
        pass

    def list_docs(self, project: Project) -> list[str]:
        pass

    def trace_to_source(self, doc: DesignDoc, project: Project) -> dict[str, list[str]]:
        """Maps design document references to corresponding source file elements."""
        pass


class CollabService:
    """
    Manages real-time collaborative editing sessions.
    Requires internet (assumption 1).
    Enforces single-editor locking per file (assumption 6).
    Delegates session state to CollabServer (assumption 2).
    """

    def __init__(self):
        self._server: CollabServer = CollabServer()
        self._current_session: Optional[CollabSession] = None

    def is_online(self) -> bool:
        pass

    def start_session(self, project: Project, host: User) -> Optional[CollabSession]:
        pass

    def join_session(self, session_id: str, user: User) -> Optional[CollabSession]:
        pass

    def leave_session(self, user: User) -> None:
        pass

    def request_edit_lock(self, filename: str, username: str) -> bool:
        """Returns True if lock granted, False if another user holds it."""
        pass

    def release_edit_lock(self, filename: str, username: str) -> bool:
        pass

