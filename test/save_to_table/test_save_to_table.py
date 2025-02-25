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

from mu_pipelines_destination_spark.save_to_table.save_to_table import SaveToTable


@deprecation.fail_if_not_removed
def test_deprecation() -> None:
    config: DestinationConfig = cast(
        DestinationConfig,
        dict({"type": "table-spark", "table_name": "people", "mode": "overwrite"}),
    )

    configuration_provider: ConfigurationProvider = DIYConfigurationProvider(
        job_config=[
            cast(
                JobConfigItem,
                dict(
                    {
                        "execution": [],
                        "destination": [
                            {
                                "type": "table-spark",
                                "table_name": "people",
                                "mode": "overwrite",
                            }
                        ],
                    }
                ),
            )
        ],
        global_properties=cast(GlobalProperties, dict({"library": "spark"})),
        connection_config=cast(ConnectionProperties, dict({})),
    )

    SaveToTable(config, configuration_provider)
