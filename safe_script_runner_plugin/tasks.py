#   Copyright 2015, Denis Makogon
#   All Rights Reserved.
#
#    Licensed under the GNU GENERAL PUBLIC LICENSE,
#    Version 2.0 (the "License"); you may not use this
#    file except in compliance with the License.
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from cloudify.decorators import operation
from fabric_plugin import tasks


def _fabric_env(fabric_env, warn_only):
    """prepares fabric environment variables configuration

    :param fabric_env: fabric configuration
    """
    tasks.ctx.logger.info('preparing fabric environment...')
    fabric_env = fabric_env or {}
    credentials = tasks.CredentialsHandler(tasks.ctx, fabric_env)
    final_env = {}
    final_env.update(tasks.FABRIC_ENV_DEFAULTS)
    final_env.update(fabric_env)
    final_env.update({
        'host_string': credentials.host_string,
        'user': credentials.user,
        'key_filename': credentials.key_filename,
        'key': fabric_env.get('key'),
        'password': credentials.password,
        'warn_only': fabric_env.get('warn_only', warn_only),
        'abort_exception': tasks.FabricTaskError,
    })
    # validations
    if not (final_env.get('password') or
            final_env.get('key_filename') or
            (final_env.get('key') and final_env.get('user'))):
        raise tasks.exceptions.NonRecoverableError(
            'access credentials not supplied '
            '(you must supply at least one of key_filename or password)')
    tasks.ctx.logger.info('environment prepared successfully')
    return final_env


@operation
def run_script(script_path, fabric_env=None, process=None, **kwargs):
    safe_fabric_env = tasks._fabric_env
    tasks._fabric_env = _fabric_env
    try:
        result = tasks.run_script(script_path,
                                  fabric_env=fabric_env,
                                  process=process, **kwargs)
        tasks._fabric_env = safe_fabric_env
        return result
    except BaseException as e:
        tasks.ctx.logger.error(str(e))
        tasks._fabric_env = safe_fabric_env
        raise e
