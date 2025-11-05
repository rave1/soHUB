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
    ):
        write_options = WriteOptions(
            batch_size=100,
            flush_interval=1000,
            jitter_interval=2_000,
            retry_interval=5_000,
            max_retries=5,
            max_retry_delay=30_000,
            exponential_base=2,
        )
        wco = write_client_options(
            success_callback=self.success,
            error_callback=self.error,
            retry_callback=self.retry,
            write_options=write_options,
        )

        token = os.getenv("INFLUXDB_TOKEN")
        if not token:
            raise Exception("No token for influx!")
        super().__init__(
            host=host, token=token, database=database, write_client_options=wco
        )

    def success(self, data: str, *_):
        logger.info(f"Successfully wrote batch: data: {data}")

    def error(self, data: str, exception: InfluxDBError, *_):
        logger.error(
            f"Failed writing batch: config: {self}, data: {data} due: {exception}"
        )

    def retry(self, data: str, exception: InfluxDBError, *_):
        logger.error(
            f"Failed retry writing batch: config: {self}, data: {data} retry: {exception}"
        )
