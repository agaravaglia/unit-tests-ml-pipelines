from datetime import datetime


class Logger:

    def __init__(self, module: str):
        self.module = module
    
    def _log(self, level: str, msg: str):
        """
        Flush to terminal the message required
        """
        print(f"[{level}][{self.module}][{datetime.now().strftime('%Y-%m%d %H:%M:%S')}]:: {msg}", flush=True)
    
    def info(self, msg: str):
        self._log(level="INFO", msg=msg)
    
    def warning(self, msg: str):
        self._log(level="WARNING", msg=msg)
    
    def error(self, msg: str):
        self._log(level="ERROR", msg=msg)