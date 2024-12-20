import string

from dataclasses import field

from hydra.core.config_store import ConfigStore
from omegaconf import MISSING
from pydantic.dataclasses import dataclass


@dataclass
class SpellCorrectionModelConfig:
    _target_: str = "src.utils.utils.SpellCorrectionModel"
    max_dictionary_edit_distance: int = 2
    prefix_length: int = 7
    count_threshold: int = 1


@dataclass
class DatasetCleanerConfig:
    _target_: str = MISSING


@dataclass
class StopwordsDatasetCleanerConfig(DatasetCleanerConfig):
    _target_: str = "src.data_processing.dataset_cleaners.StopwordsDatasetCleaner"


@dataclass
class LowerCaseDatasetCleanerConfig(DatasetCleanerConfig):
    _target_: str = "src.data_processing.dataset_cleaners.LowerCaseDatasetCleaner"


@dataclass
class URLDatasetCleanerConfig(DatasetCleanerConfig):
    _target_: str = "src.data_processing.dataset_cleaners.URLDatasetCleaner"


@dataclass
class PunctuationDatasetCleanerConfig(DatasetCleanerConfig):
    _target_: str = "src.data_processing.dataset_cleaners.PunctuationDatasetCleaner"
    punctuation: str = string.punctuation


@dataclass
class NonLettersDatasetCleanerConfig(DatasetCleanerConfig):
    _target_: str = "src.data_processing.dataset_cleaners.NonLettersDatasetCleaner"


@dataclass
class NewLineCharacterDatasetCleanerConfig(DatasetCleanerConfig):
    _target_: str = "src.data_processing.dataset_cleaners.NewLineCharacterDatasetCleaner"


@dataclass
class NonASCIIDatasetCleanerConfig(DatasetCleanerConfig):
    _target_: str = "src.data_processing.dataset_cleaners.NonASCIIDatasetCleaner"


@dataclass
class ReferenceToAccountDatasetCleanerConfig(DatasetCleanerConfig):
    _target_: str = "src.data_processing.dataset_cleaners.ReferenceToAccountDatasetCleaner"


@dataclass
class ReTweetDatasetCleanerConfig(DatasetCleanerConfig):
    _target_: str = "src.data_processing.dataset_cleaners.ReTweetDatasetCleaner"


@dataclass
class SpellCorrectionDatasetCleanerConfig(DatasetCleanerConfig):
    _target_: str = "src.data_processing.dataset_cleaners.SpellCorrectionDatasetCleaner"
    spell_correction_model: SpellCorrectionModelConfig = field(default_factory=SpellCorrectionModelConfig)


@dataclass
class DatasetCleanerManagerConfig:
    _target_: str = "src.data_processing.dataset_cleaners.DatasetCleanerManager"
    dataset_cleaners: dict[str, DatasetCleanerConfig] = field(default_factory=lambda: {})


def setup_config() -> None:
    cs = ConfigStore.instance()

    cs.store(
        group="dataset_cleaner_manager/dataset_cleaner",
        name="stop_words_dataset_cleaner_schema",
        node=StopwordsDatasetCleanerConfig,
    )

    cs.store(
        group="dataset_cleaner_manager/dataset_cleaner",
        name="lower_case_dataset_cleaner_schema",
        node=LowerCaseDatasetCleanerConfig,
    )

    cs.store(
        group="dataset_cleaner_manager/dataset_cleaner", name="url_dataset_cleaner_schema", node=URLDatasetCleanerConfig
    )

    cs.store(
        group="dataset_cleaner_manager/dataset_cleaner",
        name="punctuation_dataset_cleaner_schema",
        node=PunctuationDatasetCleanerConfig,
    )

    cs.store(
        group="dataset_cleaner_manager/dataset_cleaner",
        name="non_letters_dataset_cleaner_schema",
        node=NonLettersDatasetCleanerConfig,
    )

    cs.store(
        group="dataset_cleaner_manager/dataset_cleaner",
        name="new_line_character_dataset_cleaner_schema",
        node=NewLineCharacterDatasetCleanerConfig,
    )

    cs.store(
        group="dataset_cleaner_manager/dataset_cleaner",
        name="non_ascii_dataset_cleaner_schema",
        node=NonASCIIDatasetCleanerConfig,
    )

    cs.store(
        group="dataset_cleaner_manager/dataset_cleaner",
        name="reference_to_account_dataset_cleaner_schema",
        node=ReferenceToAccountDatasetCleanerConfig,
    )

    cs.store(
        group="dataset_cleaner_manager/dataset_cleaner",
        name="re_tweet_dataset_cleaner_schema",
        node=ReTweetDatasetCleanerConfig,
    )

    cs.store(
        group="dataset_cleaner_manager/dataset_cleaner",
        name="spell_correction_dataset_cleaner_schema",
        node=SpellCorrectionDatasetCleanerConfig,
    )

    cs.store(group="dataset_cleaner_manager", name="dataset_cleaner_manager_schema", node=DatasetCleanerManagerConfig)
