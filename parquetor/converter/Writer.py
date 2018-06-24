import pyarrow as pa
from hashlib import md5
from pyarrow import parquet
from parquetor import logger

logger = logger.get_logger(__name__)


class Writer(object):

    @classmethod
    def write_parquet(cls, data, to_path, compression="gzip"):
        pa_table = pa.Table.from_pandas(data)
        parquet.write_table(pa_table, to_path, compression=compression)
        logger.info("completed write parquet file to {}".format(to_path))

    @classmethod
    def write_s3(cls, data, s3_bucket, s3_path, compression="gzip", tmp_file_location="/tmp"):
        tmp_file_name = md5((s3_bucket + s3_path).encode("utf-8")).hexdigest()
        cls.write_parquet(data, tmp_file_location + "/" + tmp_file_name, compression=compression)

        # Todo あとでs3にuploadするところを書く
