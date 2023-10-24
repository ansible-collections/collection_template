#!/usr/bin/python
# -*- coding:utf-8 -*-

# Copyright(C) 2023 IEIT Inc. All Rights Reserved.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = '''
---
module: event_log_info
version_added: "1.0.0"
author:
    - WangBaoshan (@ieisystem)
short_description: Get event log information
description:
   - Get event log information on ieisystem Server.
notes:
   - Supports C(check_mode).
options:
    log_time:
        description:
            - Get logs after the specified date, time should be YYYY-MM-DDTHH:MM+HH:MM, like 2019-06-27T12:30+08:00.
        type: str
    count:
        description:
            - Get the most recent log of a specified number.
        type: int
    event_file:
        description:
            - Store logs to a file.
        type: str
extends_documentation_fragment:
    - ieisystem.inmanage.inmanage
'''

EXAMPLES = '''
- name: Event log info test
  hosts: inmanage
  connection: local
  gather_facts: no
  vars:
    inmanage:
      host: "{{ ansible_ssh_host }}"
      username: "{{ username }}"
      password: "{{ password }}"

  tasks:

  - name: "Get event log information"
    ieisystem.inmanage.event_log_info:
      log_time: "2020-06-01T12:30+08:00"
      provider: "{{ inmanage }}"

  - name: "Get event log information"
    ieisystem.inmanage.event_log_info:
      count: 30
      provider: "{{ inmanage }}"

  - name: "Get event log information"
    ieisystem.inmanage.event_log_info:
      event_file: "/home/wbs/wbs.log"
      provider: "{{ inmanage }}"
'''

RETURN = '''
message:
    description: Messages returned after module execution.
    returned: always
    type: str
state:
    description: Status after module execution.
    returned: always
    type: str
changed:
    description: Check to see if a change was made on the device.
    returned: always
    type: bool
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.ieisystem.inmanage.plugins.module_utils.inmanage import (inmanage_argument_spec, get_connection)


class EventLog(object):
    def __init__(self, argument_spec):
        self.spec = argument_spec
        self.module = None
        self.init_module()
        self.results = dict()

    def init_module(self):
        """Init module object"""

        self.module = AnsibleModule(
            argument_spec=self.spec, supports_check_mode=True)

    def run_command(self):
        self.module.params['subcommand'] = 'geteventlog'
        self.results = get_connection(self.module)

    def show_result(self):
        """Show result"""
        self.module.exit_json(**self.results)

    def work(self):
        """Worker"""
        self.run_command()
        self.show_result()


def main():
    argument_spec = dict(
        log_time=dict(type='str', required=False),
        count=dict(type='int', required=False),
        event_file=dict(type='str', required=False),
    )
    argument_spec.update(inmanage_argument_spec)
    log_obj = EventLog(argument_spec)
    log_obj.work()


if __name__ == '__main__':
    main()
