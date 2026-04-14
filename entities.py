"""
Domain Layer - Core entities.
No dependencies on any other layer.
"""

from __future__ import annotations
from enum import Enum
from typing import Optional


class Language(Enum):
    PYTHON = "python"
    JAVA = "java"


class Severity(Enum):
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"


class UserRole(Enum):
    DEVELOPER = "developer"
    ARCHITECT = "architect"


class User:
    def __init__(self, user_id: str, username: str, role: UserRole):
        self.user_id = user_id
        self.username = username
        self.role = role


class SourceFile:
    def __init__(self, filename: str, language: Language):
        self.filename = filename
        self.language = language
        self.content: str = ""
        self.is_locked: bool = False
        self.locked_by: Optional[str] = None

    def lock(self, username: str) -> bool:
        pass

    def unlock(self, username: str) -> bool:
        pass

    def update_content(self, new_content: str, username: str) -> bool:
        pass


class DesignDoc:
    def __init__(self, filename: str):
        self.filename = filename
        self.content: str = ""

    def update(self, new_content: str) -> None:
        pass


class DiagnosticResult:
    def __init__(self, source_file: str, line_number: int, severity: Severity, message: str):
        self.source_file = source_file
        self.line_number = line_number
        self.severity = severity
        self.message = message


class Project:
    def __init__(self, name: str, root_path: str):
        self.name = name
        self.root_path = root_path
        self.source_files: dict[str, SourceFile] = {}
        self.design_docs: dict[str, DesignDoc] = {}

    def add_source_file(self, source_file: SourceFile) -> None:
        pass

    def add_design_doc(self, design_doc: DesignDoc) -> None:
        pass

    def get_source_file(self, filename: str) -> Optional[SourceFile]:
        pass

    def get_design_doc(self, filename: str) -> Optional[DesignDoc]:
        pass

    def list_files(self) -> list[str]:
        pass


class CollabSession:
    def __init__(self, session_id: str, project_name: str):
        self.session_id = session_id
        self.project_name = project_name
        self.participants: list[User] = []
        self.active_locks: dict[str, str] = {}  # filename -> username

    def join(self, user: User) -> None:
        pass

    def leave(self, user: User) -> None:
        pass

    def request_lock(self, filename: str, username: str) -> bool:
        pass

    def release_lock(self, filename: str, username: str) -> bool:
        pass

