"""CDEvents Pydantic parsing for Data Validation"""
from typing import Dict, Union, Optional
from pydantic import BaseModel
import datetime

class parsedEvent(BaseModel):
    """BaseModel contains all the required fields and their data types for validation"""
    context_id: Optional[str]
    context_source: Optional[str]
    context_timestamp: Optional[datetime.datetime]
    subject_id: Optional[str]
    subject_source: Optional[str]
    custom_data_content_type: Optional[str]
    custom_data: Optional[Union[str, Dict, None]]
    artifact_id: Optional[str]
    change: Optional[Dict[str,str]]
    repository: Optional[Dict[str, str]]
    name: Optional[str]
    url: Optional[str]
    pipeline_name: Optional[str]
    outcome: Optional[str]
    errors: Optional[str]
    view_url: Optional[str]
    owner: Optional[str]
    environment: Optional[Dict[str,str]]
    pipeline_run: Optional[Dict[str, str]]
    task_name: Optional[str]