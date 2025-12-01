#!/usr/bin/env python3
"""
Configuration Loader for Java Migration System
"""

import yaml
import os
from typing import Dict, Any


class ConfigLoader:
    """Load and manage configuration from YAML file"""
    
    def __init__(self, config_path: str = "config.yml"):
        """
        Initialize config loader
        
        Args:
            config_path: Path to config file (default: config.yml in root)
        """
        self.config_path = config_path
        self.config = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from YAML file"""
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Configuration file not found: {self.config_path}")
        
        with open(self.config_path, 'r') as f:
            config = yaml.safe_load(f)
        
        return config
    
    def get_model_name(self) -> str:
        """Get configured model name"""
        return self.config.get('model', {}).get('name', 'gpt-oss:120b-cloud')
    
    def get_model_api_key(self) -> str:
        """Get configured API key"""
        return self.config.get('model', {}).get('api_key', '')
    
    def get_model_base_url(self) -> str:
        """Get configured base URL"""
        return self.config.get('model', {}).get('base_url', 'http://localhost:11434/v1')

    def get_model_temperature(self) -> float:
        """Get configured model temperature"""
        return self.config.get('model', {}).get('temperature', 0.7)
    
    def get_database_file(self) -> str:
        """Get configured database file"""
        return self.config.get('database', {}).get('file', 'agno.db')
    
    def get_default_java_version(self) -> str:
        """Get default Java version"""
        return self.config.get('migration', {}).get('default_java_version', '17')
    
    def get_default_modernization_level(self) -> str:
        """Get default modernization level"""
        return self.config.get('migration', {}).get('default_modernization_level', 'high')
    
    def get_default_coverage_target(self) -> int:
        """Get default coverage target"""
        return self.config.get('migration', {}).get('default_coverage_target', 80)
    
    def is_agent_enabled(self, agent_name: str) -> bool:
        """Check if a specific agent is enabled"""
        agents = self.config.get('agents', {})
        return agents.get(agent_name, {}).get('enabled', True)
    
    def get_ui_port(self) -> int:
        """Get UI port"""
        return self.config.get('ui', {}).get('port', 7777)
    
    def get_ui_host(self) -> str:
        """Get UI host"""
        return self.config.get('ui', {}).get('host', '0.0.0.0')
    
    def get_all(self) -> Dict[str, Any]:
        """Get all configuration"""
        return self.config


# Global config instance
_config = None


def get_config(config_path: str = "config.yml") -> ConfigLoader:
    """
    Get global configuration instance
    
    Args:
        config_path: Path to config file
        
    Returns:
        ConfigLoader instance
    """
    global _config
    if _config is None:
        _config = ConfigLoader(config_path)
    return _config


def reload_config(config_path: str = "config.yml"):
    """
    Reload configuration from file
    
    Args:
        config_path: Path to config file
    """
    global _config
    _config = ConfigLoader(config_path)