c = get_config()
import logging
c.JupyterHub.ip = 'HUB_INTERNAL_IP'
c.JupyterHub.port = 8000
c.JupyterHub.hub_ip = 'HUB_INTERNAL_IP'
c.JupyterHub.hub_port = 8888

# Authentication configuration
c.PAMAuthenticator.open_sessions = False

c.JupyterHub.spawner_class = 'libcloudspawner.spawner.LibcloudSpawner'
c.Spawner.start_timeout = 600
c.Spawner.http_timeout = 60
c.Spawner.debug = True
c.Spawner.notebook_dir = ""
c.Spawner.args = ['']
c.Spawner.default_url = ""
c.Spawner.port = 8000
c.LibcloudSpawner.libcloud_driver_params = {"arg_user_id": "APPCRED_ID",
                                    "arg_key": "APPCRED_KEY",
                                    "ex_force_auth_version": "3.x_appcred",
                                    "ex_force_auth_url": "https://keystone.fqdn:5000",
                                    "ex_force_service_region": "RegionOne",
                                    "ex_tenant_name": "myproject",
                                    "ex_domain_name": "Default"}
c.LibcloudSpawner.notebookargs = ""
c.LibcloudSpawner.userserver_net = "private"
c.LibcloudSpawner.userserver_keyname = "jupytercloud-2023-12"
c.LibcloudSpawner.userserver_sizes = [("Small (1 core, 1.95Gb)", "vd.1")]
c.LibcloudSpawner.userserver_images = [("JupyterLab Ubuntu 22.04", "ubuntu-2204.amd64-genericcloud.20230712")]

c.LibcloudSpawner.userdata_template_name="example_userdata_from_vanilla_cloudimage.yaml.j2"