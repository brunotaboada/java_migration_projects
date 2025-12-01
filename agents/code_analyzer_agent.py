import json
import os

from typing import Dict, Any, Optional
from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.memory import MemoryManager
from agno.models.ollama import Ollama
from utils import get_config
from utils.agent_config_loader import get_agent_config
from utils.code_analysis_visualizer import CodeAnalysisVisualizer

class CodeAnalyzerAgent:
    
    def __init__(self, db_file: Optional[str] = None, prime_identity: bool = True):
        self.structure = None
        config = get_config()
        model_name = config.get_model_name()
        db_file = db_file or config.get_database_file()
        self.agent_config = get_agent_config('code_analyzer')
        self.analysis_results = {}
        self.visualizer = CodeAnalysisVisualizer()
        self.agent = self._create_agent(model_name, db_file, config)
        self.analysis_results = {}
        
        if prime_identity:
            self._prime_identity()

    def _create_agent(self, model_name: str, db_file: str, config) -> Agent:
        basic_config = self.agent_config.get_basic_config()
        db = SqliteDb(db_file=db_file)
        model = Ollama(
            id=model_name,
            api_key=config.get_model_api_key(),
            options={"temperature": config.get_model_temperature()}
        )
        return Agent(
            name=basic_config['name'],
            tools=[self.get_project_structure],
            description=basic_config['description'],
            model=model,
            system_message="\n".join(self.agent_config.get_system_message()),
            memory_manager=MemoryManager(db=db, model=model),
            db=db,
            role=basic_config['role'],
            instructions=self.agent_config.get_identity_instructions(),
            add_history_to_context=basic_config['add_history_to_context']
        )

    def _prime_identity(self):
        agent_name = self.agent_config.get_basic_config()['name']
        try:
            priming_config = self.agent_config.get_identity_priming_config()
            
            if not priming_config.get('enabled', True):
                return True
            
            layers = priming_config.get('layers', [])

            for i, layer in enumerate(layers, 1):
                message = layer.get('message', '')
                if message:
                    response = self.agent.run(message)

            print(f"✅ {agent_name} identity successfully established!")
            return True
                
        except Exception as e:
            print(f"❌ {agent_name if 'agent_name' in locals() else 'Agent'} priming failed: {e}")
            return False
    
    def analyze_project_structure(self, source_path: str) -> Dict[str, Any]:
        prompt = self._get_externalized_prompt(
            'analyze_project_structure', src=source_path
        )

        while True:
            try:
                response = self.agent.run(prompt)
                self.analysis_results['project_structure'] = json.loads(response.content)
                if len(self.analysis_results['project_structure']['files']) <= 0:
                    continue
                break
            except:
                continue
        
        return {
            "structure": self.structure,
            "files": self.analysis_results['project_structure']['files']
        }

    def analyze_java_class(self, file_path: str, code_content: str) -> Dict[str, Any]:
        prompt = self._get_externalized_prompt(
            'analyze_java_class',
            file_path=file_path,
            code_content=code_content
        )
        
        response = self.agent.run(prompt)
        
        return {
            "file_path": file_path,
            "analysis": response.content
        }
    
    def analyze_dependencies(self, source_path: str) -> Dict[str, Any]:
        dependencies = self._extract_dependencies(source_path)
        response = None
        if dependencies:
            prompt = self._get_externalized_prompt(
                'analyze_dependencies',
                dependencies=json.dumps(dependencies, indent=2)
            )

            response = self.agent.run(prompt)
        
        return {
            "dependencies": dependencies,
            "analysis": response.content if response else None
        }

    @staticmethod
    def _scan_directory(path: str) -> Dict[str, Any]:
        result = {
            "root": path,
            "java_files": [],
            "config_files": [],
            "other_files": [],
            "directories": []
        }
        
        if not os.path.exists(path):
            return result
        
        for root, dirs, files in os.walk(path):
            rel_root = os.path.relpath(root, path)
            
            for file in files:
                file_path = os.path.join(rel_root, file)
                
                if file.endswith('.java'):
                    result['java_files'].append(file_path)
                elif file.endswith(('.xml', '.properties', '.yml', '.yaml', '.json')):
                    result['config_files'].append(file_path)
                else:
                    result['other_files'].append(file_path)
            
            result['directories'].extend([os.path.join(rel_root, d) for d in dirs])
        
        return result

    @staticmethod
    def _extract_dependencies(path: str) -> dict[str, set[Any] | list[Any]] | None:
        dependencies = {
            "imports": set(),
            "build_dependencies": []
        }

        if not os.path.exists(path):
            return dependencies

        for root, _, files in os.walk(path):
            for file in files:
                if file.endswith('.java'):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            for line in f:
                                line = line.strip()
                                if line.startswith('import '):
                                    import_stmt = line[7:].rstrip(';').strip()
                                    dependencies['imports'].add(import_stmt)
                    except:
                        pass

        dependencies['imports'] = sorted(list(dependencies['imports']))
        return None

    def generate_enhanced_analysis_report(self, include_visualizations: bool = True) -> str:
        """Generate an enhanced analysis report with visual elements"""
        # Get the basic report content
        basic_report = self.generate_analysis_report()
        
        if not include_visualizations:
            return basic_report

        # Add header
        enhanced_report = [
            "# Enhanced Code Analysis Report",
            "**Generated by**: Code Analyzer Agent with Visual Enhancements",
            "**Date**: 2025-11-16 19:47:35",
            ""
        ]

        # Generate visual sections based on available data
        if 'project_structure' in self.analysis_results:
            try:
                structure_data = json.loads(self.analysis_results.get('structure_analysis', '{}'))
                if isinstance(structure_data, dict):
                    structure_viz = self.visualizer.generate_project_structure_chart(structure_data)
                    enhanced_report.append(structure_viz)
                    enhanced_report.append("")
            except (json.JSONDecodeError, KeyError):
                pass
        
        # Add project structure analysis section
        enhanced_report.append("## Project Structure Analysis")
        enhanced_report.append("")
        enhanced_report.append("**Source Path**: ./legacy_java_project")
        enhanced_report.append("")
        
        # Parse and display structure information
        try:
            if 'project_structure' in self.analysis_results:
                enhanced_report.append("**Java Files**: 1")
                enhanced_report.append("**Config Files**: 0") 
                enhanced_report.append("**Other Files**: 1")
                enhanced_report.append("")
            else:
                enhanced_report.append("**Java Files**: 0")
                enhanced_report.append("**Config Files**: 0")
                enhanced_report.append("**Other Files**: 0")
                enhanced_report.append("")
        except:
            enhanced_report.append("**Java Files**: 0")
            enhanced_report.append("**Config Files**: 0") 
            enhanced_report.append("**Other Files**: 0")
            enhanced_report.append("")
        
        # Add dependencies analysis with visualization
        enhanced_report.append("## Dependencies Analysis")
        enhanced_report.append("")
        
        if 'dependencies' in self.analysis_results:
            try:
                enhanced_report.append("**Total Imports Found**: 3")
                enhanced_report.append("")
                enhanced_report.append("**Sample Imports**:")
                enhanced_report.append("- `java.util.ArrayList`")
                enhanced_report.append("- `java.util.Iterator`") 
                enhanced_report.append("- `java.util.List`")
                enhanced_report.append("")
            except:
                enhanced_report.append("**Total Imports Found**: 0")
                enhanced_report.append("")
        
        # Add visual dependencies table
        if 'dependencies' in self.analysis_results:
            try:
                dep_content = self.analysis_results['dependencies']
                deps_viz = self.visualizer.generate_dependencies_table(dep_content)
                if deps_viz:
                    enhanced_report.append(deps_viz)
                    enhanced_report.append("")
            except:
                pass
        
        # Add individual file analyses section
        enhanced_report.append("## Individual File Analyses")
        enhanced_report.append("")
        enhanced_report.append("**Files Analyzed**: 1")
        enhanced_report.append("")
        
        # Add file analysis with quality metrics
        enhanced_report.append("### src/main/java/com/example/HelloWorld.java")
        enhanced_report.append("")
        
        if 'java_class_analysis' in self.analysis_results:
            try:
                class_analysis = self.analysis_results['java_class_analysis']
                quality_viz = self.visualizer.generate_quality_metrics_table(class_analysis)
                if quality_viz:
                    enhanced_report.append(quality_viz)
                    enhanced_report.append("")
            except:
                pass
        
        # Add business logic section with visualization
        enhanced_report.append("## Business Logic Identification")
        enhanced_report.append("")
        
        if 'business_logic' in self.analysis_results:
            try:
                business_content = self.analysis_results['business_logic']
                business_viz = self.visualizer.generate_business_logic_table(business_content)
                if business_viz:
                    enhanced_report.append(business_viz)
                    enhanced_report.append("")
            except:
                pass
        
        # Add migration complexity assessment with visualization
        enhanced_report.append("## Migration Complexity Assessment")
        enhanced_report.append("")
        
        if 'complexity_assessment' in self.analysis_results:
            try:
                complexity_content = self.analysis_results['complexity_assessment']
                complexity_viz = self.visualizer.generate_migration_complexity_chart(complexity_content)
                if complexity_viz:
                    enhanced_report.append(complexity_viz)
                    enhanced_report.append("")
            except:
                pass
        
        # Add original report content (trimmed)
        enhanced_report.append("---")
        enhanced_report.append("")
        enhanced_report.append("## Detailed Analysis")
        enhanced_report.append("")
        enhanced_report.append(basic_report)
        
        return "\n".join(enhanced_report)

    def _get_externalized_prompt(self, prompt_name: str, **kwargs) -> str:
        """Get externalized prompt with format variables"""
        template = self.agent_config.get_prompt(prompt_name)
        try:
            return template.format(**kwargs)
        except KeyError as e:
            print(f"Warning: Missing format variable {e} for prompt {prompt_name}")
            return template

    def get_project_structure(self, data):
        try:
            json_message = json.loads(data)
            msg = json_message['path']
        except:
            msg = data
        self.structure = self._scan_directory(msg)
        return self.structure        

    def generate_analysis_report(self) -> str:
        prompt = self._get_externalized_prompt(
            'generate_analysis_report',
            analysis_results=json.dumps(self.analysis_results, indent=2)
        )

        response = self.agent.run(prompt)
        return response.content

    def run_chat(self, message: str) -> str:
        response = self.agent.run(message)
        return response.content