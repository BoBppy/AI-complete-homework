import yaml
import logging
from pathlib import Path
from typing import Dict, Any, Optional

class ConfigManager:
    _instance = None
    _config: Dict[str, Any] = {}
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
            cls._instance._load_config()
        return cls._instance
    
    def _load_config(self):
        """加载配置文件"""
        try:
            config_path = Path("config.yaml")
            if config_path.exists():
                with open(config_path, 'r', encoding='utf-8') as f:
                    self._config = yaml.safe_load(f)
                self._setup_logging()
            else:
                raise FileNotFoundError("配置文件 config.yaml 不存在")
        except Exception as e:
            print(f"加载配置文件时出错: {str(e)}")
            raise
    
    def _setup_logging(self):
        """配置日志系统"""
        logging_config = self._config.get('logging', {})
        logging.basicConfig(
            level=getattr(logging, logging_config.get('level', 'INFO')),
            format=logging_config.get('format', '%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
            filename=logging_config.get('file', 'app.log')
        )
    
    def get_openai_config(self) -> Dict[str, Any]:
        """获取OpenAI配置"""
        return self._config.get('openai', {})
    
    def get_server_config(self) -> Dict[str, Any]:
        """获取服务器配置"""
        return self._config.get('server', {})
    
    def get_file_config(self) -> Dict[str, Any]:
        """获取文件处理配置"""
        return self._config.get('file', {})
    
    def update_config(self, section: str, key: str, value: Any):
        """更新配置"""
        if section in self._config:
            self._config[section][key] = value
            with open('config.yaml', 'w', encoding='utf-8') as f:
                yaml.dump(self._config, f, allow_unicode=True)
        else:
            raise KeyError(f"配置节 {section} 不存在")
    
    def validate_file_size(self, file_size: int) -> bool:
        """验证文件大小"""
        max_size = self.get_file_config().get('max_size_mb', 10) * 1024 * 1024
        return file_size <= max_size
    
    def validate_file_extension(self, filename: str) -> bool:
        """验证文件扩展名"""
        allowed_extensions = self.get_file_config().get('allowed_extensions', ['.docx'])
        return any(filename.lower().endswith(ext) for ext in allowed_extensions)
    
    @property
    def upload_dir(self) -> Path:
        """获取上传目录路径"""
        return Path(self.get_file_config().get('upload_dir', 'uploads'))
    
    @property
    def output_dir(self) -> Path:
        """获取输出目录路径"""
        return Path(self.get_file_config().get('output_dir', 'outputs'))
    
    def ensure_directories(self):
        """确保必要的目录存在"""
        self.upload_dir.mkdir(exist_ok=True)
        self.output_dir.mkdir(exist_ok=True) 