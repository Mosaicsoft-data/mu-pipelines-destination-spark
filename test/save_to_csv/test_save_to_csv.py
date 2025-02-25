from typing import cast

import deprecation
from mu_pipelines_configuration_provider.diy_configuration_provider import (
    DIYConfigurationProvider,
)
from mu_pipelines_interfaces.config_types.connection_properties import (
    ConnectionProperties,
)
from mu_pipelines_interfaces.config_types.destination_config import DestinationConfig
from mu_pipelines_interfaces.config_types.global_properties.global_properties import (
    GlobalProperties,
)
from mu_pipelines_interfaces.config_types.job_config import JobConfigItem
from mu_pipelines_interfaces.configuration_provider import ConfigurationProvider

from mu_pipelines_destination_spark.save_to_csv.save_to_csv import SaveToCSV


@deprecation.fail_if_not_removed
def test_deprecation() -> None:
    config: DestinationConfig = cast(
        DestinationConfig, dict({"type": "csv", "file_location": "file://test.csv"})
    )

    configuration_provider: ConfigurationProvider = DIYConfigurationProvider(
        job_config=[
            cast(
                JobConfigItem,
                dict(
                    {
                        "execution": [],
                        "destination": [
                            {"type": "csv", "file_location": "file://test.csv"}
                        ],
                    }
                ),
            )
        ],
        global_properties=cast(GlobalProperties, dict({"library": "spark"})),
        connection_config=cast(ConnectionProperties, dict({})),
    )

    SaveToCSV(config, configuration_provider)
