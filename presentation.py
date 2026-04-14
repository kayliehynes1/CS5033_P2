"""
Presentation Layer - UI components.
Delegates all business logic to the service layer.
No direct access to domain, infrastructure, or crosscutting layers.
"""

from __future__ import annotations
from typing import Optional
from domain.entities import Project, SourceFile, DesignDoc, DiagnosticResult, User
from service.services import (
    CodeService, FileService, BuildRunService,
    AnalysisService, DesignDocService, CollabService,
)
from crosscutting.crosscutting import AccessibilityConfig


class EditorPane:
    """
    Main code editor panel.
    Handles syntax highlighting, code completion, and file editing.
    Requests a collab lock before allowing edits (assumption 6).
    """

    def __init__(self, code_service: CodeService, collab_service: CollabService):
        self._code_service = code_service
        self._collab_service = collab_service
        self._open_file: Optional[SourceFile] = None
        self._current_user: Optional[str] = None

    def open_file(self, source_file: SourceFile, username: str) -> bool:
        pass

    def close_file(self) -> None:
        pass

    def edit(self, new_content: str) -> bool:
        pass

    def get_completions(self, context: str) -> list[str]:
        pass

    def display(self) -> None:
        pass


class ProjectExplorer:
    """File tree panel. Lets users browse and select project files."""

    def __init__(self, file_service: FileService):
        self._file_service = file_service
        self._project: Optional[Project] = None

    def load_project(self, project: Project) -> None:
        pass

    def list_files(self) -> list[str]:
        pass

    def select_file(self, filename: str) -> Optional[SourceFile]:
        pass

    def display(self) -> None:
        pass


class AnalysisPanel:
    """Displays static and dynamic diagnostic results."""

    def __init__(self, analysis_service: AnalysisService):
        self._analysis_service = analysis_service
        self._results: list[DiagnosticResult] = []

    def run_static(self, source_file: SourceFile) -> None:
        pass

    def run_dynamic(self, source_file: SourceFile) -> None:
        pass

    def display(self) -> None:
        pass


class DesignDocView:
    """Panel for creating, editing, and tracing design documents."""

    def __init__(self, design_doc_service: DesignDocService):
        self._service = design_doc_service
        self._open_doc: Optional[DesignDoc] = None

    def open_doc(self, project: Project, filename: str) -> None:
        pass

    def edit_doc(self, project: Project, filename: str, new_content: str) -> None:
        pass

    def trace_to_source(self, project: Project) -> None:
        pass

    def display(self) -> None:
        pass


class HelpPanel:
    """In-IDE help and feature guidance."""

    def search(self, query: str) -> str:
        pass

    def display(self) -> None:
        pass


class WorkspaceUI:
    """
    Top-level UI container.
    Manages multiple open projects and hosts all panels.
    """

    def __init__(
        self,
        code_service: CodeService,
        file_service: FileService,
        build_service: BuildRunService,
        analysis_service: AnalysisService,
        design_doc_service: DesignDocService,
        collab_service: CollabService,
        accessibility: AccessibilityConfig,
    ):
        self._file_service = file_service
        self._build_service = build_service
        self._collab_service = collab_service
        self._accessibility = accessibility
        self._open_projects: dict[str, Project] = {}
        self._active_project: Optional[Project] = None

        # Panels
        self.editor = EditorPane(code_service, collab_service)
        self.explorer = ProjectExplorer(file_service)
        self.analysis_panel = AnalysisPanel(analysis_service)
        self.design_doc_view = DesignDocView(design_doc_service)
        self.help_panel = HelpPanel()

    def open_project(self, root_path: str) -> Project:
        pass

    def switch_project(self, project_name: str) -> bool:
        pass

    def build_active_project(self) -> None:
        pass

    def launch(self) -> None:
        pass

