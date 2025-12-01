#!/usr/bin/env python3
"""
Java Migration Team - Coordinates all agents for Java application modernization
FIXED VERSION with enhanced code analysis reports
"""

from typing import Dict, Any

from agents import (
    ReportAgent,
    CodeAnalyzerAgent,
    MigrationAgent,
    TestGeneratorAgent
)

class JavaMigrationTeam:
    """
    Coordinates the multi-agent team for Java application modernization.
    Manages workflow, communication, and results aggregation.
    """

    def __init__(
        self,
        source_path: str,
        target_path: str,
        db_file: str = "agno.db"
    ):
        """
        Initialize the migration team
        
        Args:
            source_path: Path to legacy Java project
            target_path: Path for modernized project
            db_file: Database file for agent memory
        """
        self.source_path = source_path
        self.target_path = target_path
        self.db_file = db_file

        # Initialize all agents
        print("🚀 Initializing Java Migration Team...")
        self.report_manager = ReportAgent(db_file)
        self.code_analyzer = CodeAnalyzerAgent(db_file)
        self.migration_agent = MigrationAgent(db_file)
        self.test_generator = TestGeneratorAgent(db_file)

        # Results storage
        self.results = {"analysis": {}}

        print("✅ All agents initialized successfully!")

    def execute_migration(self):
        """
        Execute the complete migration workflow
        
        Returns:
            Dictionary containing all migration results
        """
        print("\n" + "="*80)
        print("🎯 STARTING JAVA MIGRATION PROCESS")
        print("="*80 + "\n")

        try:
            # Phase 1: Analysis
            print("🔍 Phase 1: Code Analysis")
            analysis_results = self._phase_analysis()
            self.results["analysis"] = analysis_results
            print("✅ Code analysis completed\n")

            # Phase 2: Migration
            print("🔄 Phase 2: Code Migration")
            self._phase_migration(analysis_results)
            print("✅ Code migration completed\n")

            # Phase 3: Test Generation
            print("🧪 Phase 3: Test Generation")
            self._phase_test_generation()
            print("✅ Test generation completed\n")

            print("="*80)
            print("🎉 MIGRATION PROCESS COMPLETED SUCCESSFULLY!")
            print("="*80 + "\n")


        except Exception as e:
            print(f"\n❌ Error during migration: {str(e)}")
            raise

    def _phase_analysis(self) -> Dict[str, Any]:
        """Phase 2: Analyze legacy code"""
        print("   📂 Analyzing project structure...")
        structure_analysis = self.code_analyzer.analyze_project_structure(self.source_path)

        return {
            "structure": structure_analysis['structure'],
            "files": structure_analysis['files']
        }

    def _phase_migration(self, analysis_results: Dict[str, Any]):
        """Phase 3: Migrate code"""
        print(f"   🔄 Migrating {len(analysis_results['files'])} files...")
        try:
            count = 1
            for file_path_to_read, file_info in analysis_results['files'].items():
                print(f"      [{count}/{len(analysis_results['files'])}] Migrating: {file_path_to_read}")
                self.migration_agent.migrate_java_class(
                    file_path_to_read, file_info
                )
                count += 1
        except Exception as e:
            print(f"          ⚠️ Error: {str(e)}")
        number_of_files = len(analysis_results['files'])
        print(f"   ✓ Migration completed for {number_of_files} files")

    def _phase_test_generation(self):
        """Phase 4: Generate tests"""

        print(f"   🧪 Generating tests")

        try:
            print(f"          ⚙️  Generating BDD scenarios...")
            self.test_generator.generate_bdd_scenarios()

            # Generate unit tests
            print(f"          ⚙️  Generating unit tests...")
            self.test_generator.generate_unit_tests()
        except Exception as e:
            print(f"          ⚠️  Error generating tests: {str(e)}")

        print(f"   ✓ Test generation completed")

    def _generate_final_report(self) -> dict[str, Any]:
        """Phase 6: Generate final report"""
        print("   📄 Synthesizing results from all agents...")

        final_report = self.report_manager.synthesize_results({
            "analysis": self.results["analysis"]
        })

        print("   ✓ Final report generated")
        return final_report

def main():
    """Example usage"""
    print("\n" + "="*80)
    print("JAVA MIGRATION TEAM - Multi-Agent System")
    print("="*80 + "\n")

    # Example configuration
    source_path = "./legacy_java_project2"  # Replace with actual path
    target_path = "./modernized_java_project"

    # Create team
    team = JavaMigrationTeam(
        source_path=source_path,
        target_path=target_path
    )

    # Execute migration
    team.execute_migration()

    print(f"\n✅ Migration completed!")
    print(f"📊 Results available in: {target_path}/migration_reports/")

if __name__ == "__main__":
    main()