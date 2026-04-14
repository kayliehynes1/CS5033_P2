"""
Entry point.
Wires together all layers and launches the IDE.
"""

from crosscutting.crosscutting import AccessibilityConfig, PythonPlugin, JavaPlugin
from service.services import (
    FileService, CodeService, BuildRunService,
    AnalysisService, DesignDocService, CollabService,
)
from infrastructure.adapters import PythonBuildAdapter, JavaBuildAdapter, PytestAdapter, JUnitAdapter
from domain.entities import Language
from presentation.presentation import WorkspaceUI


def main():
    # Cross-cutting
    accessibility = AccessibilityConfig()
    plugins = [PythonPlugin(), JavaPlugin()]

    # Infrastructure adapters
    build_adapters = {
        Language.PYTHON: PythonBuildAdapter(),
        Language.JAVA: JavaBuildAdapter(),
    }
    test_adapters = {
        Language.PYTHON: PytestAdapter(),
        Language.JAVA: JUnitAdapter(),
    }

    # Services
    file_service = FileService()
    code_service = CodeService(plugins=plugins)
    build_service = BuildRunService(build_adapters=build_adapters, test_adapters=test_adapters)
    analysis_service = AnalysisService(plugins=plugins)
    design_doc_service = DesignDocService(file_service=file_service)
    collab_service = CollabService()

    # Launch UI
    workspace = WorkspaceUI(
        code_service=code_service,
        file_service=file_service,
        build_service=build_service,
        analysis_service=analysis_service,
        design_doc_service=design_doc_service,
        collab_service=collab_service,
        accessibility=accessibility,
    )
    workspace.launch()


if __name__ == "__main__":
    main()
