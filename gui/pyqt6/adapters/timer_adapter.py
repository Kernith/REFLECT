from PyQt6.QtCore import QTimer
from backend.data.collectors.timer_service import TimerService


class PyQt6TimerAdapter:
    """Adapter to wrap TimerService with PyQt6 QTimer"""
    
    def __init__(self, timer_service: TimerService, callback):
        self.timer_service = timer_service
        self.qtimer = QTimer()
        self.qtimer.timeout.connect(callback)
    
    def start(self, interval_ms: int = 100) -> None:
        """Start the timer with specified interval in milliseconds"""
        self.timer_service.start()
        self.qtimer.start(interval_ms)
    
    def stop(self) -> None:
        """Stop the timer"""
        self.timer_service.stop()
        self.qtimer.stop()
    
    def get_elapsed_time(self) -> float:
        """Get elapsed time from the timer service"""
        return self.timer_service.get_elapsed_time()
    
    def format_time(self) -> str:
        """Format elapsed time from the timer service"""
        return self.timer_service.format_time()
    
    def is_running(self) -> bool:
        """Check if timer is running"""
        return self.timer_service.is_running()
    
    def reset(self) -> None:
        """Reset the timer"""
        self.timer_service.reset()
        self.qtimer.stop()
