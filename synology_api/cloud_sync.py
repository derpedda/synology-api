from __future__ import annotations
from . import base_api


class CloudSync(base_api.BaseApi):
    '''
       Cloud Sync API implementation.

       This API provides the functionality to get information related to the package settings and current connections and tasks. 
       It also provides functionalities to set most of the settings for tasks and package configuration, as well as manage the current syncing processes.

       Due to the vast amount of public clouds available in the project, the API was not tested for every cloud scenario, so some params request may be missing in specific not tested clouds.

       The tested clouds so far are:
       - Google Drive  
       - OneDrive
       - DropBox
    '''

    def get_config(self) -> dict[str, object] | str:
        '''
        Return package settings.
        '''
        api_name = 'SYNO.CloudSync'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'], 
            'method': 'get_config'
        }

        return self.request_data(api_name, api_path, req_param)
    
    def get_connections(self, group_by: str = 'group_by_user') -> dict[str, object] | str:
        '''
        Return list of current cloud connections.

        group_by = 'group_by_user' ||  'group_by_cloud_type'
        '''
        api_name = 'SYNO.CloudSync'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'], 
            'method': 'list_conn',
            'is_tray': False,
            'group_by': group_by
        }

        return self.request_data(api_name, api_path, req_param)
    
    def get_connection_settings(self, conn_id: int) -> dict[str, object] | str:
        '''
        Return settings from a given connection.

        conn_id = int from get_connections
        '''
        api_name = 'SYNO.CloudSync'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'], 
            'method': 'get_connection_setting',
            'connection_id': conn_id
        }

        return self.request_data(api_name, api_path, req_param)
    
    def get_connection_information(self, conn_id: int) -> dict[str, object] | str:
        '''
        Return information from a given connection.

        conn_id = int from get_connections
        '''
        api_name = 'SYNO.CloudSync'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'], 
            'method': 'get_property',
            'connection_id': conn_id
        }

        return self.request_data(api_name, api_path, req_param)
    
    def get_connection_auth(self, conn_id: int) -> dict[str, object] | str:
        '''
        Return authentication information from a given connection.

        conn_id = int from get_connections
        '''
        api_name = 'SYNO.CloudSync'
        info = self.gen_list[api_name]
        api_path = info['path']
        req_param = {
            'version': info['minVersion'], 
            'method': 'get_conn_auth_info',
            'connection_id': conn_id
        }

        return self.request_data(api_name, api_path, req_param)

