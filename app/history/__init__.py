# ==============================================================================
# OBSERVER PATTERN FOR TRACKING HISTORY
# ==============================================================================

# Who: The HistoryObserver and CalculatorWithObserver classes.
# What: Allows observers to be notified of changes in the calculation history.
# Why: To promote loose coupling between the calculator and observers, adhering to the Observer Pattern.
# Where: In the calculator's history management.
# When: Whenever a new calculation is performed.
# How: Observers register themselves with the calculator and are notified upon updates.

from app.history.logging import logging


class HistoryObserver:
    """
    Observer that gets notified whenever a new calculation is added to history.
    Implements the Observer Pattern.
    """
    def update(self, calculation):
        """
        Called when a new calculation is added to the history.
        Parameters:
        - calculation (Calculation): The calculation object that was added.
        """
        # Log the notification at INFO level.
        logging.info(f"Observer: New calculation added -> {calculation}")
        