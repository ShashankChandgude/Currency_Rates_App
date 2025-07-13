"""
Tests for the logging configuration.
"""

import logging
from app.core.logging import setup_logging


def test_setup_logging():
    """Test that logging setup can be called without errors."""
    # This should not raise any exceptions
    setup_logging()
    
    # Verify that the root logger is configured
    root_logger = logging.getLogger()
    assert root_logger.level <= logging.INFO


def test_logging_levels():
    """Test that different logging levels work."""
    logger = logging.getLogger(__name__)
    
    # These should not raise exceptions
    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")
    logger.error("Error message")
    
    # Verify logger exists
    assert logger is not None


def test_logger_handlers():
    """Test that logger has handlers configured."""
    logger = logging.getLogger(__name__)
    
    # After setup_logging, there should be handlers
    setup_logging()
    root_logger = logging.getLogger()
    
    # Should have at least one handler
    assert len(root_logger.handlers) > 0 