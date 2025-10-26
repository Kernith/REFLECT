import json
import os
from typing import Dict, Any, List, Optional


class ConfigManager:
    """Pure configuration loader class with no GUI dependencies"""
    
    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self._config = None
    
    def load_config(self) -> Dict[str, Any]:
        """Load configuration from JSON file"""
        if self._config is None:
            try:
                with open(self.config_path, "r") as f:
                    self._config = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError) as e:
                print(f"Failed to load config: {e}")
                self._config = self._get_fallback_config()
        return self._config
    
    def get_observation_configs(self) -> List[Dict[str, Any]]:
        """Get all observation configurations"""
        config = self.load_config()
        return config.get("observation_configs", [])
    
    def get_colors(self) -> Dict[str, str]:
        """Get color configuration"""
        config = self.load_config()
        return config.get("colors", {})
    
    def get_config_by_index(self, index: int) -> Optional[Dict[str, Any]]:
        """Get observation configuration by index"""
        configs = self.get_observation_configs()
        if 0 <= index < len(configs):
            config = configs[index].copy()
            # Add colors to the config
            config['colors'] = self.get_colors()
            return config
        return None
    
    def get_config_by_name(self, name: str) -> Optional[Dict[str, Any]]:
        """Get observation configuration by name"""
        configs = self.get_observation_configs()
        for config in configs:
            if config.get('name') == name:
                config_copy = config.copy()
                config_copy['colors'] = self.get_colors()
                return config_copy
        return None
    
    def _get_fallback_config(self) -> Dict[str, Any]:
        """Return fallback configuration if file cannot be loaded"""
        return {
            "colors": {
                "student": "#F46715",
                "engagement": "#4169E1", 
                "instructor": "#0C8346",
                "comments": "#808080",
                "carmine": "#931621"
            },
            "observation_configs": [{
                "name": "Default",
                "timer_method": "timepoint",
                "timer_interval": 0,
                "student_actions": [],
                "instructor_actions": [],
                "engagement_images": []
            }]
        }
