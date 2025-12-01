import json
from typing import Dict, List, Any, Optional

from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.ollama import Ollama
from agno.tools.file import FileTools

from utils import get_config
from utils.agent_config_loader import get_agent_config


class TestGeneratorAgent:
    
    def __init__(self, db_file: Optional[str] = None, prime_identity: bool = True):
        config = get_config()
        model_name = config.get_model_name()
        db_file = db_file or config.get_database_file()
        self.agent_config = get_agent_config('test_generator')
        self.agent = self._create_agent(model_name, db_file, config)
        self.test_results = {}
        
        if prime_identity:
            self._prime_identity()
        
    def _create_agent(self, model_name: str, db_file: str, config) -> Agent:
        basic_config = self.agent_config.get_basic_config()
        return Agent(
            name=basic_config['name'],
            description=basic_config['description'],
            tools=[FileTools()],
            model=Ollama(
                id=model_name,
                api_key=config.get_model_api_key(),
                options={"temperature": config.get_model_temperature()}
            ),
            use_json_mode=True,
            db=SqliteDb(
                db_file=db_file
            ),
            role=basic_config['role'],
            system_message="\n".join(self.agent_config.get_system_message()),
            instructions=self.agent_config.get_identity_instructions(),
            add_history_to_context=basic_config['add_history_to_context'],
            markdown=basic_config['markdown']
        )
    
    def _get_externalized_prompt(self, prompt_name: str, **kwargs) -> str:
        """Get externalized prompt with format variables"""
        template = self.agent_config.get_prompt(prompt_name)
        try:
            return template.format(**kwargs)
        except KeyError as e:
            print(f"Warning: Missing format variable {e} for prompt {prompt_name}")
            return template
    
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
    
    def generate_bdd_scenarios(self) -> Dict[str, Any]:
        prompt = self._get_externalized_prompt(
            'generate_bdd_scenarios'
        )
        
        response = self.agent.run(prompt)
        
        try:
            result = self._parse_json(response.content)
        except:
            result = {
                "feature_file": response.content,
                "parsing_note": "Response not in expected JSON format"
            }
        
        self.test_results[f"bdds"] = result
        return result
    
    def generate_unit_tests(self) -> Dict[str, Any]:
        prompt = self._get_externalized_prompt(
            'generate_unit_tests'
        )
        
        response = self.agent.run(prompt)
        
        try:
            result = self._parse_json(response.content)
        except:
            result = {
                "test_class": response.content,
                "parsing_note": "Response not in expected JSON format"
            }
        
        self.test_results[f"test_units"] = result
        return result
    
    def generate_integration_tests(
        self,
        components: List[Dict[str, Any]],
        integration_points: List[str]
    ) -> Dict[str, Any]:
        prompt = self._get_externalized_prompt(
            'generate_integration_tests',
            components=json.dumps(components, indent=2),
            integration_points=json.dumps(integration_points, indent=2)
        )
        
        response = self.agent.run(prompt)
        
        try:
            return self._parse_json(response.content)
        except:
            return {
                "test_classes": [response.content],
                "parsing_note": "Response not in expected JSON format"
            }
    
    def generate_test_data(
        self,
        data_requirements: Dict[str, Any]
    ) -> Dict[str, Any]:
        prompt = self._get_externalized_prompt(
            'generate_test_data',
            data_requirements=json.dumps(data_requirements, indent=2)
        )
        
        response = self.agent.run(prompt)
        
        try:
            return self._parse_json(response.content)
        except:
            return {
                "test_data": response.content,
                "parsing_note": "Response not in expected JSON format"
            }
    
    def generate_mock_configurations(
        self,
        dependencies: List[str],
        mock_scenarios: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        prompt = self._get_externalized_prompt(
            'generate_mock_configurations',
            dependencies=json.dumps(dependencies, indent=2),
            mock_scenarios=json.dumps(mock_scenarios, indent=2)
        )
        
        response = self.agent.run(prompt)
        
        try:
            return self._parse_json(response.content)
        except:
            return {"mock_code": response.content}
    
    def calculate_test_coverage(
        self,
        source_code: str,
        test_code: str
    ) -> Dict[str, Any]:
        prompt = self._get_externalized_prompt(
            'calculate_test_coverage',
            source_code=source_code,
            test_code=test_code
        )
        
        response = self.agent.run(prompt)
        
        try:
            return self._parse_json(response.content)
        except:
            return {"coverage_analysis": response.content}
    
    def generate_test_suite_report(
        self,
        all_tests: Dict[str, Any]
    ) -> str:
        prompt = self._get_externalized_prompt(
            'generate_test_suite_report',
            all_tests=json.dumps(all_tests, indent=2)
        )
        
        response = self.agent.run(prompt)
        return response.content
    
    def _parse_json(self, text: str) -> Dict[str, Any]:
        import re
        
        json_match = re.search(r'```(?:json)?\s*(\{.*\})\s*```', text, re.DOTALL)
        if json_match:
            return json.loads(json_match.group(1))
        
        json_match = re.search(r'\{.*\}', text, re.DOTALL)
        if json_match:
            return json.loads(json_match.group())
        
        raise ValueError("No valid JSON found in response")
    
    def run_chat(self, message: str) -> str:
        response = self.agent.run(message)
        return response.content