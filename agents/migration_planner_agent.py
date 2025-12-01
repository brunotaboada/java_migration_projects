import json
from typing import Dict, Any, Optional

from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.ollama import Ollama

from utils import get_config
from utils.agent_config_loader import get_agent_config


class ReportAgent:

    def __init__(self, db_file: Optional[str] = None, prime_identity: bool = True):
        config = get_config()
        model_name = config.get_model_name()
        db_file = db_file or config.get_database_file()
        self.agent_config = get_agent_config('report_manager')
        self.agent = self._create_agent(model_name, db_file, config)
        self.migration_plan = None
        self.task_results = {}

        if prime_identity:
            self._prime_identity()

    def _create_agent(self, model_name: str, db_file: str, config) -> Agent:
        basic_config = self.agent_config.get_basic_config()
        return Agent(
            name=basic_config['name'],
            description=basic_config['description'],
            model=Ollama(
                id=model_name,
                api_key=config.get_model_api_key(),
                options={"temperature": config.get_model_temperature()}
            ),
            db=SqliteDb(db_file=db_file),
            use_json_mode=True,
            role=basic_config['role'],
            system_message="\n".join(self.agent_config.get_system_message()),
            instructions=self.agent_config.get_identity_instructions(),
            add_history_to_context=basic_config['add_history_to_context'],
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

    def create_migration_plan(self, project_info: Dict[str, Any]) -> Dict[str, Any]:
        prompt = self._get_externalized_prompt(
            'create_migration_plan',
            project_info=json.dumps(project_info, indent=2)
        )

        response = self.agent.run(prompt)

        try:
            self.migration_plan = self._parse_json(response.content)
        except:
            self.migration_plan = {
                "raw_plan": response.content,
                "status": "needs_parsing"
            }

        return self.migration_plan

    def _parse_json(self, plan_text: str) -> Dict[str, Any]:
        import re
        json_match = re.search(r'\{.*\}', plan_text, re.DOTALL)
        if json_match:
            return json.loads(json_match.group())
        return {"raw_plan": plan_text}


    def synthesize_results(self, agent_results: Dict[str, Any]) -> Dict[str, Any]:
        prompt = self._get_externalized_prompt(
            'synthesize_results',
            agent_results=json.dumps(agent_results, indent=2)
        )

        response = self.agent.run(prompt)

        try:
            return response.content
        except:
            return {"final_report": response.content}

    def run_chat(self, message: str) -> str:
        response = self.agent.run(message)
        return response.content