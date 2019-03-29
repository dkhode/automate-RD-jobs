#!/usr/bin/env python
"""Import job yaml file in RD."""
import os
import sys
import glob2
from rundeck.client import Rundeck

RD_URL=os.getenv("RUNDECK_URL")
RD_TOKEN=os.getenv("RUNDECK_TOKEN")


def import_jobs(rd_client, projects, files):
    """Import all jobs in files array."""
    for file_path in files:
      job = open(file_path, 'r').read()
      print("Importing %s" % file_path)
      response = rd_client.import_job(
        job, fmt="yaml",project=projects,dupeOption="update"
      )
      if response['failed'] is not None:
        print("Import %s failed." % file_path)
        print(respinse['failed'])
        sys.exit(1)
      print("Impoerted %s successfully." % file_path)
      
      
def main():
  """Retrieve all yaml files and import them on RD."""
  #Generates the folder list
  project_list = [name for name in os.listdir(projects/)
                  if os.path.isdir(os.path.join("projects/", name))]
                  
  for projects in project_list:
    rd_client = Rundeck(RD_URL, port=443, protocol="https"
                        api_token=RD_TOKEN, verify_cert=False)
    all_yaml_files = glob2.glob('projects/%s/**/*.yaml' % projects)
    import_jobs(rd_client, projects, all_yaml_files)
    

if __name__ == "__main__":
    main()
