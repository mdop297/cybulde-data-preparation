from pydantic.dataclasses import dataclass
from hydra.core.config_store import ConfigStore


@dataclass
class GCPConfig:
    project_id: str = "cybully-project"
    zone: str = "asia-southeast1-a"
    network: str = "default"


def setup_config() -> None:
    cs = ConfigStore.instance()
    cs.store(name="gcp_config_schema", node=GCPConfig)
