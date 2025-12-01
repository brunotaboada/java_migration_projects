import json
from typing import Dict, Any, Optional

from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.ollama import Ollama
from agno.tools.file import FileTools

from utils import get_config
from utils.agent_config_loader import get_agent_config


class MigrationAgent:
    
    def __init__(
        self,
        db_file: Optional[str] = None,
        prime_identity: bool = True
    ):
        config = get_config()
        model_name = config.get_model_name()
        db_file = db_file or config.get_database_file()
        self.agent_config = get_agent_config('migration_specialist')
        self.agent = self._create_agent(model_name, db_file, config)
        self.migration_results = {}
        
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
            db=SqliteDb(db_file=db_file),
            role=basic_config['role'],
            system_message="\n".join(self.agent_config.get_system_message()),
            instructions=self.agent_config.get_identity_instructions(),
            add_history_to_context=basic_config['add_history_to_context'],
            debug_mode=False,
            markdown=basic_config['markdown']
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
    
    def _get_externalized_prompt(self, prompt_name: str, **kwargs) -> str:
        """Get externalized prompt with format variables"""
        template = self.agent_config.get_prompt(prompt_name)
        try:
            return template.format(**kwargs)
        except KeyError as e:
            print(f"Warning: Missing format variable {e} for prompt {prompt_name}")
            return template
    
    def migrate_java_class(
        self,
        file_path: str,
        file_info: dict[str, Any]
    ):

        response = self.agent.run(self._get_externalized_prompt(
            'migrate_java_class',
            file_path_to_read=file_path,
            file_name=file_info['file_name_suggestion'],
            file_path=file_info['package_suggestion']
        ))

        try:
            self._parse_json(response.content)
        except:
            print("Error parsing JSON response", response.content)

    def _parse_json(self, text: str) -> Dict[str, Any]:
        import re
        
        json_match = re.search(r'```(?:json)?\s*(\{.*\})\s*```', text, re.DOTALL)
        if json_match:
            return json.loads(json_match.group(1))
        
        json_match = re.search(r'\{.*\}', text, re.DOTALL)
        if json_match:
            return json.loads(json_match.group())
        
        raise ValueError("No valid JSON found in response")
    