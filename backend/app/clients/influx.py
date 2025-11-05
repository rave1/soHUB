from influxdb_client_3 import (
    InfluxDBClient3,
    InfluxDBError,
    WriteOptions,
    write_client_options,
)
from loguru import logger
import os


class InfluxDBClientWrapper(InfluxDBClient3):
    """
    InfluxDb3 Client wrapper that populates write options.
    """

    def __init__(
        self,
        host=None,
        database=None,
        token=None,
        write_client_options=None,
    ):
        token = os.getenv("INFLUXDB_TOKEN")
        if not token:
            raise Exception("No token for influx!")
        super().__init__(
            host=host, token=token, database=database, write_client_options=self.wco
        )

    def success(self, data: str):
        logger.info(f"Successfully wrote batch: data: {data}")

    def error(self, data: str, exception: InfluxDBError):
        logger.error(
            f"Failed writing batch: config: {self}, data: {data} due: {exception}"
        )

    def retry(self, data: str, exception: InfluxDBError):
        logger.error(
            f"Failed retry writing batch: config: {self}, data: {data} retry: {exception}"
        )

    write_options = WriteOptions(
        batch_size=500,
        flush_interval=10_000,
        jitter_interval=2_000,
        retry_interval=5_000,
        max_retries=5,
        max_retry_delay=30_000,
        exponential_base=2,
    )
    wco = write_client_options(
        success_callback=success,
        error_callback=error,
        retry_callback=retry,
        write_options=write_options,
    )
