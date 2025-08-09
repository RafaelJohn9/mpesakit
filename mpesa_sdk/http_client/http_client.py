"""http_client.py: Defines an abstract base HTTP client class for making HTTP requests.

Provides a reusable interface for GET and POST requests.
"""

from typing import Dict, Any, Optional
from abc import ABC, abstractmethod


class HttpClient(ABC):
    """Abstract base HTTP client for making GET and POST requests."""

    @abstractmethod
    def post(
        self, url: str, json: Dict[str, Any], headers: Dict[str, str]
    ) -> Dict[str, Any]:
        """Sends a POST request."""
        pass

    @abstractmethod
    def get(
        self,
        url: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """Sends a GET request."""
        pass
