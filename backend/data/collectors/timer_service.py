import time
from typing import Optional


class TimerService:
    """Abstract timer service independent of GUI frameworks"""
    
    def __init__(self):
        self.start_time: Optional[float] = None
    
    def start(self) -> None:
        """Start the timer"""
        self.start_time = time.time()
    
    def stop(self) -> None:
        """Stop the timer"""
        self.start_time = None
    
    def get_elapsed_time(self) -> float:
        """Get elapsed time in seconds"""
        if self.start_time:
            return time.time() - self.start_time
        return 0.0
    
    def format_time(self) -> str:
        """Format elapsed time as M:SS string"""
        elapsed = self.get_elapsed_time()
        minutes = int(elapsed // 60)
        seconds = int(elapsed % 60)
        return f"{minutes}:{seconds:02d}"
    
    def is_running(self) -> bool:
        """Check if timer is currently running"""
        return self.start_time is not None
    
    def reset(self) -> None:
        """Reset timer to zero"""
        self.start_time = None
