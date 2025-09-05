import logging
from pathlib import Path
import os

class Logging:
    """
    Logging configuration
    """
    _instance = None

    def __new__(cls, 
                log_name: str = "AppLogger", 
                log_file: str = "app.log", 
                base_dir: Path = None):
        
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        log_path = base_dir / "logs"
        log_path.mkdir(parents=True, exist_ok=True)

        # Configure root logger
        cls._instance.logger = logging.getLogger(log_name)
        cls._instance.logger.setLevel(logging.DEBUG)

        # File handler
        file_handler = logging.FileHandler(log_path / log_file)
        file_handler.setLevel(logging.DEBUG)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Formatter
        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Attach handlers only once
        if not cls._instance.logger.handlers:
            cls._instance.logger.addHandler(file_handler)
            cls._instance.logger.addHandler(console_handler)

        return cls._instance
    
    def get_logger(self, name: str) -> logging.Logger:
        return self.logger.getChild(name)


