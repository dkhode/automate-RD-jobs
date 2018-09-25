"""Check if job syntax is ok."""
import sys
import unittest
import yaml
import glob2
import logging

logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)


class TestYamlJobs(unittest.TestCase):
  """Test class."""
  @staticmethod
  def test_jobs():
    """Test finction."""
    all_yaml_files = glob2.glob("./projects/**/*.yaml")
    uuids = {}
    for file_path in all_yaml_file:
        logger.info("Verify %s" % file_path)
        with open(file_path, 'r') as file:
          job = yaml.load(file.read())
          job = job[0]
          if job['uuid'] in uuids:
            raise ValueError(
              "Job %s has duplicate UUID of %s" % 
              (job['name'], uuids[job['uuid']])
            )
          uuids[job['uuid']] = job['name']
          file.close()
         
         
if __name__ == '__main__':
  unittest.main()
