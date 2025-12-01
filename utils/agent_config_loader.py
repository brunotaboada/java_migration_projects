#!/usr/bin/env python3
"""
Agent Configuration Loader for Java Migration System
"""

from pathlib import Path
from typing import Dict, Any, Optional

import yaml

class AgentConfigLoader:
    """Load and manage agent-specific configurations from YAML files"""
    
    def __init__(self, agent_name: str, config_dir: str = "agents_config"):
        """
        Initialize agent config loader
        
        Args:
            agent_name: Name of the agent (e.g., 'code_analyzer')
            config_dir: Directory containing agent configurations
        """
        self.agent_name = agent_name
        self.config_dir = Path(config_dir) / agent_name
        self.config_file = self.config_dir / "config.yml"
        self.config = self._load_agent_config()
    
    def _load_agent_config(self) -> Dict[str, Any]:
        """Load agent configuration from YAML file"""
        if not self.config_file.exists():
            raise FileNotFoundError(f"Agent configuration file not found: {self.config_file}")
        
        with open(self.config_file, 'r') as f:
            config = yaml.safe_load(f)
        
        return config
    
    def get_basic_config(self) -> Dict[str, Any]:
        """Get basic agent configuration"""
        return {
            'name': self.config.get('name', ''),
            'description': self.config.get('description', ''),
            'role': self.config.get('role', 'specialist'),
            'add_history_to_context': self.config.get('add_history_to_context', True),
            'markdown': self.config.get('markdown', True)
        }

    def get_system_message(self) -> list:
        """Get identity enforcement instructions"""
        system_message = []

        if self.config.get('system_messages', {}):
            system_message = self.config.get('system_messages', {})

        return system_message

    def get_identity_instructions(self) -> list:
        """Get identity enforcement instructions"""
        instructions = []

        domain = self.config.get('identity_instructions', {}).get('domain_expertise', [])
        if domain:
            instructions.append("=== YOUR DOMAIN ===")
            for expertise in domain:
                instructions.append(f"✓ {expertise}")
            instructions.append("")

        instructions.append("")

        for rule in self.config.get('identity_instructions', {}).get('critical_rules', []):
            instructions.append(f"CRITICAL: {rule}")

        return instructions
    
    def get_prompts(self) -> Dict[str, str]:
        """Get all prompts for the agent"""
        prompts_section = self.config.get('prompts', {})
        if not prompts_section:

            return {}
        return prompts_section
    
    def get_prompt(self, prompt_name: str) -> str:
        """Get a specific prompt by name"""
        prompts = self.get_prompts()
        return prompts.get(prompt_name, '')
    
    def get_ui_context_instructions(self) -> list:
        """Get UI context instructions"""
        ui_instructions = self.config.get('ui_context_instructions', [])
        return ui_instructions if isinstance(ui_instructions, list) else []
    
    def get_identity_priming_config(self) -> Dict[str, Any]:
        """Get identity priming configuration"""
        return self.config.get('identity_priming', {})
    
    def get_all(self) -> Dict[str, Any]:
        """Get complete agent configuration"""
        return self.config

class MultiAgentConfigManager:
    """Manage configurations for multiple agents"""
    
    def __init__(self, config_dir: str = "agents_config"):
        """
        Initialize multi-agent config manager
        
        Args:
            config_dir: Directory containing agent configurations
        """
        self.config_dir = Path(config_dir)
        self.agent_configs = {}
        self._discover_agent_configs()
    
    def _discover_agent_configs(self):
        """Discover all available agent configurations"""
        if not self.config_dir.exists():
            return
        
        for agent_dir in self.config_dir.iterdir():
            if agent_dir.is_dir():
                agent_name = agent_dir.name
                self.agent_configs[agent_name] = AgentConfigLoader(agent_name, str(self.config_dir))
    
    def get_agent_config(self, agent_name: str) -> Optional[AgentConfigLoader]:
        """Get configuration for a specific agent"""
        return self.agent_configs.get(agent_name)
    
    def list_agents(self) -> list:
        """List all available agents"""
        return list(self.agent_configs.keys())
    
    def get_all_agent_configs(self) -> Dict[str, AgentConfigLoader]:
        """Get all agent configurations"""
        return self.agent_configs

_agent_config_managers = {}

def get_agent_config(agent_name: str, config_dir: str = "agents_config") -> AgentConfigLoader:
    """
    Get agent configuration instance
    
    Args:
        agent_name: Name of the agent
        config_dir: Directory containing agent configurations
        
    Returns:
        AgentConfigLoader instance
    """
    global _agent_config_managers
    
    if config_dir not in _agent_config_managers:
        _agent_config_managers[config_dir] = MultiAgentConfigManager(config_dir)
    
    manager = _agent_config_managers[config_dir]
    config_loader = manager.get_agent_config(agent_name)
    
    if not config_loader:
        raise ValueError(f"No configuration found for agent: {agent_name}")
    
    return config_loader

def reload_agent_configs(config_dir: str = "agents_config"):
    """
    Reload all agent configurations
    
    Args:
        config_dir: Directory containing agent configurations
    """
    global _agent_config_managers
    if config_dir in _agent_config_managers:
        del _agent_config_managers[config_dir]

def list_available_agents(config_dir: str = "agents_config") -> list:
    """
    List all available agents
    
    Args:
        config_dir: Directory containing agent configurations
        
    Returns:
        List of agent names
    """
    manager = MultiAgentConfigManager(config_dir)
    return manager.list_agents()