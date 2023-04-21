from pyrundeck import Rundeck


rundeck = Rundeck(rundeck_url='http://localhost:4440/api/11/job/1ea9039b-5f0c-4644-a5b6-b983f50b298d/run?kJUIAvtWht594S56HxsHTk7W0JjUREsi',
                  token='kJUIAvtWht594S56HxsHTk7W0JjUREsi',
                  api_version=44
                 )

run = rundeck.run_job('cd5efd5b-7f8f-442e-8f94-da26095c7555')

#print(running_jobs)